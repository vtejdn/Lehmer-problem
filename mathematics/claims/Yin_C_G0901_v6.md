---
author: Yin
---

# Divisibility of the row resultant at a prime of double contact

<a id="statement"></a>
## A lower bound on the coefficients

Let \(P\in\mathbb Z[X]\) be the monic minimum of an algebraic unit \(\alpha\) of degree \(e\ge2\).
At a prime \(p\), let \(m_C\) be the multiplicities of the distinct roots of \(\bar P\) over \(\overline{\mathbb F}_p\), and assume \(p\ge3\max_C m_C\).
Let \(t\) be any integer prime to \(p\).
Suppose that nonzero integral polynomials \(U,V\) are coprime over \(\mathbb Q\) and that \(P^2\) divides \(U(X^p)+X^t V(X^p)\) in the Laurent ring.
Put \(z=\alpha^p,\ u=\deg U,\ v=\deg V\).
Then \(V(z)\ne0\) by coprimality and the graph value, and
\[
 \begin{split}
 v_p\bigl(N_{\mathbb Q(z)/\mathbb Q}V(z)\bigr)&\ge\sum_C m_C^2,\\
 v_p\operatorname{Res}(U,V)&\ge\sum_C m_C^2 .                         \tag{1}
 \end{split}
\]
Both inequalities can be attained simultaneously by actual integral coprime pairs for this \(P,p,t\), with nonzero reflected determinant and unrestricted widths and heights.
In particular the original row coefficients satisfy
\[
            v\log\|U\|_2+u\log\|V\|_2\ \ge\ \log p\sum_C m_C^2 .       \tag{2}
\]
This estimates the height without an input-measure term on the left.
It also gives \(e\log\|V\|_1+pv\,m(P)\ge\log p\sum_Cm_C^2\) via the archimedean norm bound.
If the same rows have genuine double contacts at several distinct primes satisfying the hypotheses, their corresponding right sides in (2) add, since the integer row resultant is the same.
Accumulating these divisibilities requires a common nonzero integer, which separate choices of the rows need not supply.

<a id="jets"></a>
## Taylor coefficients at each lifted residue

