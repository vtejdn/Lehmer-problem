---
author: Yin
---

# Closed-quantifier zero-gap direct-sum implication self-review

Recorded 2026-10-21T00:46 for human record author Yin.
The constructor supplied the explicit quantifier correction and read the complete v1/v2 argument and both consumed source units before this check.
The prior construction discussion and the isolated reviewer's reported findings were available.
This is self-review of the revised statement and unchanged proof, not independent certification of the constructor's correction.
The separate independent inspection of the revised statement and affected chain remains pending.

<a id="closed-quantifier-finding"></a>
## Complete corrected statement and argument finding

The v1 statement used m(f_n) without explicitly introducing the sequence f_n in its existential list.
The v2 statement now binds f_n in Z[t], every index n>=0, positive degrees d_n, positive leading and nonzero constant coefficients, rational automorphisms A_n and real e_n with the full strict inequalities.
These are exactly the objects actually constructed in the retained proof; no uniform Mahler gap, nonattaining flow or polynomial sequence is asserted without the zero-gap hypothesis.
The complete argument text is literally unchanged from v1.

The infimum hypothesis supplies a primitive integer polynomial with 0<m(f_n)<2^(-n-1) for every n.
Removing t factors and changing its sign preserve primitivity and Mahler measure and produce the stated nonzero constant and positive leading coefficient.
Positive measure excludes the only primitive constants, plus or minus one, so d_n is positive.
The companion matrix has nonzero determinant.
For its monic rational characteristic polynomial f_n/a_n, any denominator clearer s obeys a_n dividing s times each coefficient; an integer Bezout combination of the primitive coefficients proves a_n divides s.
Thus the GBV15 formula applies with exactly the original polynomial, all multiplicities and log(a_n), using total natural-log entropy without a degree normalization.
Neither irreducibility nor finite-set attainment on a block is required.

Coordinatewise inverses preserve finite support, so the constructed direct sum is one automorphism of the specified discrete group.
Finite products give the entropy of each finite prefix, and the invariant directed-union interface gives the supremum of those partial sums.
The first term is positive and strictly below one half; the remaining positive tail is at most one half, so the total is strictly between zero and one.
No infinite entropy is subtracted.

Every nonempty finite subset is contained in one fixed prefix, and all of its positive finite-sum trajectories remain there with identical cardinality.
Its local entropy is bounded by that prefix's sum, which is strictly below the whole sum because the next term is positive.
A finite collection of Z[t] generators lies in the same prefix and remains there under all forward iterates, so subgroup monotonicity gives the same strict bound for its entire flow-module.
This is module finite generation and requires no inverse-invariant submodule or finite generation of the underlying additive group.

The complete stated conditional conclusion follows with no remaining mathematical gap found in this self-check.
The original isolated finding must retain its actual v1 statement issue; this check does not turn it into a pass for v2.

## Exact source acceptance and limits

GBV15-U001 supplies the rational Yuzvinski formula on discrete rational vector groups, including the primitive leading coefficient and arbitrary rational endomorphisms.
Its precise statement/application evidence is reused; no fresh original p-adic proof inspection was performed.
DGB16-U001 supplies positive finite-sum trajectories and their Fekete limit, monotonicity, finite products and directed invariant unions.
The finite-support and product-trajectory mechanisms were checked directly here.
The source unit's unrelated torsion, purification and essential-quotient limitations supply no hidden premise for this proof.
No exact-spectrum theorem, Addition Theorem, positive-gap implication, prescribed entropy value or uniform bound has been adopted.
No research computation, source acquisition, Task/E change, formal verification or novelty claim was made.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Closed-quantifier whole finding](#closed-quantifier-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Closed-quantifier whole finding](#closed-quantifier-finding) | [Corrected statement](../../claims/Yin_C_G0207_v2.md#statement) | Complete zero-gap implication, all polynomial and automorphism sequences, every index and strict entropy inequality, finite-subset nonattainment and finite flow-module noncapture. |
| [Closed-quantifier whole finding](#closed-quantifier-finding) | [Complete argument](../../claims/Yin_C_G0207_v2.md#argument) | Entire retained primitive normalization, invertible rational companion, exact entropy normalization, finite prefixes, one direct-sum automorphism and every finite-support tail argument. |
| [Closed-quantifier whole finding](#closed-quantifier-finding) | [GBV15 interface](../literature/GBV15/Yin_U001.md#gbv15-u001) | Only the accepted rational entropy formula and its primitive leading-coefficient normalization; no new audit of the original proof or use of block attainment. |
| [Closed-quantifier whole finding](#closed-quantifier-finding) | [DGB16 interfaces](../literature/DGB16/Yin_U001.md#dgb16-u001) | Only finite trajectories, monotonicity, finite products, invariant directed unions and the exact Z[t] flow-module meaning at the retained source depth. |
