---
author: Yin
---

# Review of the Mahler gap for lifts with bounded trace residues

<a id="whole-lift-review"></a>
## Finding on both whole-lift assertions

Review act at 2026-11-07T18:03 UTC for Yin.
A reviewer outside proof development independently inspected the fixed statement and all three proof sections of G0880 v1.
The inputs were the fixed Claim, the cited DS17 source unit and the two primary theorem statements.
The reviewer received no development dialogue, draft notes, prior review opinions or author explanation.

Both assertions follow with the stated whole-polynomial scope.
For the signed assertion, the factorization \(B^*=\prod_i(z^2-b_i z+1)\) proves that Kronecker's theorem applies even for reducible \(B\) and repeated lift roots at \(b_i=\pm2\).
Inverting \(t^{-n}B(t)\) in \(\mathbb Z[[t^{-1}]]\) gives integrality of every coefficient in the expansion of \(C/B\) at infinity.
Partial fractions identify these coefficients as the moments of the residues, and the integral recurrence for \(D_j\) then gives integer values of \(H\) on the entire cyclic group.
Under Haar probability normalization, the Fourier coefficients are precisely the grouped character weights in the expansion of \(H\), so the triangle inequality gives the bound \(2\sum_i|r_i|\), also at a character equal to its inverse.
Sanders' integer coset weights yield at most their \(\ell^1\) sum in signed repetitions, a bound depending only on \(\max(1,2K)\).
This checks both the normalization and the uniformity in \(N\) against the author's definitions and Theorem 1.1 on pp. 1-2. [Sanders, arXiv:1610.07092v5](https://arxiv.org/pdf/1610.07092)

The sum of the two geometric series for a trace pair has constant term two, so subtracting one per pair produces the numerator \(1-z^2\) and gives the subtraction of \(k\) from \(S\).
In \(P/B^*=1-az+z^2+zC/B\), substitution therefore gives the stated polynomial identity after multiplication by \((1-z^2)D\).
For \(L>0\) its three summands have at most \(6\cdot2^L\), \(L2^{L-1}\) and \(2^L\) terms, respectively, using one product factor per repetition even when two moduli coincide.
The bound \((7+L)2^L\) also holds for the empty product, and the constant coefficient is one in every case.
Zeros of \(C\) at some poles, \(C=0\), and common factors of the cross-multiplied identity cause no difficulty for additivity of the total logarithmic measure.
With the signed-coset bound fixed by \(K\), the resulting nonzero integral polynomial satisfies the hypotheses of Dobrowolski and Smyth's Theorem 2, with the normalization in equation (3) on p. 2. [Dobrowolski and Smyth, arXiv:1606.04376v2](https://arxiv.org/pdf/1606.04376)

For the positive assertion, monicity bounds the larger radius \(\rho\) of each reciprocal root pair by \(M(P)\), including repeated roots.
For \(1\le\rho\le2\), the triangle inequality gives \(|q|\le\rho+\rho^{-1}\le5/2\) even for nonreal \(q\).
Strict positivity gives opposite one-sided limits on each open pole interval, hence \(n-1\) distinct zeros can be removed one at a time with multiplicity.
The first two Newton identities give the displayed trace sums for all remaining pairs \(u,v\), whether complex, real or repeated.
Pairing consecutive endpoints gives \(b_1\le\sum b_i-\sum c_i\le b_n\).
Pairing \(c_i\) with \(b_i\) and integrating \(|2t|\) over the disjoint intervals gives the bound \(8+4=12\) for the square sums.
Both estimates include \(n=1\), when the chosen zeros form an empty family.
Thus \(|a|\le7\) and \(0<\sum|r_i|=k\le147/4<37\) for \(M(P)\le2\).
The minimum of the signed-class gap at \(K=37\) and \(\log 2\) works over the full strictly positive class.

The source checks cover the external statements and their use here.
The original proofs of the external theorems were accepted as established inputs.
The conclusion concerns a qualitative gap in the total logarithmic measure of the full lift, with neither a numerical gap computed nor a bound for each positive-measure factor inferred.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-lift finding](#whole-lift-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-lift finding](#whole-lift-review) | [Statement](../../claims/Yin_C_G0880_v1.md#statement) | Both assertions and the whole-lift and factor scopes. |
| [Whole-lift finding](#whole-lift-review) | [Integral Fourier coefficients](../../claims/Yin_C_G0880_v1.md#fourier) | Integrality, Fourier norm, endpoint multiplicity and Sanders' theorem. |
| [Whole-lift finding](#whole-lift-review) | [Sparse completion](../../claims/Yin_C_G0880_v1.md#sparse-completion) | Coset summation, clearing, support count, exact measure equality and the fixed-support gap. |
| [Whole-lift finding](#whole-lift-review) | [Positive residues](../../claims/Yin_C_G0880_v1.md#positive-residues) | Root radius bound, gap zeros, trace identities and reduction to bounded mass. |
| [Whole-lift finding](#whole-lift-review) | [Fixed-support theorem](../literature/DS17/Yin_U001.md#ds17-u001) | The univariate whole-polynomial consequence of Theorem 2 and its normalization. |
