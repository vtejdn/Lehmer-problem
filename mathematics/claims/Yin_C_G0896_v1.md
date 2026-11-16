---
author: Yin
---

# A degree obstruction for totally real factors producing the fourth zero-profile coefficient

<a id="statement"></a>
## A lower bound without a shrinking-measure hypothesis

Take the full odd grid \(p=2n+1\), \(b_j=2\cos(2\pi j/p)\), \(1\le j\le n\), and the [integral trace coordinates](Yin_C_G0881_v3.md#prefix-coordinates) \(h=\sum_{i=0}^{n-1}a_i E_i\), with residues \(\rho_j=(4-b_j^2)h(b_j)/p\).
Require strict positivity through one index \(1\le c<n\), strict negativity thereafter, and agreement with \(P_{*,0}=(1+z^2)^2/((1-z)(1-z^2))\) through the coefficient of \(z^4\).
For \(n\ge3\) this fixes \(a_0=2,a_1=0,a_2=4\).
Form \(G\) by multiplying once each primitive irreducible factor of \(h\) of odd multiplicity having a zero in \((-2,2)\), with positive leading coefficients.
If every root of this \(G\) is real, then along any such sequence with \(p\to\infty\),
\[
                         \frac{\deg G}{\sqrt{p/\log p}}\longrightarrow\infty.      \tag{1}
\]
Other factors of \(h\) can have arbitrary degree and multiplicity.
There is no restriction on the complete Mahler measure and no condition at the left endpoint.
In particular any fixed totally real product accounting for the sign change fails at all sufficiently large conductors even at this one fixed prefix.

<a id="size"></a>
## The root-pair estimate at comparable degrees

Write \(d=\deg G\), which is positive since the signs change.
Assume on an unbounded subsequence that \(d\le K\sqrt{p/\log p}\) for a fixed \(K\).
The [moment box](../computations/programs/Yin_J_G0155/versions/v2/readme.md#covering-box) uses just these coefficients and strict signs and gives \(\sum_j|\rho_j|\le p^2/4\) and \(|a_i|\le p^2(i+1)/4\).
Thus the circle norm of \(h^*=z^{\deg h}h(z+z^{-1})\) is \(O(p^5)\) by \(|E_i|\le i+1\).
For the angular midpoint \(a\) in the cut gap put \(X_j=(b_j-a)p\rho_j>0\).
Its full-grid mean on the \(n\) traces is \(-2ap/n\le4p/n\) by the first two moments.

Apply the [partial-product inequality](Yin_C_G0895_v1.md#partial-product) to \(G\mid h\).
For clarity the proof there uses the polynomial bound on \(\|h^*\|_\infty\) only to obtain \(\log^+\|(h/G)^*\|_\infty=O((d+1)\log p)\) and \(\log M(G^*)=O(\log p)\); the bound \(O(p^5)\) here suffices for both.
Deleting \(O(d+1)\) nodes as in that proof gives
\[
          \log M(G^*)\le n^{-1}\sum_{j\in J}\log X_j
                                  +O((d+1)^2\log(p)/p).
\]
The surviving fraction \(q=|J|/n\) tends to one.
Its log term is at most \(q\log((4p/n)/q)\) by concavity and positivity, so \(M(G^*)\le C_K\) for a constant independent of the conductors and polynomials on this subsequence.

Suppose first that \(d\to\infty\) along a further subsequence.
The [two endpoint products](../ledger/Yin_L_G0464_v30.md#external-real) show that the number of exterior real traces of \(G\) is \(O_K(d/\log d)\): the estimate there uses \(M(G^*)\le C_K\) and \(|G(2)G(-2)|\ge1\).
No root is \(2\) or \(-2\), by the choice of the factors.
By total reality the number \(I\) of interior roots therefore satisfies \(I\ge d-O_K(d/\log d)\).
The [paired-root determinant](../ledger/Yin_L_G0464_v30.md#close-pairs) needs only the strict signs and the actual measure of \(G^*\), with any positive integral leading coefficient.
It gives
\[
         (I-1)\log\big(p/(8\pi d)\big)\le d\log(2d)+(2d-1)\log C_K.
\]
Since \(d/(I-1)\le1+O_K(1/\log d)\), rearrangement gives \(\log p\le2\log d+O_K(1)\).
This forces \(d\gg_K\sqrt p\), contradicting the assumed bound on \(d\).

<a id="fixed"></a>
## A fixed factor and its unique interior conjugate

It remains to rule out bounded \(d\) on an unbounded subsequence.
The bound \(M(G^*)\le C_K\) bounds the integer coefficients of \(G^*\) in fixed degree by elementary symmetric functions, so a further subsequence has fixed \(G\).
The quotient \(h/G\) has constant sign at the nodes since any interior real zero in it has even multiplicity.
The roots of \(G\) are simple.
Each distinct interior root would eventually occupy its own open grid gap and force opposite signs at that gap.
Strictness rules out coincidence with a node, and the two extreme nodes approach the endpoints.
Thus \(G\) has exactly one interior root \(y\).
Every irreducible factor used to form \(G\) has an interior root, so \(G\) is irreducible.
Its root \(y\) lies in the sign-transition gap on this subsequence.

The fixed third moment is \(\sum b_j^2\rho_j=6\).
Consequently the positive quantities
\[
          Y_j=(2-b_j)(b_j-y)p\rho_j
\]
have average \((p/n)(-6-4y)\), forcing \(y<-3/2\).
We claim that
\[
               M(G^*)\le 2(-6-4y)=4-8u,\qquad u=2+y\in(0,1/2).        \tag{2}
\]
In the partial-product proof use the deletion set for \(G^*\), in particular removing nodes nearest in angle to both roots of \(z^2-yz+1\).
Equation (4) of [the binomial product calculation](Yin_C_G0895_v1.md#partial-product) gives mean log on the surviving nodes at least \(-o(1)\) for \(|b_j-y|\): the lift of \(t-y\) is monic of measure one and the same deletion set has bounded size.
This binomial calculation itself needs no integrality of \(y\).
On the full half grid the extra factors \(2-b_j\) and \(4-b_j^2\) each have product \(p\), and deleting finitely many terms loses only \(O(1)\) from their log products.
The integral cofactor still has full absolute product at least one and its omitted positive logarithms total \(O_G(\log p)\).
Combining the lower estimates gives \(n^{-1}\sum_{J}\log Y_j\ge \log M(G^*)-o(1)\).
The same concavity bound with the displayed mean of \(Y_j\) gives (2).

<a id="classification"></a>
## Excluding the remaining totally real factor

Let \(A\) be the positive integer leading coefficient of \(G\), and let \(r\) be the number of its exterior roots.
Write them as \(\pm(\lambda_i+\lambda_i^{-1})\) with \(\lambda_i>1\).
Then \(M(G^*)=A\prod_i\lambda_i\).
Set \(w=4-8u\), so \(1\le A\le w<4\).
If \(r=0\), the primitive polynomial \(G\) is linear, and \(Au\) is a positive integer.
Equation (2) gives \(A\le4-8/A\), which is impossible.

If \(r\ge2\), put \(x=\log(w/A)\).
By concavity of \(\log\sinh\) and \(\sum\log\lambda_i\le x\),
\[
 \prod_i(\lambda_i-\lambda_i^{-1})\le[2\sinh(x/r)]^r
                                        \le[2\sinh(x/2)]^2 .
\]
For the last inequality put \(S=2\sinh(x/2)\le3/2\).
Convexity of \(\sinh\) from zero gives \(2\sinh(x/r)\le2S/r\).
When \(S\le1\) its \(r\)-th power is at most \(S^2\); when \(S>1\) and \(r\ge3\) the base is at most one, and the case \(r=2\) is equality.
The nonzero integer \(G(2)G(-2)\) must therefore satisfy
\[
 1\le |G(2)G(-2)|=A^2u(4-u)\prod_i(\lambda_i-\lambda_i^{-1})^2
       \le u(4-u)(w-A)^4/w^2
       \le \frac{v(3-v)^4}{2(4-v)^2},\qquad v=8u\in(0,3].
\]
The last expression is less than one on this interval.
Its interior maximum occurs at the smaller root of \(12-17v+3v^2=0\), which lies between \(4/5\) and \(5/6\).
Substitution of the respective endpoint bounds yields a maximum at most \(219615/225625<1\).
This excludes \(r\ge2\).

For \(r=1\) write \(G=At^2+Bt+C\), so \(A\in\{1,2,3\}\).
Let \(s\) be its exterior root.
Since \(A\lambda_1\le4\), \(|s|\le4/A+A/4\).
The bounds on \(y,s,A\) imply \(|B|,|C|\le14\) by the two elementary symmetric functions.
The table lists all primitive irreducible candidates with \(y\in(-2,-3/2)\), \(|s|>2\), and \(A\lambda_1\le4\).
For each candidate the last number lies strictly between \(4-8(2+y)\) and \(A\lambda_1\), contradicting (2).

| \(A\) | \(B\) | \(C\) | separating number |
| --- | --- | --- | --- |
| 1 | -2 | -7 | 3 |
| 1 | -2 | -6 | 2 |
| 1 | -1 | -5 | \(47/20\) |
| 1 | -1 | -4 | 2 |
| 2 | -1 | -9 | \(7/2\) |
| 2 | -1 | -8 | \(5/2\) |
| 2 | -1 | -7 | 2 |

One can reproduce the finite comparison using rational arithmetic and square roots of positive integers only.
For each triple in the indicated integer box discard imprimitive triples and nonpositive or square discriminants.
Use both \(y=(-B\pm\sqrt{B^2-4AC})/(2A)\), \(s=-B/A-y\).
After the two root-interval tests, keep \(|s|\le4/A+A/4\), which is equivalent to \(A\lambda_1\le4\).
For a tabulated separator \(q\ge A\), the last strict upper comparison \(q<A\lambda_1\) is equivalent to \(|s|>q/A+A/q\).
The signs of these quadratic comparisons follow by squaring positive quantities.
This excludes the last fixed case and proves (1).

## Assessment history

### Decision totally-real-cut-degree

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:12 |
| status | open |
| reason | Record the fixed-prefix degree obstruction for totally real factors and its finite quadratic comparison for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed fourth coefficient](#statement) | Divergent square-root-scale degree ratio for totally real factors producing the signs, without a measure or endpoint bound. |
| argument | [Measure and pairs](#size) | Uniform cofactor and determinant bounds on the assumed degree scale. |
| argument | [A single conjugate](#fixed) | Fixed polynomial, third moment and the geometric mean at its interior root. |
| argument | [Totally real classification](#classification) | Integer endpoint products, degree reduction and the complete quadratic comparison. |
| dependency | [Partial products](Yin_C_G0895_v1.md#partial-product) | Finite binomial product and integral cofactor estimate. |
| dependency | [Exterior real roots](../ledger/Yin_L_G0464_v30.md#external-real) | Two endpoint evaluations with bounded Mahler measure. |
| dependency | [Close pairs](../ledger/Yin_L_G0464_v30.md#close-pairs) | Disjoint grid-angle pairs and Vandermonde row differences for an arbitrary integral leading coefficient. |


### Decision totally-real-cut-degree-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:16 |
| status | proved |
| reason | Adopt the fixed-prefix lower bound on the degree of the totally real factors carrying the sign change. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed fourth coefficient](#statement) | Divergent square-root-scale degree ratio for totally real factors producing the signs, without a measure or endpoint bound. |
| argument | [Measure and pairs](#size) | Uniform cofactor and determinant bounds on the assumed degree scale. |
| argument | [A single conjugate](#fixed) | Fixed polynomial, third moment and the geometric mean at its interior root. |
| argument | [Totally real classification](#classification) | Integer endpoint products, degree reduction and the complete quadratic comparison. |
| dependency | [Partial products](Yin_C_G0895_v1.md#partial-product) | Finite binomial product and integral cofactor estimate. |
| dependency | [Exterior real roots](../ledger/Yin_L_G0464_v30.md#external-real) | Two endpoint evaluations with bounded Mahler measure. |
| dependency | [Close pairs](../ledger/Yin_L_G0464_v30.md#close-pairs) | Disjoint grid-angle pairs and Vandermonde row differences for an arbitrary integral leading coefficient. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v69.md#totally-real-degree-review) | Independent proof review covering the bounded measure argument, determinant comparison, fixed sign gap and all seven exact quadratic candidates. |

## Current assessment
[Selected decision](#decision-totally-real-cut-degree-reviewed)
