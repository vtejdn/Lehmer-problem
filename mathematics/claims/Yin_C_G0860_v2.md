---
author: Yin
---
# Powered-polynomial and all-place mask precision: exact depths and paid costs

Human author Yin.
This is a project deduction strengthening the scalar precision comparison of [C860v1](Yin_C_G0860_v1.md#statement).
The original A--E conclusions and their complete proof remain at that fixed version, with their [actual proved assessment](Yin_C_G0860_v1.md#decision-whole-independent-review-2026-11-04).
They are exact dependencies of this version; the earlier assessment and independent review are not transferred to the new statements below.
The substantive change is an exact formula for every proper mask's all-place coefficient depth, a common denominator charging each rotation only once, and a uniform vanishing-certificate conclusion also covering full masks with arbitrarily growing rotation primes.

The radical-capacity-return agent developed this argument for Yin.
A second agent, mask-depth-check, made a bounded contributor check of the formal coefficient ring, integral power basis, denominator degrees and asymptotic return.
This checking was part of proof development and supplies no formal or independent review finding.
The complete v2 argument below has the [selected independent-review assessment](#decision-whole-independent-review-2026-11-04), with exact source and dependency limits retained there.

## Statement

Let \(P\in\mathbb Z[t]\) be monic, irreducible, reciprocal and noncyclotomic, of degree \(d\ge2\) and constant term one.
Let \(\alpha_1,\ldots,\alpha_d\) be all its conjugate roots, and assume every positive power of a root has degree \(d\).
Put
\[
 m=m(P)>0,\qquad H=\max_i|\alpha_i|,\qquad
 P_n(x)=\prod_{i=1}^d(1-\alpha_i^nx),\qquad U=P_2,\quad V=P_4.
\]
Reciprocity identifies \(P_n(x)\) with the monic powered polynomial \(Q_n(x)=\prod_i(x-\alpha_i^n)\) used in v1.
All quantities use the original \(d\) conjugates and total, rather than degree-normalized, logarithmic Mahler measure.
Define the maximal original coefficient depth
\[
 L=\max\{a\in\mathbb Z_{\ge0}:V-U\in2^a\mathbb Z[x]\},\qquad R=V/U.
\]
Then \(2\le L<\infty\).

For an odd prime \(q\), choose a primitive \(q\)-th root of unity \(\zeta\), put \(K=\mathbb Q(\zeta)\), and write \(A=\mathcal O_K\otimes_{\mathbb Z}\mathbb Z_2\).
For every nonempty mask \(I\subseteq\mathbb Z/q\mathbb Z\), set
\[
 D_I=\prod_{j\in I}U(\zeta^jx),\qquad
 N_I=\prod_{j\in I}V(\zeta^jx),\qquad
 \lambda(I)=\max\{a\in\mathbb Z_{\ge0}:N_I-D_I\in2^a\mathcal O_K[x]\}.
\]
This is the common coefficient depth at all places above two; it is finite for the stated original inputs.
Write
\[
 \log R(x)=\sum_{n\ge1}\ell_nx^n\in4x\mathbb Z_2[[x]],\qquad
 a_q=\min_{\substack{n\ge1\\q\nmid n}}v_2(\ell_n),\qquad
 b_q=\min_{\substack{n\ge1\\q\mid n}}v_2(\ell_n).
\]
Zero coefficients have valuation infinity, and a minimum over an identically zero group of coefficients is infinity.

**A. Exact all-place mask depths.**
One has \(\min(a_q,b_q)=L\), and every nonempty proper mask satisfies
\[
 \boxed{\lambda(I)=\min\{a_q,b_q+v_2(|I|)\}},                  \tag{M1}
\]
while the full mask satisfies
\[
 \boxed{\lambda(\mathbb Z/q\mathbb Z)=b_q}.                    \tag{M2}
\]
Consequently all proper masks of the same size have the same global depth, every odd-size proper mask has depth exactly \(L\), and every proper mask obeys
\[
                         \lambda(I)\le L+v_2(|I|).             \tag{M3}
\]
No assumption on the factorization of \(\Phi_q\) modulo two is imposed.

**B. The denominator charges each rotation once.**
Let \(O\) be the full orbit of \(I\) under the original group \(\operatorname{Gal}(K/\mathbb Q)\), acting by multiplication on rotation positions.
Put
\[
 S=\bigcup_{J\in O}J,\qquad Q(x)=\prod_{j\in S}U(\zeta^jx),
 \qquad b=d|S|.
\]
Then \(Q\in\mathbb Z[x]\), \(Q(0)=1\), and \(\deg Q=b\).
The maximal depth \(\lambda=\lambda(I)\) is common to all masks in \(O\).
If \(\lambda\ge3\), set \(a=\lambda-2\) and define
\[
 G_J=(N_J/D_J)^{1/2},\qquad
 f=\sum_{J\in O}G_J=\sum_{n\ge0}c_nx^n,\qquad
 \mathcal D_h=\det(c_{i+j+1})_{0\le i,j<h},
\]
where every square root has constant coefficient one.
The series \(f\) is integral and nonrational, and there are infinitely many nonzero \(\mathcal D_h\).
For every \(h\ge1\),
\[
 v_2(\mathcal D_h)\ge(a+1)h
                  +a\sum_{r\ge1}\max(h-rb,0).                 \tag{M7a}
\]
The valuation of zero is infinity.
The same elementary complex disk comparison as v1 gives
\[
 \log H\ge\eta(P,I,q),\qquad m\ge\eta(P,I,q),\qquad
 \eta(P,I,q)=\frac{(\lambda-2)\log2}{8b}.                       \tag{M7b}
\]
The parameter \(b\) replaces the larger product-denominator cost \(B=d|I||O|\).
This is an upper bound for ranks of the specified approximants, not an assertion that their ranks, or the best possible approximation ranks, equal this bound.

**C. Uniform vanishing of this certificate near one.**
Whenever \(\lambda\ge3\), the proper masks satisfy
\[
 \eta(P,I,q)\le\frac{(L+1/2)\log2}{8d},                        \tag{M8a}
\]
and the full mask satisfies
\[
 \eta(P,\mathbb Z/q\mathbb Z,q)
 \le\frac{\log(2d)}{8dq}+\frac{3m}{2d}
 \le\frac{\log(2d)}{24d}+\frac{3m}{2d}.                        \tag{M9a}
\]
For every sequence of the stated original inputs with \(m(P_j)\to0\), one has \(d_j\to\infty\), and the supremum of \(\eta(P_j,I,q)\) over all odd primes \(q\) and all nonempty masks of depth at least three tends to zero.
The supremum is defined to be zero if the indexing set is empty.
This includes primes \(q\) growing arbitrarily with \(j\), without assuming \(q\,m(P_j)\to0\).
The same conclusion holds for any supplied lower depth at least three and for the earlier, larger denominator cost \(B\).

This theorem limits the combination of a single global coefficient-product depth, these binomial truncations and the elementary Cauchy disk estimate.
It does not bound the actual Mahler measure from above, bound the true minimal approximation rank from below, or exclude cancellations only after trace combinations, distinct weights at individual finite places, or a different complex quadratic estimate.
No unrestricted positive Mahler gap or near-one input family is asserted.

## Exact dependencies and source scope

| Role | Fixed input and exact use |
| --- | --- |
| Dependency | [C860v1 A--E](Yin_C_G0860_v1.md#statement), with its [selected proof assessment](Yin_C_G0860_v1.md#decision-whole-independent-review-2026-11-04): retain the entire earlier result at its exact scope; use B for maximal original depth \(L=o(\log d)\), the [\(k=2\) budget](Yin_C_G0860_v1.md#multilevel-precision-budget) for the full mask on \(P_q\), and D's truncation valuation and elementary disk assembly with the new denominator bound proved below. |
| Dependency | [C858 all-place construction](Yin_C_G0858_v1.md#all-place-hankel-budget): original power-stable branch noncollision, private zeros, integrality and nonrationality of the identical rational orbit sum, the finite rank-to-elementary-divisor implication, and the shifted leading-Hankel nonvanishing criterion at its retained BNZ22 inspection scope; its [disk calculation](Yin_C_G0858_v1.md#cauchy-radius-cost) retains the unchanged radius and order of limits. |
| Dependency | [C219 discriminant escape](Yin_C_G0219_v1.md#discriminant-escape): on a hypothetical power-stable positive-measure vanishing sequence, \(D\to\infty\), hence \(d\to\infty\) because the integral discriminant has absolute value at least one. |
| Accepted source input | [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001): \(\mathcal O_{\mathbb Q(\zeta_q)}=\mathbb Z[\zeta_q]\), the degree \(q-1\), and the integral power basis; this uses its existing accepted statement scope and does not claim inspection of the original integer-ring proof. |
| Accepted source input | [Dimitrov, arXiv:1912.12545v1, Lemma 2.1, printed pp. 3--4](https://arxiv.org/pdf/1912.12545v1#page=3): \(P_4\equiv P_2\pmod4\), giving the exact \(L\ge2\) domain used for formal logarithm isometry. The statement and its displayed finite argument were read for this candidate, without a whole-paper proof review. |

All mathematical premises are fixed project materials or the exact accepted source statement above.
No rolling Draft, native computation or numerical estimate is a premise.
The original v1 argument and review remain available at their fixed locators, and this version does not change their assessed scope.

<a id="argument"></a>
## Complete argument

The source congruence gives \(R-1\in4x\mathbb Z[[x]]\).
The original \(V\ne U\) follows from the power-stable noncollision argument in C858, or directly from positive height of the conjugate roots.
For every nonempty mask, the same C858 private-zero argument shows \(N_I/D_I\ne1\), since a rotated squared root is not any rotated fourth-powered root and distinct rotated squared roots do not coincide.
Thus all the asserted maximal depths are finite.
The formal logarithm lies in \(4x\mathbb Z_2[[x]]\) by the coefficient argument immediately below.

<a id="proper-mask-depth"></a>
### Proof of the exact depth formulas

For a nonzero series in \(A[[x]]\), its depth is the largest integer \(a\) for which every coefficient belongs to \(2^aA\).
For any \(z\in2^a xA[[x]]\) with \(a\ge2\), the term \(z^r/r\) has depth at least \(ar-v_2(r)\).
For \(r\ge2\) this is at least \(a+1\), since \(v_2(r)\le r-1\).
Consequently
\[
                    \log(1+z)-z\in2^{a+1}A[[x]],              \tag{M4}
\]
and the formal logarithm preserves the exact depth of \(z\).
Each coefficient involves only finitely many terms, so no interchange of analytic limits is required.
The coefficient ring is essential: logarithm coefficients can have odd denominators, so they are not asserted to belong to \(\mathcal O_K\).
Multiplication by a series in \(1+xA[[x]]\), with integral inverse there, preserves coefficientwise divisibility and its exact depth.
Applying this to \(U\), \(D_I\), and their inverses identifies \(L\) with the depth of \(R-1\), and \(\lambda(I)\) with the depth of \(N_I/D_I-1\).
For the original algebraic-integral coefficients, membership in \(2^aA\) is equivalent to membership in \(2^a\mathcal O_K\).

Formal differentiation gives \((\log T)'=T'/T\) for \(T\in1+xK[[x]]\), so logarithms add under multiplication by comparing derivatives and constant coefficients.
It follows that
\[
 \log\!\left(\prod_{j\in I}R(\zeta^jx)\right)
   =\sum_{n\ge1}\ell_n c_I(n)x^n,\qquad
 c_I(n)=\sum_{j\in I}\zeta^{jn}.                              \tag{M5}
\]
For \(q\mid n\), one has \(c_I(n)=|I|\).
For \(q\nmid n\), multiplication by \(n\) permutes the residue classes, so \(c_I(n)\) is the value at \(\zeta\) of another nonempty proper binary mask polynomial of degree at most \(q-1\).
The accepted integral power basis \(\mathcal O_K=\mathbb Z[\zeta]\), with basis \(1,\zeta,\ldots,\zeta^{q-2}\), is recorded at its exact source and proof limits in [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001).
Thus reduction modulo two identifies \(A/2A\) with \(\mathbb F_2[z]/(\Phi_q(z))\).
The only binary polynomials of degree at most \(q-1\) divisible by \(\Phi_q=1+z+\cdots+z^{q-1}\) are zero and \(\Phi_q\) itself.
Both are excluded by a nonempty proper mask, proving
\[
                   c_I(n)\notin2A\qquad(q\nmid n).            \tag{M6}
\]
No irreducibility of \(\Phi_q\) modulo two, or condition on \(\operatorname{ord}_q(2)\), is used.
Multiplication by a scalar \(\ell_n\in\mathbb Q_2\) adds \(v_2(\ell_n)\) to the coefficient depth in \(A\).
Therefore (M5), (M6), and the logarithm isometry (M4) give (M1).
For the full mask, \(c_I(n)=0\) when \(q\nmid n\), and \(c_I(n)=q\), a two-adic unit, when \(q\mid n\), giving (M2).
Finally, (M3) follows from \(\min(a_q,b_q)=L\).

<a id="overlap-denominator"></a>
### Paying each denominator factor once

Let \(O\) be the full orbit of \(I\) under the original group \(\operatorname{Gal}(K/\mathbb Q)\) acting on rotation positions, exactly as in C858 and C860v1.
Set
\[
 S=\bigcup_{J\in O}J,\qquad
 Q(x)=\prod_{j\in S}U(\zeta^jx),\qquad b=d|S|.
\]
The set \(S\) is Galois invariant, so \(Q\in\mathbb Z[x]\), \(Q(0)=1\), and \(\deg Q=b\).
For prime \(q\), the possible nonempty unions are \(\{0\}\), \((\mathbb Z/q\mathbb Z)^\times\), and \(\mathbb Z/q\mathbb Z\).
Thus this is an actual denominator bound for the existing rational orbit sum, not a descent assertion for an arbitrary family of masks.

The global depths of the masks in \(O\) agree by Galois invariance of \(2^\lambda\mathcal O_K\).
Suppose their common actual depth is \(\lambda\ge3\), put \(a=\lambda-2\), and write \(N_J-D_J=2^\lambda A_J\).
The truncation of
\[
 G_J=\sum_{r\ge0}2^{\lambda r}\binom{1/2}{r}(A_J/D_J)^r
\]
through index \(t\) has denominator dividing \(Q^t\).
Indeed \(Q^t/D_J^r\) is a polynomial whenever \(r\le t\), and
\[
 \deg\left(A_J^r Q^t/D_J^r\right)
       \le r\deg D_J+tb-r\deg D_J=tb.
\]
The scalar coefficients are integers, and the orbit-summed numerator over \(Q^t\) is Galois invariant and algebraic integral, hence integral rational.
The valuation calculation and remainder bound in [C860v1](Yin_C_G0860_v1.md#statement) therefore give integral rational approximants of numerator and denominator degree at most
\[
 b_s=b\max\left(0,\left\lfloor\frac{s-2}{a}\right\rfloor\right)
\]
modulo \(2^s\).
Use the same trace \(f=\sum_{J\in O}G_J\) and shifted leading Hankel determinants \(\mathcal D_h\) as C860v1; their integrality and infinitely many nonzero indices are the unchanged [C858 interface](../claims/Yin_C_G0858_v1.md#all-place-hankel-budget).
The same elementary-divisor count gives
\[
 v_2(\mathcal D_h)\ge(a+1)h
                   +a\sum_{r\ge1}\max(h-rb,0).
\]
The elementary Cauchy disk comparison therefore applies with \(b\) replacing \(B=d|I||O|\).
Consequently the resulting scalar lower certificate is
\[
              \eta(P,I,q)=\frac{(\lambda-2)\log2}{8b},
              \qquad \log H(P)\ge\eta(P,I,q),\quad
                     m(P)\ge\eta(P,I,q).                     \tag{M7}
\]
This improves the paid upper rank bound by avoiding repeated factors; it makes no assertion that this rank bound is minimal.

<a id="uniform-mask-certificate-vanishing"></a>
### No positive uniform certificate from these depths and truncations

For a proper mask put \(k=|I|\).
Since \(|S|\ge k\) and \(v_2(k)/k\le1/2\), equations (M3) and (M7) imply
\[
 \eta(P,I,q)
 \le\frac{(L+v_2(k))\log2}{8dk}
 \le\frac{(L+1/2)\log2}{8d}.                                 \tag{M8}
\]
On any hypothetical power-stable near-one sequence, [C219's discriminant escape](../claims/Yin_C_G0219_v1.md#discriminant-escape) gives \(d\to\infty\), and [C860v1 B](Yin_C_G0860_v1.md#statement) gives \(L=o(\log d)\).
Thus (M8) tends to zero uniformly over every odd rotation prime and every proper mask.

For the full mask, the exact rotation identity gives
\[
 D_I(x)=P_{2q}(x^q),\qquad N_I(x)=P_{4q}(x^q),\qquad b=dq.
\]
Its depth is the original powered-polynomial depth for the polynomial \(P_q\), which remains irreducible, reciprocal and power-stable of degree \(d\), with total logarithmic measure exactly \(qm\).
Apply the \(k=2\) case of [C860v1's precision budget](Yin_C_G0860_v1.md#multilevel-precision-budget) to this same powered polynomial.
Its absolute discriminant is a positive integer, so the corresponding parameter \(D_q\le d\), and
\[
                 \lambda\log2\le\log(2d)+12qm.
\]
Keeping the original full-mask cost \(dq\) in (M7) gives
\[
 \eta(P,I,q)
 \le\frac{\log(2d)}{8dq}+\frac{3m}{2d}
 \le\frac{\log(2d)}{24d}+\frac{3m}{2d}\longrightarrow0.         \tag{M9}
\]
This argument does not assume \(qm\to0\), and therefore includes rotation primes growing arbitrarily along the original near-one sequence.

The bounds (M8)--(M9) hold for the maximal actual scalar depth, and hence also for any supplied lower depth used by the same certificate.
Depths below three do not provide the positive-depth certificate (M7).
The earlier larger denominator cost \(B\) gives a certificate no larger than (M7), so it has the same limitation.
This is a quantitative obstruction on the unchanged original input to repairing that elementary comparison by choosing deeper global coefficient-product masks, even after denominator overlaps are removed.
It leaves open a genuinely smaller actual approximation-rank cost, cancellations occurring only after trace combinations, a more refined comparison at individual finite places, and a different complex quadratic estimate.
No uniform lower bound for the original Mahler measure, near-one input construction, or resolution of G0001 follows.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T19:55 |
| status | proved |
| reason | Adopt all new exact mask-depth formulas, the denominator-union improvement and the uniform vanishing of this scalar disk certificate after independent R1076 v2. This covers growing rotation primes without assuming q times m tends to zero. The earlier v1 theorem and its evidence remain fixed, and the new result excludes neither weighted finite-place comparisons nor trace cancellations, better ranks or different complex estimates. G0001 remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact new statement](#statement) | Entire A--C, all M1--M9 formulas, original power-stable inputs, depth conventions, arbitrary odd primes, supremum and exclusions. |
| argument | [Complete argument](#argument) | Formal logarithm isometry, proper/full depths, overlap denominator, finite ranks, Hankel valuations, disk comparison and uniform asymptotic return. |
| dependency | [Original precision budget](Yin_C_G0860_v1.md#statement) | Accepted original A--E at their fixed assessment; maximal L=o(log d), k=2 on P_q, scaled-binomial valuations and unchanged disk interfaces. |
| dependency | [All-place construction](Yin_C_G0858_v1.md#all-place-hankel-budget) | Same original branch noncollision, private zeros, integral nonrational orbit sum, finite rank and shifted leading-Hankel interfaces, with retained source limits. |
| dependency | [Discriminant escape](Yin_C_G0219_v1.md#discriminant-escape) | On the stated power-stable positive-measure vanishing sequence, D and hence d tend to infinity. |
| support | [Integral cyclotomic power basis](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Exact accepted integer-ring and degree statements for prime q; no new inspection of the original integer-ring proof. |
| review | [Independent whole-v2 finding](../audits/reviews/Yin_R_G1076_v2.md#mask-depth-whole) | Whole new statement and proof, all exact dependency interfaces and the separately inspected Dimitrov v1 Lemma 2.1 finite argument, with source and Task limits. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
