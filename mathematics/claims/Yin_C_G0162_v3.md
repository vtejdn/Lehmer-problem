---
author: Yin
---

# Salem units below the plastic number with minimal local mixed resultants

<a id="statement"></a>
## Simultaneous control in a growing range of primes and powers

Let \(\theta\) be the real root of \(z^3-z-1\) greater than one.
There are monic irreducible reciprocal polynomials \(S\) of degrees \(d\to\infty\), with coefficients in \(\{-1,0,1\}\), each having exactly one root outside the unit circle.
Their complete Mahler measures satisfy \(1<M(S)<\theta\) and tend to \(\theta\).
All positive powers of each root retain degree \(d\).
For an absolute \(c>0\) put \(T_d=c(\log d)^{1/5}\).
For every prime \(p\le T_d\), the splitting field is unramified at \(p\), and every factor of \(\bar S\) over \(\mathbb F_p\) has degree greater than \(6T_d^2\).

Let \(x_i\) range over all \(d\) roots, and write \(R_{a,b}=\prod_{i,j}(x_i^a-x_j^b)\) for distinct positive integers \(a,b\).
This nonzero integer is the signed mixed resultant on the original root labels.
For \(p,a,b\le T_d\) its valuation is exactly
\[
 v_p(R_{a,b})=
 \begin{cases}
  d(1+v_p(\min(a,b)))&
   \max(a,b)/\min(a,b)\text{ is a positive power of }p,\\
  0&\text{otherwise}.
 \end{cases}                                                        \tag{1}
\]
In the first case precisely \(d\) pairs contribute, each with the displayed valuation divided by \(d\).
Also \(p\) divides none of the cyclic resultants \(\prod_i(x_i^n-1)\) for \(1\le n\le T_d\).

