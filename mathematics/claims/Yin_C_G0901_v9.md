---
author: Yin
---

# Coefficient growth at a fixed power map and increasing root multiplicity

<a id="statement"></a>
## The exact cost for a set of residue classes

Fix an integer \(q\ge2\), a nonempty set \(S\subseteq\{0,\ldots,q-1\}\), and a nontorsion algebraic unit \(\alpha\).
Put \(\beta=\alpha^q\), \(E=\mathbb Q(\alpha)\), \(K=\mathbb Q(\beta)\), and write \(m\) for total logarithmic Mahler measure.
For each nonempty \(J\subseteq S\) let
\[
 r(J)=\dim_K\operatorname{span}_K\{\alpha^s:s\in J\},
 \qquad \rho(S)=\min_{\varnothing\ne J\subseteq S}\frac{r(J)}{|J|}.
\]
Let the integral row width \(B=B(a)\) satisfy \(B/a\to\infty\) and \(\log(B+2)=o(a)\) as the positive integer \(a\) tends to infinity.
Consider all nonzero \(F=\sum_{s\in S}X^s U_s(X^q)\) with integral rows of degree at most \(B\) and \(\operatorname{ord}_\alpha F\ge a\).
Then
\[
             \lim_{a\to\infty}\frac1a\log\min_F\|F\|_1
                            =\rho(S)m(\beta).                             \tag{1}
\]
Some allowed rows may be zero.
If \(\rho(S)<1\), (1) also holds when at least one of the row values \(U_s(\beta)\) is required to be nonzero.
If \(\rho(S)=1\), every row of every such multiple vanishes to order at least \(a\) at \(\beta\), so that additional requirement is impossible.
When \(E=K\) the answer is \(qm(\alpha)/|S|\).
For the full set of \(q\) classes the answer is \(m(\alpha)\) even when the power lowers the degree: divisibility by the \(a\)-th power of the monic minimum gives the lower bound and \(r(S)=[E:K]\) gives the matching upper bound.
All limits here fix \(\alpha,q,S\).

<a id="wronskian"></a>
## Independent conjugate combinations in one Wronskian

For an actual nonzero graph let \(J\) denote its occupied classes, \(l=|J|\), \(r=r(J)\), \(L=q(B+1)\), and \(c=\min_{s\in J}\operatorname{ord}_\beta U_s\).
The \([E:K]\) embeddings of \(E\) over \(K\) send \(\alpha\) to \(\zeta_i\alpha\) with \(\zeta_i^q=1\).
The matrix with columns \(\bigl((\zeta_i\alpha)^s\bigr)_i\), \(s\in J\), has rank \(r\).
Indeed the embeddings on a \(K\)-basis of \(E\) form an invertible matrix by separability, and the coordinate matrix of the listed powers in that basis has rank \(r\).
Dividing each column by \(\alpha^s\) preserves rank.
Select \(r\) independent coefficient rows \((\zeta_i^s)_{s\in J}\).

