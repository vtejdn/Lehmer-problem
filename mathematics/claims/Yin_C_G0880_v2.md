---
author: Yin
---

# Fixed polynomial weights in the trace-residue Mahler gap

This project deduction extends the [bounded-variation argument](Yin_C_G0880_v1.md#fourier) and the [central sign calculation](../ledger/Yin_L_G0462_v2.md#central-sign-test).

<a id="statement"></a>
## A fixed integral weight

Use the monic integral data \(B,Q=(t-a)B+C,P(z)=z^{n+1}Q(z+z^{-1})\) and the real residues \(r_i=C(b_i)/B'(b_i)\) of [v1](Yin_C_G0880_v1.md#statement), including simple trace poles in \([-2,2]\).
For every fixed nonzero \(A\in\mathbb Z[t]\) and \(K<\infty\), a uniform positive gap holds for the positive total \(m(P)\) on
\[
                         \sum_i|A(b_i)r_i|\le K .
\]
The constants may depend on the weight and budget.
In particular every hypothetical sequence of these lifts with \(0<m(P)\to0\) has \(\sum_i|A(b_i)r_i|\to\infty\) for *every* fixed nonzero integral weight.

<a id="sparse-division"></a>
## Dividing bounded sparse polynomials by a fixed noncyclotomic factor

Suppose a sequence of nonzero integer polynomials \(U_j\) has bounded support size and bounded coefficient magnitudes, and a fixed primitive irreducible \(G\in\mathbb Z[z]\) divides them all.
Suppose \(G\) has positive degree and none of its roots is zero or a root of unity.
The quotients \(U_j/G\) also have bounded support size and coefficient magnitudes, with bounds depending on the original bounds and \(G\).
Here is a qualitative gap argument; compare [Lenstra's lacunary factor method](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1999a/art.pdf).

Take a root \(\beta\ne0\) of \(G\).
Some absolute value of its number field has \(|\beta|\ne1\): if all finite values were one it would be an algebraic unit, and if also all complex conjugates had modulus one then Kronecker's theorem would make it torsion.
Suppose a quotient bound fails and pass to a sequence with that quantity tending to infinity.
After taking subsequences the ordered coefficient list is fixed and each consecutive exponent difference is constant or tends to infinity.
Hence \(U_j=\sum_h z^{e_{j,h}}D_h(z)\), where each block \(D_h\) is fixed and differences between successive block starts tend to infinity.
If some \(D_h(\beta)\ne0\), take the last such block when \(|\beta|>1\), or the first when \(|\beta|<1\).
After dividing \(U_j(\beta)=0\) by its power \(\beta^{e_{j,h}}\), every other nonzero summand tends to zero at this place.
This contradicts \(D_h(\beta)\ne0\).
Every block is therefore divisible by \(G\) in \(\mathbb Z[z]\) by primitivity, and the quotients are sums of translates of finitely many fixed quotient blocks, a contradiction.
Repeating this lemma handles a fixed list of irreducible factors with multiplicity.

<a id="filtered-completion"></a>
## Clearing an arbitrary weight

Divide \(A C\) by the monic \(B\) and let \(C_A\) denote the integral remainder.
Then \(C_A/B\) has residues \(A(b_i)r_i\), and \(A Q/B=J+C_A/B\) with \(J\in\mathbb Z[t]\) of degree at most \(s+1\), \(s=\deg A\).
Use the [integer Fourier moments and Sanders decomposition](Yin_C_G0880_v1.md#fourier) for \(C_A/B\).
It gives \(C_A/B=z(S-k)/(1-z^2)\) at \(t=z+z^{-1}\), with \(k=\sum A(b_i)r_i\) integral and \(S\) a bounded sum of signed terms \(z^u/(1-z^v)\).
Let \(D\) be the product of these denominators and set \(A^*=z^s A(z+z^{-1})\), \(B^*=z^nB(z+z^{-1})\).
Multiplication of the displayed division identity by \(z^{s+1}(1-z^2)D\) gives
\[
         U=(1-z^2)D A^* P/B^*
           = z^{s+1}(1-z^2)D J(z+z^{-1})+z^{s+2}D(S-k).
\]
Thus \(U\) is a nonzero integer polynomial of bounded support size even if the coefficients of \(J\) vary.
Its measure satisfies \(M(U)=M(A^*)M(P)\), since \(D,1-z^2,B^*\) have measure one.
It suffices to treat \(M(P)\le2\).
The fixed-support height bound of [Dobrowolski–Smyth, Corollary 2](../audits/literature/DS17/Yin_U001.md#ds17-u001) then bounds all coefficients of \(U\), also for a single monomial by its measure.

Write \(A^*=c G H\) with \(c\) its signed content, \(G\) the product of primitive noncyclotomic irreducibles, and \(H\) a product of monic cyclotomics (empty products allowed).
There is no zero root of \(A^*\), since its constant coefficient is the leading coefficient of \(A\).
Since \(B^*\) is monic and cyclotomic, the cross-multiplied identity implies \(cG\mid U\) in \(\mathbb Z[z]\): compare contents and use coprimality of the primitive noncyclotomic factors with \(B^*\).
The sparse division lemma shows that \(U/(cG)\) has bounded support and its measure is exactly \(M(P)\).
The [fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) now applies to this whole quotient.

<a id="moving-cut"></a>
## A necessary escape condition on a moving sign transition

Suppose the poles are strictly interior, with one transition from negative to positive residues in increasing order, and \(Q(-2)/B(-2)<0\).
Let \(c\in[-2,2]\) be any separator within the transition gap, so \((b_i-c)r_i\ge0\).
Write \(V=\sum|r_i|\).
The [disjoint matching and three Newton sums](../ledger/Yin_L_G0462_v2.md#central-sign-test) apply independently of the transition's location: there is a root in each same-sign gap and one between \(-2\) and the first pole.
If \(M(P)\le2\), the two remaining trace roots have magnitude at most \(5/2\), and the matching bounds \(k_0=\sum r_i\) and \(l=\sum b_i r_i\) absolutely.
In particular \(\sum |b_i-c||r_i|=l-c k_0=O(1)\).
For each fixed real algebraic \(c_0\in[-2,2]\) choose a nonzero \(A\in\mathbb Z[t]\) vanishing at \(c_0\).
Boundedness of \(A'\) on the trace interval gives
\[
       \sum |A(b_i)r_i|\ \le\ \|A'\|_\infty \bigl(O(1)+|c-c_0|V\bigr).
\]
Consequently on a sequence of such candidates with \(0<m(P)\to0\), one must have \(|c-c_0|V\to\infty\) for each fixed algebraic \(c_0\) and every choice of the separators.
This excludes every fixed algebraic cut, including nonintegral rationals and real algebraic points with nontorsion lifts.
Convergence to such a cut at a slower rate, a moving cut with transcendental limit and the unrestricted Lehmer problem remain open.

## Assessment history

### Decision fixed-weight-gap

| Field | Value |
| --- | --- |
| date | 2026-11-08T02:13 |
| status | proved |
| reason | Independent whole-proof review checked the fixed-weight argument, exact sparse-factor cancellation and the necessary escape rate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole-lift gap](#statement) | Any fixed nonzero integral weight at the simple trace poles, with its own finite budget. |
| argument | [Fixed-factor division](#sparse-division) | Bounded sparse quotients when the fixed divisor has no zero or torsion root. |
| argument | [Filtered completion](#filtered-completion) | Exact recovery of the original whole measure and the fixed-support bound. |
| argument | [Single moving transition](#moving-cut) | A fixed algebraic separator and the necessary escape condition for every convergent cut. |
| dependency | [Integral Fourier moments](Yin_C_G0880_v1.md#fourier) | The cyclic coset decomposition applied to the proper weighted remainder. |
| dependency | [Fixed-support bounds](../audits/literature/DS17/Yin_U001.md#ds17-u001) | Corollary 2 controls the coefficients and Theorem 2 isolates measure one. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G1105_v2.md#weighted-lift-review) | All fixed-weight assertions and the sign-transition consequence. |

## Current assessment

[Selected decision](#decision-fixed-weight-gap)
