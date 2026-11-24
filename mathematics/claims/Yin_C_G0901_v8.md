---
author: Yin
---

# The full power index in the asymptotic lower bound for a row resultant

<a id="statement"></a>
## A single exponent and all pairs of conjugates

Fix a nontorsion algebraic unit \(\alpha\) with monic minimum \(P\) of degree \(e\).
Put \(x_1,\ldots,x_e\) for its conjugates.
Let \(p\) be a prime and \(U,V\in\mathbb Z[Y]\) nonzero coprime polynomials over \(\mathbb Q\) satisfying
\[
                       P(X)^2\mid U(X^p)+XV(X^p).
\]
Write \(R=\operatorname{Res}(U,V)\ne0\) using the actual row degrees, \(y_i=x_i^p\), \(Q_p=\min_{\mathbb Q}(\alpha^p)\) and \(I=[\mathbb Z[\alpha]:\mathbb Z[\alpha^p]]\).
The coprime graph gives \(V(y_i)\ne0\) and \(x_i=-U(y_i)/V(y_i)\), so the powered nodes retain their fields and are distinct.
Then as \(p\to\infty\) through such primes,
\[
       \log|R|\ \ge\ 4\log I-o_P(p)
          =2pD(P)-o_P(p),\qquad
       D(P)=\sum_{i<j}\left|\log|x_i|-\log|x_j|\right| .                \tag{1}
\]
The error is uniform over all row choices, with no width bound, for this fixed seed.
For a Salem seed with exterior root \(\rho>1\), the leading lower bound is \(4(e-1)p\log\rho\).
The [finite power-index bound](Yin_C_G0345_v365.md#statement) allowed a binomial loss for simultaneous collisions.
The estimate here retains the entire leading index by using disjoint pairs and bounding the cost of combining their conditions, including pairs in the same residue class.

<a id="finite"></a>
## A finite bound with an explicit overlap term

Fix a finite splitting field of \(P\).
At each rational prime \(\ell\ne p\), take a place above \(\ell\) and use its valuation \(v\) normalized by \(v(\ell)=1\).
Write \(r_{ij}=v(y_i-y_j)\) for \(i\ne j\), and define
\[
 E_\ell=\sum_i\ \sum_{\substack{j<k\\j,k\ne i}}\min(r_{ij},r_{ik}) .
\]
The sum is independent of the choice of place, since changing the place permutes the full list of conjugates.
The local and global bounds are
\[
 \begin{split}
        v_\ell(R)&\ge 4v_\ell(I)-8 E_\ell,\\
        \log|R|&\ge4\log I_{p'}-8\sum_{\ell\ne p}E_\ell\log\ell ,
                  \qquad I_{p'}=I/p^{v_p(I)}.                          \tag{2}
 \end{split}
\]
The sums here have finite support.
At primes \(p\) satisfying \(p\ge3M_p\), where \(M_p\) is the largest root multiplicity of \(\bar P\), one can add \((\log p)\sum_Cm_C^2\) to the second right side by the [separate exponent-prime estimate](Yin_C_G0901_v6.md#resultant).

To prove the first bound choose edges on the conjugate indices greedily in order of decreasing \(r_{ij}\), adding an edge precisely if its weight is positive and both endpoints are still unused.
Every omitted edge of positive weight shares an endpoint with a previously selected edge of at least its weight.
Charge it to the minimum of these two weights at that common endpoint.
Different omitted edges give different terms of \(E_\ell\) because the selected and omitted edges are distinguished.
Thus the sum of all omitted weights is at most \(E_\ell\).

Discard from the matching any selected pair with the same original residue.
For such a pair \(v(y_i-y_j)=v(x_i-x_j)\) since the geometric sum for the \(p\)-th power difference is a unit at \(\ell\ne p\).
Pairs with different original residues have \(v(x_i-x_j)=0\).
The [power-index identity](Yin_C_G0231_v1.md#powered-order-index) expresses \(v_\ell(I)\) as the sum of \(v(y_i-y_j)-v(x_i-x_j)\) over \(i<j\).
It follows that the weights of the surviving matching edges sum to at least \(v_\ell(I)-E_\ell\).

<a id="gluing"></a>
## Combining conditions at pairs that need not be comaximal

Order the surviving edges by their original order of selection and choose one representative index \(i_s\) and its partner \(j_s\) at each edge.
For two different edges \(s<t\), \(v(y_{i_s}-y_{i_t})\le r_{i_sj_s}\).
Indeed when \(s\) was selected, both its representative and the still unused representative of \(t\) were available.
Hence this cross term equals \(\min(r_{i_sj_s},r_{i_si_t})\).
Different pairs of matching edges give different terms in \(E_\ell\), and the sum of these cross valuations is at most \(E_\ell\).

Over the valuation ring \(\mathcal O\) of the completed splitting field, each edge gives the quotient
\[
             B_s=\mathcal O[Y]/((Y-y_{i_s})^2,(Y-y_{j_s})^2).
\]
Both rows map to zero there by the [two inverse branches](Yin_C_G0345_v365.md#branches).
Specifically, in the disc centered at \(y_{i_s}\), lift two analytic \(p\)-th-root functions with the distinct original residues of \(x_{i_s},x_{j_s}\).
The derivative \(p x^{p-1}\) is a unit at these unit centers and Hensel lifting gives the branches over \(\mathcal O\).
Each combination \(U+\text{(branch)}V\) vanishes twice at the corresponding powered node, and their difference is \(V\) times a power series with unit constant.
Both \(V\) and then \(U\) vanish in the quotient.
The formal series may be evaluated in \(B_s\): the parameter \(Y-y_{i_s}\) is square-zero there, and \(y_{j_s}-y_{i_s}\) belongs to the maximal ideal.
The length of \(B_s\), scaled so \(\mathcal O/(\ell)\) has length one, is \(4r_{i_sj_s}\).
For example multiplication by \((Y-y_{j_s})^2\) on the two free Taylor coordinates at \(y_{i_s}\) has determinant \((y_{i_s}-y_{j_s})^4\).

Let \(b\) be the number of surviving edges.
On polynomials of degree below \(2b\) the map to \(\bigoplus_s\mathcal O[Y]/(Y-y_{i_s})^2\) has determinant, up to sign,
\(\prod_{s<t}(y_{i_s}-y_{i_t})^4\).
For a direct calculation, use two basis polynomials at each \(s\), namely \(\prod_{j<s}(Y-y_{i_j})^2\) and its product with \(Y-y_{i_s}\).
They are monic in consecutive degrees, and the triangular blocks of their values and first derivatives at the representatives give the asserted determinant.
Passing to the quotients \(B_s\) therefore costs cokernel length at most \(4\sum_{s<t}v(y_{i_s}-y_{i_t})\).

Put \(u=\deg U,\ w=\deg V\).
The double contact forces \(Q_p\mid pY(U'V-UV')-UV\) by eliminating \(x_i\) from the value and derivative equations.
The lowest product term has coefficient multiplied by \(p(\operatorname{ord}_0U-\operatorname{ord}_0V)-1\ne0\), so the polynomial is nonzero of degree at most \(u+w\).
Thus \(u+w\ge e\ge2b\), and the Sylvester target of polynomials of degree below \(u+w\) maps onto at least the image just computed.
Its Sylvester image maps to zero in every \(B_s\).
The normalized length of its cokernel is \(v_\ell(R)\), so
\[
          v_\ell(R)\ge 4\sum_s r_{i_sj_s}
                              -4\sum_{s<t}v(y_{i_s}-y_{i_t}) .
\]
The two bounds on matching loss give (2), also for the empty matching.

<a id="limit"></a>
## The error at fixed seed and the scope of the lower bound

For each fixed triple of distinct indices, the [overlap estimate](Yin_C_G0345_v411.md#overlap) gives a normalized weighted sum of \(\min(r_{ij},r_{ik})\) over all the finite places of the fixed splitting field that is \(o_P(p)\).
It covers a torsion ratio within the triple and uses the cited estimate for the common divisors of two unit differences otherwise.
Summing over triples gives \(\sum_{\ell\ne p}E_\ell\log\ell=o_P(p)\): with \(v(\ell)=1\), the weights for places over \(\ell\) are their local degrees divided by the global degree times \(\log\ell\), and the whole symmetric sum \(E_\ell\) is the same at each such place.
For fixed \(P\), sufficiently large \(p\) do not divide \(\operatorname{disc}P\).
All original residues are then distinct at \(p\), and Frobenius preserves their distinctness, so \(p\nmid I\).
Finally \(|\operatorname{disc}Q_p|=I^2|\operatorname{disc}P|\), and the [archimedean power-discriminant estimate](Yin_C_G0345_v411.md#overlap) gives \(\log|\operatorname{disc}Q_p|=pD(P)+O_P(\log(2p))\).
This proves (1).

In particular \(\deg V\log\|U\|_2+\deg U\log\|V\|_2\ge2pD(P)-o_P(p)\) by the Sylvester determinant bound.
One also has \(D(P)\ge e\,m(P)\) by summing the distances between the positive, negative and zero log moduli of a unit.
For a Salem number the log moduli are \(h,-h,0,\ldots,0\), giving \(D(P)=2(e-1)h\).
The [one-exponent reciprocal divisor](Yin_C_G0345_v493.md#statement) uses reciprocal partners, whereas (1) includes every pair and applies to nonreciprocal seeds as well.
The dependence on the seed in the overlap estimate and the factor \(D(P)\) leave open a lower bound independent of the seed for the original positive Mahler measures.

<a id="overlap-example"></a>
## A reciprocal double contact where the fourth index power does not divide the resultant

Take \(p=7,\ \ell=11,\ a=342\), and
\[
       P(X)=\frac{(a+X)X^7-(1+aX)}{X^2-1}
          =X^6+aX^5+X^4+aX^3+X^2+aX+1 .
\]
This reciprocal unit polynomial is irreducible: modulo seven it is \((X+1)^6\), and \(P(-1)=4-3a\) is divisible by seven just once, making \(P(X-1)\) Eisenstein.
Its root sum \(-a\) excludes roots of unity as its complete conjugate set.
For a root \(x\) put \(y=x^7=(1+ax)/(a+x)\), write \(Q\) for its monic minimum, and set \(A(Y)=aY-1,\ B(Y)=Y-a\).
The inverse \(x=-A(y)/B(y)\) shows that \(Q\) has degree six (the pole \(y=a\) would imply \(a^2=1\)).
Take
\[
       V=7Y B^2 Q',\qquad
       U=7YABQ'+Q\{AB+7Y(a^2-1)\}.
\]
For the value, \(U(y)+xV(y)=0\).
For the derivative in \(Y\), write \(W=7YB Q'\), so \(V=BW,\ U=AW+Q\{AB+7Y(a^2-1)\}\).
At \(Y=y\), substituting \(x=-A/B\) gives
\[
 U'+xV'+\frac{x}{7y}V
    =\left(\frac{1-a^2}{B}-\frac A{7y}\right)W
        +Q'\{AB+7y(a^2-1)\}=0 .
\]
Thus \(P^2\mid U(X^7)+XV(X^7)\).
Both rows have degree eight, and the first has nonzero constant and leading coefficients while the second has zero constant coefficient.
Their reflected determinant is nonzero.

Modulo eleven, \(P=\Phi_7\) has six distinct nonzero roots, none equal to \(-1\).
The differences \(y_i-y_j=(a^2-1)(x_i-x_j)/((a+x_i)(a+x_j))\) all have valuation one because \(v_{11}(a-1)=1\).
Each \(y_i\) reduces to one, so \(v_{11}(I)=15\), and the six roots \((y_i-1)/11\) are integral with distinct residues.
In particular \(11^{-6}Q(1+11Z)\) is integral and squarefree on reduction.

The leading coefficient \(42\) of \(V\) is an eleven-adic unit.
At its root zero \(U(0)=aQ(0)\) is a unit.
At \(a\), counted twice from \(B^2\), \(v_{11}(U(a))=7\), because each \(a-y_i=(a^2-1)/(a+x_i)\) has valuation one.
At each of the five roots \(\gamma\) of \(Q'\), \((\gamma-1)/11\) is integral and \(v_{11}(Q(\gamma))=6\), since the scaled polynomial is squarefree on reduction and its derivative has unit leading coefficient.
Here \(AB\) is divisible by \(11^2\) in the valuation sense, while \(7\gamma(a^2-1)\) has valuation one, so \(v_{11}(U(\gamma))=7\).
These finite values also show that the rows are coprime.
The resultant product over the roots of \(V\) now gives
\[
               v_{11}(R)=2\cdot7+5\cdot7=49
                             <4v_{11}(I_{7'})=60 .
\]
Thus the fourth index power need not divide the row resultant exactly, even for a reciprocal seed, genuine coprime rows and width only two above the seed degree.
This finite collision does not contradict the fixed-seed limit in (1).

## Assessment history

### Decision full-asymptotic-power-index

| Field | Value |
| --- | --- |
| date | 2026-11-24T19:05 |
| status | proved |
| reason | Disjoint collision pairs contribute to the Sylvester length after paying a confluent interpolation index. For a fixed seed the omitted triple overlaps have sublinear logarithmic size. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The finite valuation estimate with its triple-collision correction, the fixed-seed asymptotic at arbitrary row width and the explicit counterexample to an exact fourth-power divisor. |
| argument | [finite](#finite) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [gluing](#gluing) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [limit](#limit) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [overlap-example](#overlap-example) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0345_v365.md#statement) | Local collision quotients for two inverse branches. |
| dependency | [Input](Yin_C_G0345_v411.md#overlap) | The fixed-seed common-divisor estimate for three powered nodes. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1058.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-full-asymptotic-power-index)