Form the [integral Euler Wronskian](Yin_C_G0345_v362.md#determinant) of the \(l\) polynomials \(G_s=X^s U_s(X^q)\), with derivatives \((X\,d/dX)^j\), \(0\le j<l\).
The determinant is \(X^{\sum_{s\in J}s}W(X^q)\), where \(W\in\mathbb Z[Y]\) is nonzero by the Vandermonde leading coefficient at the distinct top exponents.
Its norm is at most \(l!(1+L)^{l(l-1)/2}\|F\|_1^l\).
Remove the factor \(D=(X^q-\beta)^c\) from each column polynomial before differentiating.
The Leibniz rule multiplies the resulting Wronskian by \(D^l\).
Take an invertible constant change of columns whose first \(r\) columns give the combinations \(F(\zeta_i X)/D\) for the selected embeddings.
These \(r\) polynomials vanish at \(\alpha\) to order at least \(\max(0,a-c)\).
Each of the first \(l\) Euler derivatives in each such column has order at least \(\max(0,a-c-l+1)\).
Consequently
\[
 \operatorname{ord}_\beta W
 \ge lc+r\max(0,a-c-l+1)\ge r(a-l+1)+(l-r)c .
\]
Since \(W\) is integral, every conjugate of \(\beta\) has this order.
Mahler measure and the norm bound give
\[
  [r(a-l+1)+(l-r)c]m(\beta)
      \le l\log\|F\|_1+\log(l!)+\tbinom l2\log(1+L).                    \tag{2}
\]
This gives the lower bound in (1) since \(l\) is bounded and \(\log(B+2)=o(a)\).
When \(r=l\), the selected embeddings directly express each \(G_s\) as a constant linear combination of the \(F(\zeta_iX)\), so each \(U_s\) vanishes to order at least \(a\) at \(\beta\).

<a id="boxes"></a>
## Counting the independent jet coordinates

Choose a set \(J\) attaining the least ratio, with its cardinality \(l\) as small as possible, and put \(r=r(J)\), \(d_0=[K:\mathbb Q]\).
Use a basis of the \(K\)-span consisting of \(r\) of the \(\alpha^s\).
Their remaining coordinates are fixed elements of \(K\), all integral after multiplying by a fixed positive integer.
Write \(t\) for the multiplicity to be constructed.
Use an operative width \(b\) for which \(f=b/t\to\infty\) and \(b\le t^2\), and set \(N=l(b+1)\), \(L_0=q(b+1)\).
Test the \((H+1)^N\) coefficient choices in \([0,H]\).
The \(j\)-th divided derivative at \(\alpha\), multiplied by \(\alpha^j\), sends a term \(X^{qi+s}\) to \(\binom{qi+s}{j}\beta^i\alpha^s\).
Thus each jet is determined by \(r\) elements of \(K\).
After the fixed denominator is cleared, their absolute values at an embedding \(\sigma\) are at most
\[
 C N H\binom{L_0}{j}\max(1,|\sigma(\beta)|)^b .
\]
Here and below constants may depend on \(\alpha,q,S\).
Use real coordinates at real places and two real coordinates at each conjugate pair of complex places.
Two different algebraic integers cannot lie in the same box of side \(1/2\) in all these coordinates, by the nonzero integral norm of their difference.
As in the [integral jet count](Yin_C_G0345_v362.md#jets), the number of distinct tuples of the first \(t\) jets is at most
\[
 (C'NH)^{r d_0 t}
 \left(\prod_{j=0}^{t-1}\binom{L_0}{j}\right)^{r d_0}
 \exp\!\bigl(rbt\,m(\beta)\bigr).
\]
The sum of the logarithms of the binomials is \(O_q(t^2\log(2+f))\).
Indeed \(\binom{L_0}{j}\le(\mathrm e L_0/j)^j\) for \(j>0\) and the majorant \(j\log(\mathrm e L_0/j)\) increases for \(j\le t\).
Eventually \(N>rd_0t\).
Choose \(H\) as the next integer above the exponential of
\[
 \frac{rbt\,m(\beta)+r d_0t\log(C'N)+r d_0\sum_{j<t}\log\binom{L_0}{j}}{N-rd_0t}.
\]
Subtract two different choices with equal jets.
The resulting nonzero graph \(F_0\) has order at least \(t\) and its norm satisfies
\[
       \log\|F_0\|_1\le \rho(S)t\,m(\beta)
               +O\!\left(t\frac{\log(2+f)}{f}+\log(2t)\right).           \tag{3}
\]
Here \(\log N=O(\log(2t))\), and expanding \(1/(1-rd_0t/N)\) costs \(O(t/f)\) in the leading term.
Taking \(t=a,\ b=\min(B(a),a^2)\) proves the upper bound in (1).

<a id="values"></a>
## Removing a common zero by a divided derivative

Suppose \(\rho(S)<1\), fix \(\epsilon>0\), take \(t=\lceil(1+\epsilon)a\rceil\), and set \(b=\min(B(a)-1,t^2)\).
These choices still have \(f=b/t\to\infty\).
For all sufficiently large \(a\) every class in the chosen \(J\) is occupied in (3).
Otherwise (2) on a proper subset would give a strictly larger limiting lower cost per unit multiplicity, by the minimal cardinality of \(J\).
In particular \(l-r>0\).
Apply (2) to \(F_0\) with \(t\) in place of \(a\) and \(b\) in place of \(B\).
As \(m(\beta)>0\), its common order \(c\) satisfies
\[
       c/t=O\!\left(\frac{\log(2+f)}{f}+\frac{\log(2t)}{t}\right).
\]
Use \(F_1=X^c F_0^{(c)}/c!\), which still has integral coefficients and the same allowed residue classes.
Its order at \(\alpha\) is at least \(t-c\ge a\) eventually.
At a row of exact common order \(c\), the original \(X^sU_s(X^q)\) has exactly that order at \(\alpha\), so the corresponding row of \(F_1\) takes a nonzero value at \(\beta\).
The norm multiplier is at most \(\binom{L_0}{c}\), whose logarithm is \(o(t)\).
For \(c>0\) this follows by writing \(x=c/t\) and bounding its normalized logarithm by \(x\log(\mathrm e L_0/(tx))\).
One has \(x\log(2+f)\to0\) by the displayed estimate and \(f\le t\), and \(x\log(1/x)\to0\).
For \(c=0\) the multiplier is one.
Letting \(\epsilon\downarrow0\) gives (1) with the nonzero row value.

<a id="lehmer"></a>
## A finite criterion for the unrestricted problem with the exponent fixed

Fix any one integer \(q\ge2\), either sign \(\sigma=\pm1\), and the same width schedule \(B(a)\).
For \(a\ge2\) form \(H_a\) by taking the least of \(2^{\lceil qa/2\rceil}\) and the one-norms of integral rows \(A\) of degree at most \(B\) for which
\[
         A(X^q)+\sigma X A^{*B}(X^q),\qquad A^{*B}(Y)=Y^B A(1/Y),
\]
has a nonzero nontorsion root \(\alpha\) of order at least \(a\) with \(A(\alpha^q)\ne0\).
Then for the unrestricted infimum \(\lambda\) of positive total logarithmic Mahler measures,
\[
 \lambda\le \frac{\log((2qB+1)H_a^2)}{(a-1)q},
 \qquad
                 \lim_{a\to\infty}\frac{2\log H_a}{qa}=\lambda .         \tag{4}
\]
This fixes the exponent even at \(q=2\), in contrast to the [growing prime and multiplicity test](Yin_C_G0345_v417.md#statement).
For computable \(B\) each search is finite by bounding coefficients by the initial candidate, factoring the signed graph and testing for cyclotomic factors and nonzero row values.

For the lower bound use the [derivative identity](Yin_C_G0345_v417.md#elimination), valid for every integer \(q\ge2\).
The nonzero row value recovers \(\alpha\) from \(\alpha^q\).
The \((a-1)\)-st power of the primitive minimum of \(\alpha^q\) divides a nonzero integral polynomial of norm at most \((2qB+1)H_a^2\).
This gives the stated inequality also for nonunit inputs, and the default candidate suffices since \(\lambda\le\log2\).
For the upper bound it suffices to approach \(\lambda\) by reciprocal nontorsion units by the [small-measure reduction](Yin_C_G0345_v408.md#lower).
Each has an [all-power representative of exactly the same measure](Yin_C_G0345_v421.md#norm), still a reciprocal unit.
Apply the nonzero-value construction with residues \(0,1\) at such a representative.
Here \(r=1,l=2\), so the resulting \(U(X^q)+XV(X^q)\) has rate at most \(qm(\alpha)/2\) in (1) and both row values are nonzero by the value equation.
Write \(b\le B-1\) for the operative width of this construction.
Reverse the graph about \(qb+1\) and add it to the graph with either sign \(\delta\).
The reciprocal minimum still divides the sum to the required multiplicity, and one choice gives \(A_\delta(\beta)\ne0\) for \(A_\delta=U+\delta V^{*b}\), since their sum is \(2U(\beta)\).
Now multiply \(A_\delta\) by \(Y^{B-b}+\sigma\delta\), a reversal eigenpolynomial of sign \(\sigma\delta\) with nonzero value at the nontorsion point.
The final signed graph at formal width \(B\) is the previous signed graph times this multiplier at \(X^q\).
Its row norm is at most \(2(\|U\|_1+\|V\|_1)\).
Taking the limsup at each representative and then the infimum over representatives yields (4).
A degree-independent positive lower exponential rate in (4) remains to be proved.

## Assessment history

### Decision fixed-power-coefficient-rate

| Field | Value |
| --- | --- |
| date | 2026-11-24T19:30 |
| status | proved |
| reason | Independent embeddings over the power field give the Wronskian lower rank. Integral jet counting attains it, and a divided derivative removes a common zero with sublinear logarithmic cost. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The least coefficient growth on allowed classes, the nonzero-value dichotomy and the signed finite criterion for unrestricted Lehmer at a single fixed exponent. |
| argument | [wronskian](#wronskian) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [boxes](#boxes) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [values](#values) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [lehmer](#lehmer) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0345_v362.md#determinant) | The integral Euler Wronskian and its coefficient bound. |
| dependency | [Input](Yin_C_G0345_v362.md#jets) | Box counting for integral divided derivatives. |
| dependency | [Input](Yin_C_G0345_v417.md#elimination) | The signed two-row derivative identity. |
| dependency | [Input](Yin_C_G0345_v421.md#norm) | A measure-preserving representative with no power-degree loss. |
| dependency | [Input](Yin_C_G0345_v408.md#lower) | Reduction of the unrestricted infimum to reciprocal nontorsion units. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1061.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-fixed-power-coefficient-rate)
