---
author: Yin
---

# Independent review of polynomial weights in the trace-residue gap

<a id="weighted-lift-review"></a>
## Fixed weights and moving separators

At 2026-11-08T02:05 UTC, a separately assigned agent for Yin checked the whole [fixed-weight Claim v2](../../claims/Yin_C_G0880_v2.md#statement), including its sparse-division lemma and moving-separator consequence.
The reviewer had no part in developing the argument and received the fixed text and dependency locators without the proof-generation dialogue or an author's explanation.
The review used the cited v1 and ledger derivations and the external statements identified below.
The earlier review of v1 supplied no verdict on v2.

**Sparse division.**
Bounded integral coefficients and bounded support size permit a subsequence with one ordered coefficient list.
For its finitely many consecutive gaps, successive subsequences make each gap constant or divergent, leaving fixed coefficient blocks separated by distances tending to infinity.
A nonzero algebraic number of modulus one at every finite place is a unit, and Kronecker's theorem forces it to be torsion if all its complex conjugates also have modulus one.
At a place with modulus different from one, division by the extremal nonvanishing block's starting power leaves its fixed nonzero value as the limit, contradicting vanishing of the whole polynomial there.
Gauss's lemma gives integral quotients of all the fixed blocks even for a nonmonic primitive divisor.
Their translated sum has support bounded by the sum of the block support sizes and height bounded by the sum of their heights, also if translates overlap.
The argument can therefore be iterated a fixed number of times.
The checked hypothesis excludes zero and all roots of unity for either sign of a primitive irreducible divisor.
This restriction matters since \((1-z^j)/(1-z)\) has \(j\) terms.

**Weighted Fourier reduction and cancellation.**
Monic division gives the proper integral remainder of \(AC\) modulo \(B\), and its value at each simple root \(b_i\) equals \(A(b_i)C(b_i)\).
Expansion at infinity gives integral moments of the weighted residues, and the integral trace recurrence gives an integer-valued function on the common finite cyclic group.
Its Fourier algebra norm is bounded by \(2K\), including at doubled endpoint characters and when residues vanish.
Summing each pair of geometric series with the constant correction gives the stated rational expression for the proper remainder.
The normalization and uniform signed-coset bound agree with [Sanders, Theorem 1.1, pp. 1–2](https://ora.ox.ac.uk/objects/uuid%3A99e1bf6c-9b38-478d-aefb-2cef4d0d55c9/files/rxs55md820).

With \(s=\deg A\), the polynomial \(z^{s+1}J(z+z^{-1})\) has degrees between zero and \(2s+2\).
Each product of at most \(L\) binomials has at most \(2^L\) terms, and each geometric denominator in \(S\) cancels a factor of \(D\), including when denominators repeat.
The resulting \(U\) has bounded support, and its cross-multiplied expression is nonzero even when the proper remainder vanishes.
For support size \(h\ge2\), its height is at most \(2^{h-2}M(U)\), where \(M(U)\le2M(A^*)\) in the measure range at issue.
For \(h=1\) its height equals \(M(U)\).
These uses and the final positive logarithmic gap for fixed support agree with [Dobrowolski–Smyth, Corollary 2 and Theorem 2, p. 2](https://arxiv.org/pdf/1606.04376).

Since \(B^*\) is primitive, the integer content \(c\) of the weight divides the content of \(U\) by multiplicativity of content.
No nontorsion irreducible factor of \(A^*\) divides \(B^*\), so its full multiplicity divides \(U/c\).
The constant term of \(A^*\) excludes a zero root, and the signed content absorbs the unit in its factorization.
Sparse division applies to every retained nontorsion factor, leaving a nonzero integral polynomial of bounded support and measure \(M(U)/M(cG)=M(P)\).
This identity also handles a constant weight and an empty nontorsion product.
Above \(M(P)=2\) one can use \(\log 2\) as a lower bound, so the result applies on the entire class.
The divergence statement follows by ruling out a bounded subsequence separately for each fixed weight.

**Moving separator.**
In the two nonempty strict sign blocks, the \(n-2\) same-sign gaps and the left endpoint interval each supply a real trace zero with the asserted signs.
Matching to the right-hand pole of each interval leaves one unmatched pole and two roots counted with multiplicity.
For any trace root, its reciprocal lift has larger radius \(1\le r\le M(P)\), hence its trace has modulus at most \(r+r^{-1}\le5/2\) when \(M(P)\le2\).
For \(h=1,2,3\), the absolute value of the \(h\)-th difference of power sums is at most \(\operatorname{Var}_{[-2,2]}(t^h)+2^h+2(5/2)^h\), independently of the transition and degree.
The coefficients of \(t^{-1},t^{-2},t^{-3}\) in \(\log(Q/(tB))\) yield \(a=\Delta_1\), \(2k_0=a^2-\Delta_2\), and \(3l=a^3-3ak_0-\Delta_3\).
Thus \(l-c k_0=\sum_i|b_i-c||r_i|\) is uniformly bounded for every allowed separator.
The mean value inequality at an algebraic zero \(c_0\) of a fixed integral \(A\) adds at most \(\|A'\|_\infty|c-c_0|V\) to the bound for the weighted sum.
If that product \(|c-c_0|V\) had a bounded subsequence, the fixed-weight gap would exclude positive measures tending to zero along it.

The whole project deduction passes at these hypotheses, including the explicitly stated root condition in the sparse lemma and its application after extracting signed content.
The results of Sanders and Dobrowolski–Smyth were checked at statement and application level, with their original proofs and the classical Kronecker theorem accepted as external inputs.
Lenstra's paper serves as a comparison only.
The conclusion is qualitative for each fixed weight and concerns the total measure of the lift.
It gives no lower bound uniform over weights and settles neither slower convergence to an algebraic cut nor the unrestricted Lehmer problem.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Fixed weights and moving separators](#weighted-lift-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#weighted-lift-review) | [Fixed-weight statement](../../claims/Yin_C_G0880_v2.md#statement) | All fixed nonzero integral weights, finite budgets, and divergence for each fixed weight. |
| [Whole finding](#weighted-lift-review) | [Sparse division](../../claims/Yin_C_G0880_v2.md#sparse-division) | Height and support bounds, nonarchimedean places, exact root exclusions and multiplicities. |
| [Whole finding](#weighted-lift-review) | [Filtered completion](../../claims/Yin_C_G0880_v2.md#filtered-completion) | Integral remainder, sparse integer polynomial, exact divisibility and whole measure. |
| [Whole finding](#weighted-lift-review) | [Moving separator](../../claims/Yin_C_G0880_v2.md#moving-cut) | Signed interior configuration, absolute moment bounds, fixed algebraic zeros and escape. |
| [Whole finding](#weighted-lift-review) | [Trace inputs](../../claims/Yin_C_G0880_v1.md#statement) | The precise monic, simple-pole setup inherited by v2. |
| [Whole finding](#weighted-lift-review) | [Integral moments](../../claims/Yin_C_G0880_v1.md#fourier) | Integer-valued finite cyclic data and norm bound for the proper weighted remainder. |
| [Whole finding](#weighted-lift-review) | [Cleared generating function](../../claims/Yin_C_G0880_v1.md#sparse-completion) | Rational identity and its use after weighting. |
| [Whole finding](#weighted-lift-review) | [Trace matching](../../ledger/Yin_L_G0462_v2.md#central-sign-test) | Disjoint intervals, power sums through degree three and both moment bounds. |
| [Whole finding](#weighted-lift-review) | [Sanders source unit](../literature/San20/Yin_U001.md#san20-u001) | Fourier convention and signed-coset bound at fixed norm. |
| [Whole finding](#weighted-lift-review) | [Dobrowolski–Smyth source unit](../literature/DS17/Yin_U001.md#ds17-u001) | Fixed-support height bound for at least two terms and fixed-support positive gap. |
