---
author: Yin
---

# A divided-difference determinant for double contacts at every prime above three times the seed degree

<a id="determinant"></a>
## The determinant at the powered nodes

Let \(P\) be the monic minimum of an algebraic unit of degree \(e\ge2\), with conjugates \(x_1,\ldots,x_e\).
Fix a prime \(p\ge3e\) and an integer \(t\) not divisible by \(p\), of either sign.
Write \(y_i=x_i^p\) and \(Q=\prod_i(Y-y_i)\).
All \(y_i\) are distinct and \(Q\) is irreducible by the [power-field argument for \(p>e+1\)](Yin_C_G0901_v2.md#finite).
Take the roots in a finite extension of \(\mathbb Q_p\), with \(v(p)=1\), and group the \(x_i\) by their residues in its residue field.
Write \(m_C\) for the size of each class \(C\).
Define the \(e\)-by-\(e\) Loewner matrix by
\[
 L_{ij}=\frac{x_i^t-x_j^t}{y_i-y_j}\quad(i\ne j),\qquad
 L_{ii}=\frac{t x_i^t}{p y_i}.
\]
It is nonsingular, and
\[
          v(\det L)-v(\operatorname{disc}Q)=-\sum_C m_C^2 .              \tag{1}
\]
The classes are the root multiplicities in the reduction over an algebraic closure of the residue field, including distinct conjugate residues separately.

<a id="series"></a>
## The inverse power on a residue class

In the individual local field \(\mathbb Q_p(x_i)\), let \(\omega\) be the Teichmüller lift of the residue of \(x_i\).
It belongs to this field by Hensel lifting the nonzero residue as a root of unity of order dividing the order of the residue field's multiplicative group.
Lifts of the same residue agree in the splitting field.
The ramification index of this individual field is at most \(e\), so \(v(x_i/\omega-1)\ge1/e\).
Define \(z_i=(y_i/\omega^p-1)/p\).
In the binomial expansion of \((1+u)^p-1\) for \(u=x_i/\omega-1\), the term \(pu\) has strictly lowest valuation when \(u\ne0\), since \(v(u)\ge1/e>1/(p-1)\).
Thus \(v(z_i)\ge1/e\), also when \(u=0\).

Put
\[
 f_t(Z)=(1+pZ)^{t/p}=\sum_{n\ge0}b_n Z^n,\qquad
 b_n=\frac{\prod_{j=0}^{n-1}(t-jp)}{n!}.
\]
The numerator is a \(p\)-adic unit, and \(v_p(n!)\le(n-1)/(p-1)\) for \(n\ge1\).
The series therefore converges at \(v(Z)\ge1/e\).
The formal binomial identities \(f_1^p=1+pZ,\ f_t=f_1^t\) give the same identities at these points, including negative \(t\) since \(f_1(Z)\) is a unit.
Also \(v(f_1(z_i)-1)>1/(p-1)\).
A \(p\)-th root of unity at this distance from one must equal one, by the same lowest-term comparison for \((1+u)^p-1\).
It follows that \(f_1(z_i)=x_i/\omega\) and \(x_i^t=\omega^t f_t(z_i)\).
Differentiation in \(y_i=\omega^p(1+p z_i)\) gives \(t x_i^t/(p y_i)\).

<a id="reduction"></a>
## Divided differences inside each residue class

Order the nodes in each class.
In its rows, replace row \(a+1\) of \(pL\) by the divided difference on the first \(a+1\) nodes in the coordinate \(z\), computed from the original rows, for \(0\le a<m_C\).
Perform the corresponding column operations within each class.
The nodes are distinct, so these transformations are invertible.
On monomials the divided difference of order \(a\) on \(z_0,\ldots,z_a\) kills degrees below \(a\), and sends \(Z^u\), \(u\ge a\), to the complete homogeneous symmetric polynomial of degree \(u-a\) on these nodes.
This follows by applying the divided-difference recurrence to \(1/(1-ZT)\), whose order-\(a\) difference is \(T^a/\prod_{j=0}^a(1-z_jT)\).

On a diagonal block the kernel before the operations is
\[
 \omega^{t-p}\frac{f_t(Z)-f_t(W)}{Z-W}
      =\omega^{t-p}\sum_{u,v\ge0} b_{u+v+1} Z^uW^v ,
\]
where the diagonal values use the derivative.
After differences of orders \(a,b\), a term with \(n=u+v+1\) and \(d=a+b+1\le2e-1\) can survive only if \(u\ge a,v\ge b\).
Its valuation is at least
\[
                    (n-d)/e-v_p(n!).
\]
For \(d<n<p\) this is positive.
At \(n\ge p\) it is at least \((n-d)/e-(n-1)/(p-1)\), positive at \(n=p\) because \(p\ge3e\), and increasing without bound thereafter.
Thus only \(n=d\) survives reduction, at \(u=a,v=b\).
The reduction of the entry is \(\bar\omega^{\,t-p}\bar t^{\,a+b+1}/(a+b+1)!\).

On two distinct classes with lifts \(\omega,\tau\), the kernel is
\[
 p\,\frac{\omega^t f_t(Z)-\tau^t f_t(W)}
          {\omega^p-\tau^p+p(\omega^p Z-\tau^p W)} .
\]
The constant term of the denominator is a unit because Frobenius preserves distinct residues.
Its geometric inverse has integral coefficients and the coefficient of bidegree \((u,v)\) has valuation at least \(u+v\).
The displayed kernel therefore has coefficients of total degree \(n\) of valuation at least \(1-v_p(n!)\).
After the two differences put \(d=a+b\le2e-2\).
For \(n\ge d\) the additional contribution is at least \((n-d)/e\), and terms of degree less than \(d\) vanish.
The bounds for \(n<p\) and \(n\ge p\) above prove strictly positive valuation for every surviving term.
They also justify termwise evaluation of both divided differences, since the tails converge to zero after the operations.
All off-diagonal blocks vanish on reduction.

For a diagonal block of size \(m\), remove its nonzero residue scalars and the row and column powers of \(\bar t\).
Multiplying row \(a\) of the remaining matrix by \((a+m)!\), a unit since \(a+m<p\), gives the value at \(a\) of the monic polynomial \(\prod_{j=b+2}^m (X+j)\) in column \(b\).
These polynomials have distinct degrees \(m-1-b\) for \(0\le b<m\).
Their evaluation matrix on \(0,\ldots,m-1\) is invertible by the Vandermonde determinant.
Thus the transformed full matrix has unit determinant.
The determinant of the row transformation on a class is \(1/\prod_{i<j\in C}(z_j-z_i)\), by its triangular diagonal coefficients, and the column transformation has the same determinant.
Within a class \(v(y_j-y_i)=1+v(z_j-z_i)\), while between classes it is zero.
Using \(v(\operatorname{disc}Q)=2\sum_{i<j}v(y_j-y_i)\) gives
\[
 v(\det L)-v(\operatorname{disc}Q)
      =-e-2\sum_C\binom{m_C}{2}=-\sum_C m_C^2 .
\]

<a id="rows"></a>
## Minimum row spans and divisibility of the row norm

Suppose \(U,V\in\mathbb Z[Y]\) are nonzero and \(P^2\mid U(X^p)+X^t V(X^p)\) in the Laurent ring.
If both occupied exponent spans were smaller than \(e\), removing the lowest monomial of each row would change \(t\) by a multiple of \(p\) and give rows of degree less than \(e\).
Their values at the \(y_i\) would all be nonzero because \(Q\) is irreducible of degree \(e\).
In general, whenever \(V(y_1)\ne0\), rationality implies \(V(y_i)\ne0\) for every \(i\).
For \(R=-U/V\), value and derivative contact give \(R(y_i)=x_i^t,\ R'(y_i)=(t/p)x_i^t/y_i\).
Indeed differentiation of \(R(X^p)-X^t\) at \(x_i\) gives the latter identity.
The polynomial
\[
 K(Y,Z)=\frac{V(Y)U(Z)-U(Y)V(Z)}{Y-Z}
\]
therefore evaluates on these nodes to the matrix \(\operatorname{diag}(V(y_i))L\operatorname{diag}(V(y_i))\), including the diagonal by continuity.
For row degrees at most \(l\) it has degree at most \(l-1\) in each variable and its evaluation matrix has rank at most \(l\) (a zero numerator gives rank zero).
Taking \(l<e\) contradicts (1) for the shifted rows and their adjusted offset.
Thus the two spans cannot both be smaller than \(e\).

For arbitrary row degrees and \(V(y_1)\ne0\), reduce \(K(Y,Z)\) by the monic \(Q\) separately in both variables and let \(D\) be the resulting integral \(e\)-by-\(e\) coefficient matrix in ascending powers.
The evaluation matrix is the Vandermonde matrix on \(y_i\) times \(D\) times its transpose.
Taking determinants and valuations gives the exact equality
\[
       v_p(\det D)=2v_p\!\left(N_{\mathbb Q(y_1)/\mathbb Q}V(y_1)\right)
                    -\sum_C m_C^2\ \ge0.                                \tag{2}
\]
In particular the norm is a nonzero integer divisible by \(p^{\lceil\sum_C m_C^2/2\rceil}\).
For \(B\ge\deg V\), \(h=m(P)\), and \(H\ge\|V\|_1\), the archimedean embeddings give
\[
       \tfrac12\log p\sum_C m_C^2
          \ \le\ \log|N V(y_1)|\ \le\ e\log H+pBh .                   \tag{3}
\]
The upper bound uses \(|V(x_i^p)|\le H\max(1,|x_i|)^{pB}\) at every embedding.

<a id="height"></a>
## A short pair for every original seed at all these primes

Let \(P\) now be reciprocal and nontorsion, \(B=e+k\) with integer \(k\ge0\), \(r=k+1,\ s=\min(r,e)\).
At every prime \(p\ge3e\) the [ordinary two-row conditions](Yin_C_G0345_v408.md#statement) for this very seed, with offset one and before imposing the coefficient cutoff, have a solution satisfying
\[
 \log H\ \le\
 \frac{2(pB+1)h+2e\log(6N)+e\log(2+pB)+(2r-s)\log3}{s}
       +\log(10(B+1))+k\log(2\mathrm e B/k),\qquad N=2B+2 .             \tag{4}
\]
The last term is zero at \(k=0\) and \(\mathrm e=\exp(1)\).
As before \(H\) denotes the maximum coefficient one-norm of the two rows.

To verify (4), consider any rational linear subspace of double-contact pairs of width at most \(B\) where \(UU^\iota=VV^\iota\) identically.
If its dimension exceeded \(r\), imposing the \(r\) equations that the coefficients of \(Y^e,\ldots,Y^B\) in \(U\) vanish would leave a nonzero pair.
Both its rows would be nonzero, and their occupied exponent spans would be equal because the highest exponent of the nonzero \(UU^\iota\) equals the span of \(U\), and likewise for \(V\).
Both spans would thus be smaller than \(e\), contrary to the [minimum span just proved](#rows).
The unwanted dimension is at most \(r\) regardless of ramification.
The [subspace with zero row values](Yin_C_G0901_v2.md#finite) still has dimension at most \(2r-\min(r,e)\), since the powered minimum has full degree.
The [same two-jet box](Yin_C_G0901_v2.md#finite) with these two bounds produces a pair of nonzero reflected determinant and nonzero values, and the [common divisor estimate](Yin_C_G0901_v2.md#division) gives (4).

For \(0<h\le1\) take \(k=\lceil e\sqrt h\rceil\).
Uniformly in every prime \(p\ge3e\), the resulting pairs satisfy
\[
      h\le \frac{\log H}{p}\ll
                 \sqrt h\log(2/\sqrt h)+\frac{\log(2e)}{\sqrt e}.          \tag{5}
\]
For clarity, \(B\le2e,\ s\ge r/2\), and \(\log(2+pB)/p\) decreases for \(p\ge3e\), so its maximum here is \(O(\log(2e)/e)\).
Divide (4) by \(p\) and use \(eh/r\le\sqrt h\), \(h\ge(\log2)/(4e)\) by the [house estimate](Yin_C_G0345_v869.md#degree), and \(\sqrt h\le k/e\ll\sqrt h\).
The lower bound follows by [reflected elimination](Yin_C_G0345_v408.md#lower).

Thus the [finite degree test](Yin_C_G0901_v2.md#gap), with score \((B-e)/e+(\log H)/p\), can use any single preassigned prime \(p(e)\ge3e\) at degree \(e\).
A vanishing unrestricted infimum supplies seeds of positive measures tending to zero and degrees tending to infinity by the reciprocal-unit reduction.
The same original seed passes at every \(p\ge3e\) at its degree, with scores tending uniformly to zero and \(H\le2^p\) eventually.
If desired one may first [choose a representative whose powers all preserve degree](Yin_C_G0345_v421.md#norm) at each small measure and apply this conclusion directly to those representatives.
Conversely a sequence of such scores tending to zero forces the infimum to vanish by the individual lower bound and the fallback \(\log2\).
The [construction for arbitrarily slowly diverging prime cutoffs](Yin_C_G0901_v3.md#statement) has a different scope because it may enlarge the degree by power substitution and also enforces primitive exponent differences of the parent.

<a id="clusters"></a>
## A necessary bound on concentration in a residue class

Fix \(K_0>3\).
For any sequence of reciprocal nontorsion unit minima with \(h\to0\) and \(e\to\infty\), equations (3) and (5) imply
\[
           \sup_{3e\le p\le K_0 e,\ p\ {\rm prime}}
                \frac{\log e}{e^2}\sum_C m_C^2\ \longrightarrow\ 0,       \tag{6}
\]
where the sum in (6) runs over residue classes at the selected prime.
Indeed \(B\le2e,\ p/e\le K_0\), and division of (3) by \(e^2\), with \(\log p\ge\log e\), bounds the quantity by a constant depending only on \(K_0\) times \((\log H)/p+h\).
Consequently every individual class has size \(o(e/\sqrt{\log e})\), uniformly over these primes.
If every sufficiently small positive-measure reciprocal unit supplied a prime in such an interval with normalized sum in (6) bounded below by a fixed positive constant, (6) would rule out a sequence with measures tending to zero.
The existence of such a prime for every candidate is open.

## Assessment history

### Decision local-determinant

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:04 |
| status | proved |
| reason | The prime-adic block calculation also covers primes dividing the discriminant. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#determinant) | The exact valuation of the divided-difference determinant, norm divisibility and original-seed bounds at every prime at least three times the degree. |
| argument | [Series](#series) | Local inverse power at each residue. |
| argument | [Reduction](#reduction) | Block reduction and valuation with all multiplicities. |
| argument | [Rows](#rows) | Rank obstruction and norm divisibility. |
| argument | [Height](#height) | Original-seed height bound. |
| argument | [Clusters](#clusters) | Necessary modular concentration bound for small total measure. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1045.md#finding) | The precise statement and proof at the stated dependency interfaces. |

## Current assessment

[Selected decision](#decision-local-determinant)
