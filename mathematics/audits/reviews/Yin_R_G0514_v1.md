---
author: Yin
---

# Complete normal-matrix gap, sparse excess and Jordan checks

Actual current inspection: 2026-10-21T03:50.
Human record author: Yin.
The constructor read the entire original L24/L25/L26, exact GBV15 and DS17-U001 interfaces, and all statements and complete proofs in C228/C229.
The current two whole findings are actual self-review, with the original mathematical development accounts available; no isolated review or newly rerun mathematics is claimed.
The three original author checks below retain their actual day-precision date2026-10-06 and their self-review relationship.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete normal theorem](#current-normal-obstruction-finding) | self-reviewed |
| [Complete sparse/Jordan theorem](#current-excess-jordan-finding) | self-reviewed |
| [Original normal author check](#original-normal-author-check) | self-reviewed |
| [Original sparse construction check](#original-excess-author-check) | self-reviewed |
| [Original Jordan check](#original-jordan-author-check) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete normal theorem](#current-normal-obstruction-finding) | [Statement](../../claims/Yin_C_G0228_v1.md#statement) | All ordinary normal unimodular integer matrices of arbitrary positive size, exact sharp log(phi) entropy, and all irreducible rational mixed-real/nonreal factors including any coprime neutral padding under rational positive metrics. |
| [Complete normal theorem](#current-normal-obstruction-finding) | [Argument](../../claims/Yin_C_G0228_v1.md#argument) | Full integer Frobenius trace and signwise exponential-merging proof, exact equality controls, rational cyclic-centralizer/adjoint action contradiction and reducing rational subspace argument under padding. |
| [Complete sparse/Jordan theorem](#current-excess-jordan-finding) | [Statement](../../claims/Yin_C_G0229_v1.md#statement) | Every positive size and every integral unimodular matrix, each fixed excess bound k0>=1, exact sparse neutral completion, all nonzero-eigenvalue Jordan blocks and all integral conjugates after arbitrary signed-permutation stabilizations; no entropy-only complexity bound or compression of the positive irreducible core. |
| [Complete sparse/Jordan theorem](#current-excess-jordan-finding) | [Argument](../../claims/Yin_C_G0229_v1.md#argument) | Complete signed matching inequality, active/inactive cycle removal, rational inverse and determinant-lemma polynomial, exact factorial/exponential term count and controls, full derivative Vandermonde multiplicity proof, optimized-excess escape and constant-entropy Jordan counterfamilies. |
| [Original normal author check](#original-normal-author-check) | [Original L24](../../ledger/Yin_L_G0024_v1.md#normal-integral-gap) | Full normal trace gap, sharp controls, cyclic rational adjoint contradiction and padding, with no general normalization theorem. |
| [Original sparse construction check](#original-excess-author-check) | [Original L25](../../ledger/Yin_L_G0025_v1.md#bounded-excess-gap) | Full signed matching/cycle/determinant construction, exact support bound, optimized excess and two controls, using DS17 at accepted scope. |
| [Original Jordan check](#original-jordan-author-check) | [Original L26](../../ledger/Yin_L_G0026_v1.md#jordan-complexity-obstruction) | Full nonzero-root multiplicity lemma, Jordan preservation and zero/fixed-positive entropy counterfamilies under the stated stabilizations. |

<a id="current-normal-obstruction-finding"></a>
## Actual entire normal theorem inspection

The exact registered statement and entire proof support proved.
Unimodularity gives sum u_i=0, normality supplies the Frobenius trace identity, strict AM–GM and its integer value give a positive surplus at least1, and both signwise merging inequalities have the displayed direction.
Solving M^2+M^-2>=3 gives the exact golden-ratio bound and both stated examples attain it with the required determinant.
For irreducible p, cyclicity makes every rational commuting adjoint a rational polynomial f(T).
Positive-metric normality forces f(lambda)=conjugate(lambda), while one real root forces p to divide f−t and hence forces every conjugate real, a contradiction.
Under coprime padding the rational p-primary subspace is invariant for U and its adjoint, has the correct dimension and restricted rational positive metric, so the same contradiction applies.
Irrational metrics and general nonnormal dynamics are outside this obstruction.

<a id="current-excess-jordan-finding"></a>
## Actual entire sparse and Jordan inspection

The exact registered statement and all construction/counterfamily arguments support proved.
The chosen determinant matching yields sum|E_ij|<=k, including matching and off-matching entries separately; at most2s active signed cycles suffice and every inactive cycle is an actual untouched direct summand.
The signed-cycle inverse has exactly one monomial numerator per entry, and the rank-s determinant lemma gives F=D^(s−1)chi_A0 as a nonzero monic integer polynomial.
The diagonal/off-diagonal counts give at most s!3^s2^{s(2s−1)}<=K(k) terms, so applying DS17 once at fixed K(k0) needs no monotonic eta choice.
All entropy is preserved because every removed cycle and D have zero Mahler measure.
The explicit golden-ratio and unipotent controls satisfy the claimed determinants and signs.
Nonzero-root multiplicity is at most support minus1 by the Euler-derivative Vandermonde system, and inactive cycles are semisimple, so every Jordan block of size at least2 forces the asserted k bound.
Well-ordering supplies each optimized minimum; the unchanged Jordan block under each permitted stabilization/conjugacy forces these minima to diverge even at entropy0 or fixed log(phi).
This cannot obstruct deletion of the neutral primary factor or prove a bound for an irreducible positive core; the threshold statement is conditional on an actual positive-entropy member.
No new source theorem, numerical or symbolic program, research execution or uniform Lehmer conclusion is used.

<a id="original-normal-author-check"></a>
## Original normal check

Original inspection date:2026-10-06.

Coordinator self-review only: checked both exponential merging inequalities, the determinant-one normalization, sharp controls, the cyclic centralizer, rationality and eigenvalue action of the adjoint, and the reducing-subspace argument for padding.
No subagent, independent review, source acquisition or computational experiment was performed.

<a id="original-excess-author-check"></a>
## Original sparse construction check

Original inspection date:2026-10-06.

Self-review checked the matching inequality, inactive-block decomposition, signed-cycle inverse, determinant lemma dimensions and sign, nonvanishing, term count, and exact entropy preservation.
DS17 remains an accepted external theorem at its recorded audit scope; its original dependencies were not newly verified.
No independent review or completion decision was obtained.

<a id="original-jordan-author-check"></a>
## Original Jordan check

Original inspection date:2026-10-06.

Self-review checked inactive-cycle semisimplicity, preservation of Jordan size under conjugacy and direct sum, the Vandermonde argument, and the distinction between neutral deletion and the narrower permitted stabilizations.
No independent review, general compression theorem, gap proof or Lehmer counterexample is claimed.