Pass to the ring of integers \(\mathcal O\) of a finite unramified extension of \(\mathbb Q_p\) containing the nonzero residues of all the roots in its residue field, and normalize \(v_p(p)=1\).
At a class \(C\) of size \(m\), take its Teichmüller lift \(\omega\), set \(c=\omega^p\), and put \(z_i=(x_i^p/c-1)/p\) for roots \(x_i\) of \(P\) in this class.
The [local chart](Yin_C_G0901_v5.md#local) has \(v_p(z_i)\ge1/m\), all the powered nodes distinct, and \(x_i^t=\omega^t f_t(z_i)\), where
\[
               f_t(Z)=\sum_{n\ge0} b_n Z^n,\qquad
               b_n=\prod_{j=0}^{n-1}(t-jp)/n! .
\]
The logarithmic derivative in the powered variable \(Y=c(1+pZ)\) gives the contact derivative \(t x_i^t/(p x_i^p)\) as in the [inverse power calculation](Yin_C_G0901_v4.md#series).

Write \(K_C(Z)=\prod_{i\in C}(Z-z_i)\) and \(\mathcal S_C=\mathcal O[Z]/K_C^2\).
The cluster polynomial has coefficients in \(\mathcal O\) by invariance under local Galois automorphisms fixing the residue field and by integrality.
Its reduction is \(Z^m\).
The remainder of \(Z^n\) in the basis of degrees below \(2m\) has coefficient at \(Z^j\) of valuation at least \((n-j)/m\).
Indeed the coefficient at \(Z^j\) in \(K_C^2\) has valuation at least \((2m-j)/m\) by its roots, and the recurrence for monic remainders preserves the inequality from the initial monomials.
For \(n\ge p\) one has
\[
       (n-j)/m-v_p(n!)\ \ge\ (n-2m+1)/m-(n-1)/(p-1)>0 .
\]
This is positive at \(p\) and increases without bound because \(p\ge3m\).
For \(2m\le n<p\) the factorial is a unit and every remainder coefficient has positive valuation.
Consequently \(f_t\) converges in \(\mathcal S_C\), where its reduction is
\[
                  E_t(Z)=\sum_{j=0}^{2m-1}\bar t^{\,j}Z^j/j!
                       \pmod {Z^{2m}} .
\]
The \(2m\) vectors \(Z^j,f_t Z^j\) for \(0\le j<m\) form an \(\mathcal O\)-basis.
To see this, eliminate the first \(m\) coefficient positions with the \(Z^j\).
At positions \(m\le l<2m\) the remaining columns reduce to \(\bar t^{l-j}/(l-j)!\).
After stripping the nonzero powers of \(\bar t\) and multiplying row \(l\) by \(l!\), the columns evaluate the monic falling factorial polynomials of degrees \(0,\ldots,m-1\) at distinct residues \(l\).
The resulting Vandermonde determinant is a unit.

In this algebra, double contact gives
\[
               U(c(1+pZ))+\omega^t f_t(Z)V(c(1+pZ))=0 .                \tag{3}
\]
Over the splitting field this follows by taking both values and first derivatives at every \(z_i\), which determine the class modulo \(K_C^2\).
The series and its derivative converge at each of the nodes by the [series bounds](Yin_C_G0901_v4.md#series).
Write \(A^{[j]}(c)\) for the coefficient of \((Y-c)^j\) in \(A(Y)\).
In (3) all terms of degree \(j\ge m\) in the Taylor expansion of either row carry \(p^j\).
In the basis just proved, each of the first \(m\) coefficients \(c^j p^j U^{[j]}(c)\) and \(\omega^t c^j p^j V^{[j]}(c)\) must therefore lie in \(p^m\mathcal O\).
In particular
\[
           U,V\ \in\ (p,Y-c)^m\subset\mathcal O[Y].                    \tag{4}
\]
At all \(m\) powered nodes in this class, \(v_p(Y-c)\ge1\), so \(V\) takes values of valuation at least \(m\).
All \(e\) powered nodes remain conjugate and distinct by the local chart.
Taking the norm proves the first bound of (1).

<a id="resultant"></a>
## From the Taylor coefficients to the integral resultant

Divide out the joint scalar \(p\)-content of \(U,V\).
The resulting integral pair has the same double contact and satisfies (4) in every class, and restoring the scalar can only increase the valuation of its resultant.
Interchange the names of the two rows for this resultant estimate if necessary, so \(U\) has \(p\)-primitive coefficients.
Write its roots over \(\overline{\mathbb Q}_p\) as \(\gamma_i\), with multiplicities.
Multiplicativity of the \(p\)-adic coefficient Gauss norm follows by rescaling each factor to have integral coefficients and nonzero reduction, then using the polynomial domain of the residue field.
In particular \(p\)-primitivity gives
\[
                 v_p(\operatorname{lc} U)+\sum_i\min(0,v_p(\gamma_i))=0.
\]
Applying the same norm to \(U(c+pZ)\) gives
\[
   \min_j\{v_p(U^{[j]}(c))+j\}
     =\sum_{v_p(\gamma_i-c)>0}\min(1,v_p(\gamma_i-c)).
\]
Indeed each factor contributes \(\min(1,v_p(\gamma_i-c))\), and the negative valuations cancel the leading coefficient as above because \(c\) is a unit.
By (4) the displayed sum is at least \(m\).
At each root counted in it, (4) for \(V\) gives \(v_p(V(\gamma_i))\ge m\min(1,v_p(\gamma_i-c))\).
These roots therefore contribute at least \(m^2\) to the sum of evaluations in this residue class.
Other integral roots contribute nonnegative valuations.
At every nonintegral root we have \(v_p(V(\gamma_i))\ge v\,v_p(\gamma_i)\), whose possible loss is paid by \(v_p((\operatorname{lc}U)^v)\) in the product formula for the resultant.
Summing the distinct residue classes proves (1).
Hadamard's inequality on the integral Sylvester determinant gives \(|\operatorname{Res}(U,V)|\le\|U\|_2^v\|V\|_2^u\), proving (2).

<a id="smith"></a>
## Two generating rows in the local order

There is also an exact description of the intermediate lattice in the transfer from the [integral Bezout determinant](Yin_C_G0901_v4.md#rows).
Over \(\mathcal O\) restrict to the class \(C\), with \(R_C=\mathcal O[x]\) on its \(m\) characteristic-zero conjugates and \(A_C=\mathcal O[x^p]\subset R_C\).
The class factor has reduction \((X-\bar\omega)^m\).
Since \(m<p\), \(x^p/c-1\) is divisible by \(p\) in \(R_C\), giving \(Z=(x^p/c-1)/p\in R_C\).
Within this class \(v_p(z_i-z_j)=v_p(x_i-x_j)\): in \( (x_i/x_j)^p-1\) the linear term has strictly smallest valuation since \(v_p(x_i/x_j-1)\ge1/m>1/(p-1)\).
The two Vandermonde determinants consequently give \([R_C:\mathcal O[Z]]\) unit index, so \(R_C=\mathcal O[Z]\) with relation \(K_C(Z)=0\).

The Smith exponents of \(A_C+x^t A_C\subset R_C\) are
\[
                          \lfloor j/2\rfloor,\qquad 0\le j<m .
\]
In fact \(A_C=\mathcal O[pZ]\) and \(x^t=\omega^t f_t(Z)\) in \(R_C\).
Take \(Z^j\) for \(0\le j<\lceil m/2\rceil\) and \(x^tZ^j\) for \(0\le j<\lfloor m/2\rfloor\).
These are a basis of \(R_C\): above the first \(\lceil m/2\rceil\) coefficient positions the identical factorial evaluation argument to that in the [doubled space](#jets) uses the row positions \(\lceil m/2\rceil,\ldots,m-1\).
Multiplying each selected vector by \(p^j\) gives elements of the stated lattice.
All other generators \(p^j Z^j,p^j x^tZ^j\) with nonnegative \(j\) already lie in the span of the selected weighted vectors, since their omitted weights are at least the maximum selected weight and the unweighted vectors constitute a basis.
This proves the Smith formula with multiplicities.

<a id="sharp"></a>
## Equality for genuine contact pairs without a height constraint

We give actual contact pairs attaining both valuations in (1).
In \(\mathcal S_C\), choose two leading coefficients for polynomials \(\hat U,\hat V\) of degree at most \(m\).
The basis in the [Taylor calculation](#jets) uniquely determines the lower coefficients so that
\[
                    \hat U+\omega^t f_t\hat V=0\quad\text{in }\mathcal S_C .
\]
The leading coefficients can be chosen in the local unramified ring with both reductions nonzero and \(\overline{\hat V}(0)\ne0\).
Indeed the reduced kernel has dimension two.
Its subspace on which both constants vanish (equivalently just \(\overline{\hat V}(0)=0\)) has dimension at most one.
Dividing out \(Z\) leaves degree bounds \(m-1\) with contact modulo \(Z^{2m-1}\), and this system has rank \(2m-1\) by the same basis of monomials and exponential multiples, using the \(m\) ordinary columns and the first \(m-1\) exponential columns.
The two zero leading-coefficient lines and this proper subspace do not cover the two-dimensional residue space, since its finite residue field has at least three elements and therefore at least four projective lines.
The two resulting reduced polynomials \(\overline{\hat U},\overline{\hat V}\) are coprime.
They do not both vanish at zero, and removing any other common irreducible would preserve their contact modulo \(Z^{2m}\) while reducing both degrees below \(m\), contradicting the basis result.

Use \(U_C(Y)=p^m\hat U((Y/c-1)/p)\) and \(V_C(Y)=p^m\hat V((Y/c-1)/p)\), integral polynomials in \(Y\) of degree \(m\).
Make choices over the unramified extension associated to the residue of the class and use their Frobenius conjugates on its orbit.
The class polynomials \(Q_C(Y)=\prod_{i\in C}(Y-x_i^p)\) are pairwise coprime on reduction.
Lift the \(U_C,V_C\) separately by the Chinese remainder theorem modulo the \(Q_C^2\), taking the unique representatives of degrees below \(2e\).
The lifted rows have coefficients in \(\mathbb Z_p\) by invariance under the unramified Galois group.
Take \(Q=\prod Q_C\), and add \(Q^2\) to the first row to make it monic.
Its reduction has multiplicity exactly \(m\) at \(\bar c\), because the leading coefficient of \(\hat U\) is a unit and the congruence fixes \(U_C\) modulo \((Y-\bar c)^{2m}\).
At the remaining root residues of the first row, arrange that the second row has nonzero reduction by adding \(Q^2H\) to it.
Such \(H\) exists over \(\mathbb Z_p\) by polynomial congruences over \(\mathbb F_p\) at the remaining distinct irreducible factors, where \(\bar Q\) is invertible.
These operations preserve (3) on every class.

There are exactly \(m\) first-row roots \(\gamma\) reducing to \(\bar c\), and all have \(v_p(\gamma-c)\ge1\).
Indeed if \(0<v_p(\gamma-c)<1\), the degree-\(m\) Taylor term, whose coefficient is a unit, has strictly smaller valuation than every lower term by (4) and strictly smaller valuation than all higher terms by integrality.
Under the substitution \(Y=c(1+pZ)\), \(Q_C(Y)^2=p^{2m}c^{2m} K_C(Z)^2\).
Thus after dividing the rows by \(p^m\) in this variable their reductions at integral \(Z\) agree with \(\overline{\hat U},\overline{\hat V}\), respectively.
At \(Z=(\gamma/c-1)/p\), coprimality on reduction makes the second row have valuation exactly \(m\).
Its valuation at each powered node in the original class is also exactly \(m\) because every \(z_i\) has positive valuation and \(\overline{\hat V}(0)\ne0\).
The monic first row has only integral roots, and the additional root residues contribute zero.
The prescribed equalities follow over \(\mathbb Z_p\).

Finally approximate the resulting \(p\)-adic pair by a rational pair in the same finite-dimensional linear space of double-contact solutions.
The linear equations are rational by taking remainders modulo \(P^2\) after clearing any negative monomial.
A rational basis spans their kernel over \(\mathbb Q_p\).
Sufficiently close approximations are \(p\)-integral, have the same degrees, and preserve the nonzero norm and resultant valuations by continuity.
A small rational multiple of \(Q^2\) may be added to the second row to secure nonzero reflected determinant, using \(UU^\iota-VV^\iota\) as a quadratic in the multiple with nonzero quadratic coefficient.
This perturbation preserves contact and both valuations (with the first leading coefficient a \(p\)-adic unit even if the degree of the second row increases).
Clearing all denominators by a scalar prime to \(p\) yields integral rows.
Their resultant is nonzero, ensuring coprimality over \(\mathbb Q\).
This proves sharpness with no assertion about the smallest archimedean height attainable by these pairs.

<a id="coverage"></a>
## A Salem family with few repeated roots at every large prime

For a prime proportional to \(e\) and width \(B=O(e)\), the unconditional bound \(\sum_C m_C^2\ge e\) in (2) gives only a lower bound of order \(\log p\) for \(\log H\).
A lower bound of order \(p\) from (2) would follow from \((\log e)\sum_Cm_C^2/e^2\) bounded away from zero.
Along a hypothetical shrinking sequence the [short original rows](Yin_C_G0901_v5.md#short) show that such concentration must fail throughout any fixed positive linear prime interval.

Even with all power degrees preserved, it is impossible to supply that concentration on every bounded-measure input.
Set \(Q_0=X^3-X-1,\ Q_0^*=1-X^2-X^3,\ F_N=X^NQ_0+Q_0^*\) for \(N\ge1\).
These are [Salem–Boyd polynomials](../audits/literature/Hir06/readme.md#reciprocal-sequence-method-attribution).
The cubic has one real root \(\theta>1\), since both local extrema are negative, and its other two roots have modulus \(\theta^{-1/2}<1\) by the product of the roots.
On the circle the ratio \(X^NQ_0/Q_0^*\) thus has degree \(N+1\).
The value \(-1\) has at least \(N+1\) distinct circle preimages, as follows by lifting the argument over one turn.
One has \(F_N(\theta)=-\theta^2-\theta<0\) and \(F_N(\theta+\varepsilon)>0\) eventually for each fixed \(\varepsilon>0\).
The reciprocal polynomial \(F_N\) of degree \(N+3\) thus has exactly one exterior root \(\lambda_N>\theta\) for large \(N\), and \(\lambda_N\to\theta\).
These roots are distinct because \(Q_0,Q_0^*\) have no common root.
Their monic irreducible unit factors \(P_N\) contain the inverse of the exterior root by the norm, and their degrees \(e_N\) tend to infinity since bounded degree and bounded measure would give only finitely many integer polynomials.
Consequently the \(\lambda_N\) are Salem numbers eventually.
Every positive power preserves their degree: all fibers on the conjugates of a power have the same cardinality, and the fiber at the unique exterior conjugate is a singleton.

For every prime \(q\ne23\), the polynomial
\[
 XQ_0F_N'-(NQ_0+XQ_0')F_N
      =XQ_0(Q_0^*)'-(NQ_0+XQ_0')Q_0^*
\]
has degree at most six and is nonzero modulo \(q\).
Indeed \(Q_0\) has discriminant \(-23\) and nonzero constant term, while \(Q_0+Q_0^*=-X(X+1)\) and \(Q_0(0)=Q_0(-1)=-1\).
Evaluation at any such root makes the right side nonzero.
Hence \(\deg\gcd(\bar P_N,\bar P_N')\le\deg\gcd(\bar F_N,\bar F_N')\le6\).
If \(m_C\) are the multiplicities of the distinct residues of \(P_N\), then \(\sum_C(m_C-1)\le6\), and
\[
                    e_N\le\sum_Cm_C^2\le e_N+42
                 \qquad\text{at every prime }q\ne23 .
\]
The upper bound follows by putting all six possible excess multiplicities in a single class.
These genuine inputs have \(m(P_N)\to\log\theta>0\).
Concentration on inputs whose positive measures tend to zero remains open.

## Assessment history

### Decision sharp-row-resultant

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:35 |
| status | proved |
| reason | The local jet forces the Taylor valuations, and actual unrestricted-height pairs attain both valuation bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Sharp local divisibility of the norm and resultant for ordinary double contacts. |
| argument | [jets](#jets) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [resultant](#resultant) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [smith](#smith) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [sharp](#sharp) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [coverage](#coverage) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0901_v5.md#local) | The local chart applies when the prime is at least three times the maximum residue multiplicity. |
| dependency | [Input](Yin_C_G0901_v4.md#series) | The inverse power on a lifted residue gives its doubled jet. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1049.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-sharp-row-resultant)