For the [original conjugate-pair criterion](Yin_C_G0162_v2.md#statement), at every such \(p\) the largest compatible fraction \(\beta\) on one Galois orbit satisfies
\[
          \frac1{d-2}\le\max_\Omega \beta\ll_\epsilon d^{-1+\epsilon}
                                  \quad(\epsilon>0).                     \tag{2}
\]
These examples rule out imposing a square-root matching threshold or a surplus over (1) on all inputs with \(1<M(S)<\theta\).
At the degree itself, \(B_d=|\operatorname{Res}(S,z^d+1)|\) has prime factors only above \(T_d\) and \(d^{-1}\log B_d\to\log\lambda>\log2\), where \(\lambda\) is the largest real root of \(z^4-z^3-2z^2-z+1\).
The measures approach \(\theta\) from below.
The polynomial family is a classical Salem--Boyd construction, of the form inspected in the [Hironaka source comparison](../audits/literature/Hir06/Yin_U001.md#hir06-u001).
The work here chooses the exponents and proves the local conditions on the actual Salem polynomials.

<a id="choice"></a>
## A delay that avoids small residue fields

For an integer \(T\ge 3\) put \(K=6T^2+12\) and let \(d_0\) be the least common multiple of \(6\), the integers from \(1\) to \(T\), and
\[
                p^3,\quad p^j-1\quad (p\le T\text{ prime},\ 1\le j\le K).
\]
Take \(d=d_0\) or \(2d_0\) as specified in the [degree-sized return](#adaptive-return).
In particular \(d\ge 2^K-1\).
The elementary bound \(\sum_{p\le T}\log p=O(T)\) follows by dyadic summation since every prime between \(m\) and \(2m\), excluding \(m\), divides \(\binom{2m}{m}\le4^m\).
Bounding the lcm by the product now shows \(\log d=O(TK^2)=O(T^5)\), so \(T_d\le T\) for an absolute positive \(c\).

Write \(f=z^3-z-1,\ g=z^3f(1/z)=1-z^2-z^3,\ G=g/f,\ N=d+1\) and \(H=zf-g=(z+1)(z^3-1)\).
Consider the quotient
\[
 S(z)=\frac{z^N f(z)-g(z)}{H(z)}
     =1+(z^6-z^5-z)\sum_{j=0}^{d/6-1}z^{6j}.                         \tag{3}
\]
This identity follows by dividing \(zf(z)(z^d-1)\) by \(H\).
It gives the claimed coefficients, reciprocity, degree and constant.
The polynomials \(f,g\) are coprime in every characteristic because \(f+g=-z(z+1)\) and \(f(0)=f(-1)=-1\).

Fix \(p\le T\).
For any \(r\ne0\) of degree at most \(K\) over \(\mathbb F_p\), its order divides \(d\), and \(z^d-1\) vanishes at \(r\) to order at least \(p^3>4\).
Thus \(1+zf(z)(z^d-1)/H(z)\) takes the value one at \(r\), including at the zeros of \(H\).
The same value at zero follows from (3).
It follows that no root of \(\bar S\) has degree at most \(K\).
A repeated root of \(\bar S\) would satisfy \(z^d(zf)=g\) and the derivative equation.
Since \(p\mid d\), eliminating \(z^d\) gives
\[
                          (zf)'g-(zf)g'=0 .
\]
The factors \(zf,g\) have no common zero.
The last polynomial has degree at most six and constant \(-1\), so no root of \(\bar S\) can satisfy it.
Hence \(\bar S\) is squarefree and has no root in common with \(H\).
Its distinct root reductions imply unramifiedness of the splitting field since inertia fixes each root, as in the [finite-prime construction](Yin_C_G0162_v2.md#finite-pool).

<a id="salem"></a>
## The quotient is the full irreducible Salem polynomial

The cubic \(f\) has a single real root \(\theta>1\) by its negative discriminant, and its other two roots have modulus \(\theta^{-1/2}<1\) by their product.
On the unit circle \(|g|=|f|>0\).
By Rouché's theorem, \(z^Nf-\lambda g\) for \(0<\lambda<1\) has \(N+2\) roots in the disk and only one outside.
Letting \(\lambda\) increase to one shows that \(z^Nf-g\) has at most one root strictly outside, counted with multiplicity.
For every fixed \(s\in(1,\theta)\) its value at \(s\) is negative for large \(N\) and its value at \(\theta\) is \(-g(\theta)>0\).
Thus for all large \(T\) the unique exterior root is real, simple, lies below \(\theta\) and tends to \(\theta\).
The reciprocal quotient has precisely its inverse inside the disk.

Every root of unity \(\zeta\) of \(z^Nf-g\) has degree at most twelve.
Indeed one of \(\zeta^2,-\zeta^2,-\zeta\) is conjugate to \(\zeta\), according as its order is odd, twice an odd integer, or divisible by four.
In the middle case the exponent \(\operatorname{ord}(\zeta)/2+2\) is coprime to the order, and in the last case the same holds for \(\operatorname{ord}(\zeta)/2+1\).
Write the conjugate as \(\xi\zeta^h\) with \((\xi,h)=(1,2),(-1,2),(-1,1)\), respectively.
Since \(N\) is odd and no denominator vanishes, \(G(\xi\zeta^h)=\xi G(\zeta)^h\).
In each case clearing denominators gives a nonzero polynomial of degree at most \(6h\).
To see nonvanishing, \(G(z)=-1+z+O(z^2)\) at zero.
For \((1,2)\) and \((-1,1)\) the constant terms differ, and for \((-1,2)\) the linear terms differ.
If \(S\) had such a torsion root, it would have a monic factor of degree at most twelve whose reduction modulo two contradicts the residue-degree bound.
Every monic irreducible factor of \(S\) is a unit polynomial.
The factor containing the unique exterior root must contain the inverse root as well by the modulus of its constant term.
Any other factor would have only unit-circle roots and would be cyclotomic by Kronecker's theorem.
This proves irreducibility and the measure statement.

If two distinct conjugates had equal positive powers, transport one to the unique exterior root by a Galois automorphism.
Its power has strictly greater modulus than the powers of all other conjugates, a contradiction.
This gives degree preservation at all positive powers.

<a id="different-ratios"></a>
## No mixed collisions away from Frobenius ratios

Work in an algebraic closure of \(\mathbb F_p\) for \(p\le T\).
Every root \(x\) of \(\bar S\) satisfies \(x^N=G(x)\) and neither \(f(x)\) nor \(g(x)\) vanishes.
Take \(1\le a,b\le T\), \(a\ne b\), with neither ratio a power of \(p\).
A collision \(x^a=y^b\) of roots would also give \(G(x)^a=G(y)^b\).
The two bivariate polynomials
\[
 X^a-Y^b,\qquad g(X)^a f(Y)^b-f(X)^a g(Y)^b
\]
have no common curve in this characteristic.
To check this, let \(A=a/\gcd(a,b)\), \(B=b/\gcd(a,b)\).
Over an algebraic closure of \(\overline{\mathbb F}_p(X)\), set \(X=t^B\); every solution of \(Y^b=X^a\) has \(Y=\xi t^A\) with \(\xi^b=1\).
In \(G(t^B)^a\) the first nonconstant term has exponent \(B p^{v_p(a)}\), whereas in \(G(\xi t^A)^b\) this exponent is \(A p^{v_p(b)}\), by the expansion at zero and \(\xi\ne0\).
Equality of exponents would force the prime-to-\(p\) parts of \(a,b\) to agree, contrary to the ratio assumption.
Thus the resultant in \(Y\) is nonzero.
Its degree in \(X\) is at most \(6ab\), since each term uses at most \(3b\) coefficients of the first polynomial of \(X\)-degree at most \(a\) and at most \(b\) coefficients of the second of \(X\)-degree at most \(3a\).
Its vanishing at \(x\) would contradict the lower bound \(K\) on the residue degrees.
This proves the zero case of (1).

For \(1\le n\le T\), distinct roots of \(\bar S\) remain distinct after taking their \(n\)-th powers.
Indeed otherwise the roots would be \(x,\xi x\) with \(\xi\ne1,\ \xi^n=1\).
As \(n\mid d\), one has \(G(\xi x)=\xi G(x)\).
The equation after clearing denominators has degree at most six and is nonzero by the unequal constants at \(x=0\).
Its coefficients belong to \(\mathbb F_p(\xi)\), a field of degree at most \(n\).
Hence \(x\) would have degree at most \(6n\) over \(\mathbb F_p\).
The same residue-degree bound excludes roots of unity of order dividing \(n\) among the reductions, giving the cyclic resultant assertion.

<a id="unit-depth"></a>
## Exactly one unit of local valuation before amplification

Let \(q=p^h\le T,\ h\ge1\).
For any root \(\alpha\) of \(S\), there is a unique root \(\gamma\) with reduction \(\bar\alpha^q\).
Normalize the valuation in the unramified splitting field by \(v(p)=1\).
We show that \(v(\alpha^q-\gamma)=1\) and, for \(p=2\), also \(v(\alpha^q+\gamma)=1\).

For a sign \(\xi\), use \(\xi=1\) at every prime, and additionally \(\xi=-1\) at two.
Consider the fixed polynomial
\[
           D(z)=\xi\,g(z)^q f(\xi z^q)-f(z)^q g(\xi z^q).
\]
All its coefficients are divisible by \(p\), by Frobenius and the congruence \(\xi\equiv1\bmod p\).
The polynomial \(D/p\) has nonzero reduction modulo \(p\).
Indeed as an integral formal power series at zero we have \(G(z)^{q/p}\equiv G(z^{q/p})\bmod p\), and taking \(p\)-th powers gives congruence modulo \(p^2\).
The coefficient at exponent \(q/p\) in \(\xi G(z^{q/p})^p-G(\xi z^q)\) is \(\xi p(-1)^{p-1}\), which is nonzero modulo \(p^2\).
If all coefficients of \(D\) vanished modulo \(p^2\), division by the unit series \(f(z)^q f(\xi z^q)\) would contradict this coefficient.
Thus \(D/p\bmod p\) is nonzero of degree at most \(6q\).
It cannot vanish at \(\bar\alpha\), giving \(v(D(\alpha))=1\).
Since \(N\) is odd and \(\alpha^N=G(\alpha)\),
\[
   (\xi\alpha^q)^N f(\xi\alpha^q)-g(\xi\alpha^q)=D(\alpha)/f(\alpha)^q .
\]
The denominator is a unit.
Also \(\overline{\xi\alpha^q}=\bar\gamma\) is a root of \(\bar S\), so coprimality with \(\bar H\) makes \(H(\xi\alpha^q)\) a unit.
The left side factors as \(H(\xi\alpha^q)S(\xi\alpha^q)\).
In \(S(\xi\alpha^q)\) exactly the factor belonging to \(\gamma\) has positive valuation.
This proves both local claims, including at two.

If \(\max(a,b)=nq,\ \min(a,b)=n\), the injectivity of reduction followed by \(n\)-th powering on the reduced root set shows that exactly these \(d\) matched pairs contribute.
For their unit ratios \(w=\alpha^q/\gamma\), \(v(w^n-1)=1+v_p(n)\).
Indeed a prime-to-\(p\) exponent preserves positive valuation in \(w-1\), by the geometric sum.
At odd \(p\), the binomial expansion increases a positive integral valuation by exactly one at each \(p\)-th power.
At \(p=2\) the first squaring gives \(v(w^2-1)=v(w-1)+v(w+1)=2\), and subsequent squarings each add one.
Summing the valuations proves (1), without any power-degree change or multiplicity adjustment.
The mixed products themselves are nonzero in characteristic zero since equality of unequal positive powers would give unequal heights for a single pair of conjugates of equal positive height.

<a id="orbit-fraction"></a>
## The compatible fraction on each original orbit

Distinct reductions imply at most \(d\) compatible pairs in any one orbit.
For \(y\) equal to \(x\) or \(x^{-1}\) the congruence \(\bar x^p=\bar y\) would put \(\bar x\) in \(\mathbb F_{p^2}\), which was excluded.
On every other ordered orbit the two roots are multiplicatively independent.
Indeed the [dependence criterion](Yin_C_G0483_v1.md#independent-and-dependent-pairs) would give \(y=\zeta x^{\pm1}\) with \(\zeta\) torsion, and all-power degree preservation and reciprocity would then force \(y=x^{\pm1}\).
If that orbit has size \(sd\), its [rank-two height bound](Yin_C_G0483_v1.md#independent-and-dependent-pairs) gives \(m(S)\ge C_\delta d^{1/2-\delta}s^{-1/2-\delta}\) for every fixed \(0<\delta<1/2\).
Since \(m(S)<\log\theta\), choosing \(\delta\) sufficiently small gives \(s\gg_\epsilon d^{1-\epsilon}\).
Thus \(\beta\le1/s\ll_\epsilon d^{-1+\epsilon}\).
All \(d\) Frobenius edges lie in the \(d(d-2)\) ordered off-pair positions, giving the lower bound in (2) by weighted averaging.
This use of the rank-two input is restricted to its stated independent-pair scope.

<a id="adaptive-return"></a>
## The degree-sized return receives all its contributions from larger primes

Set \(k=d/6\).
At the \(d\)-th roots of unity outside \(z^6=1\), (3) equals one.
At a sixth root \(u\), its value is \(1+k(1-u-u^{-1})\).
Consequently
\[
 |\operatorname{Res}(S,z^d-1)|=(k-1)(1+3k)(1+2k)^2 .
\]
At \(z^d=-1\), the numerator of (3) is \(-W(z)\), where \(W=zf+g=z^4-z^3-2z^2-z+1\).
All four roots of \(H\), counted with multiplicity, have \(d\)-th power one.
Taking products at the roots of \(z^d+1\) therefore gives
\[
                 B_d=\frac1{16}\prod_{W(r)=0}|1+r^d| .
\]
Writing \(t=z+z^{-1}\) yields \(W/z^2=t^2-t-4\).
The positive trace \((1+\sqrt{17})/2>5/2\) gives a reciprocal real pair \(\lambda,\lambda^{-1}\) with \(\lambda>2\).
The other trace lies in \((-2,2)\) and gives a conjugate pair \(\gamma,\bar\gamma\) on the circle.
Choose \(d=d_0\) when \(|1+\gamma^{d_0}|\ge1\), and otherwise take \(d=2d_0\).
Indeed if \(\Re(\gamma^{d_0})<-1/2\), its square has real part greater than \(-1/2\).
Thus the unit-circle factors have product between one and four, and \(\log B_d=d\log\lambda+O(1)\).

For every \(p\le T\) a common root of \(\bar S\) and \(z^d+1\) would be a root of \(\bar W\) by the numerator identity.
Its degree would be at most four, contradicting the residue-degree bound also in characteristic two.
Hence all prime factors of \(B_d\) exceed \(T\).
Since \(|1+x_i^d|\le2\max(1,|x_i|)^d\), the integer \(B_d\) alone gives the certificate
\[
      \log M(S)\ \ge\ \frac1d\sum_{p>T}v_p(B_d)\log p-\log 2
                   =\log(\lambda/2)+O(1/d)>0
\]
for all sufficiently large members of the sequence.
This certificate uses a half-turn at exponent \(d\), equivalently a factor of the cyclic resultant at exponent \(2d\).
Its proof uses the particular numerator \(z^{d+1}f-g\).

## Assessment history

### Decision minimal-local-salem-products

| Field | Value |
| --- | --- |
| date | 2026-11-16T11:22 |
| status | open |
| reason | Submit the height-one Salem family and its local mixed resultant formulas for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Simultaneous local conditions](#statement) | Measures below the plastic number, degree preservation, growing prime and power window, exact valuations and orbital fractions. |
| argument | [Choice of delay](#choice) | Coefficients, finite-field avoidance, unramifiedness and window as a function of degree. |
| argument | [Exterior root and irreducibility](#salem) | Circle count, all torsion possibilities and their exclusion from the quotient. |
| argument | [Distinct powers](#different-ratios) | Fixed-resultant elimination at non-Frobenius ratios and injectivity on reduced roots. |
| argument | [Local depth](#unit-depth) | Nonzero cleared first Frobenius difference, dyadic sign, and every valuation in the mixed product. |
| argument | [Orbit density](#orbit-fraction) | Rank-two bound for off-pair conjugates and sharp density exponent. |
| argument | [Degree-sized return](#adaptive-return) | Exact full-turn and half-turn products, larger-prime support and a positive logarithmic measure certificate. |
| dependency | [Original-field orbit estimates](Yin_C_G0483_v1.md#independent-and-dependent-pairs) | Multiplicative dependence criterion and uniform fixed-rank height comparison. |
| support | [Classical family](../audits/literature/Hir06/Yin_U001.md#hir06-u001) | Established Salem--Boyd form and exterior-root mechanism at the recorded source scope. |


### Decision adaptive-returns-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T11:31 |
| status | proved |
| reason | Adopt the original Salem mixed valuations, sparse matching and degree-sized larger-prime return after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Simultaneous local conditions](#statement) | Measures below the plastic number, degree preservation, growing prime and power window, exact valuations and orbital fractions. |
| argument | [Choice of delay](#choice) | Coefficients, finite-field avoidance, unramifiedness and window as a function of degree. |
| argument | [Exterior root and irreducibility](#salem) | Circle count, all torsion possibilities and their exclusion from the quotient. |
| argument | [Distinct powers](#different-ratios) | Fixed-resultant elimination at non-Frobenius ratios and injectivity on reduced roots. |
| argument | [Local depth](#unit-depth) | Nonzero cleared first Frobenius difference, dyadic sign, and every valuation in the mixed product. |
| argument | [Orbit density](#orbit-fraction) | Rank-two bound for off-pair conjugates and sharp density exponent. |
| argument | [Degree-sized return](#adaptive-return) | Exact full-turn and half-turn products, larger-prime support and a positive logarithmic measure certificate. |
| dependency | [Original-field orbit estimates](Yin_C_G0483_v1.md#independent-and-dependent-pairs) | Multiplicative dependence criterion and uniform fixed-rank height comparison. |
| support | [Classical family](../audits/literature/Hir06/Yin_U001.md#hir06-u001) | Established Salem--Boyd form and exterior-root mechanism at the recorded source scope. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G0387_v4.md#salem-local-review) | Full proof, including the dyadic first displacement and the contrasting full-turn and half-turn norms. |

## Current assessment
[Selected decision](#decision-adaptive-returns-reviewed)
