---
author: Yin
---

# Independent review of the moving linear cut times an arbitrary square

Review performed for Yin at 2026-11-09T12:20 UTC on the current fixed candidate [C880 v3](../../claims/Yin_C_G0880_v3.md#statement), which had no assessment when inspected.
This is an initial whole-proof review by a separately assigned agent outside the proof's substantive development.
The review context supplied the fixed candidate, scope and execution conditions, but no development dialogue, mathematical summary, author explanation or previous verdict.
No previous project R finding was consulted before or after the initial judgment.
The candidate and necessary fixed proofs were read directly; their existing assessment sections and the accepted source units were visible as part of those materials, without treating those assessments as substitutes for the checks below.
The author corrected only the encoding of Baker--Wustholz's name while the review was in progress; the final candidate text was reread.

<a id="linear-cut-square-review"></a>
## Finding

No substantive mathematical gap was found in the complete statement or proof of C880 v3.
The argument proves one qualitative positive gap for the whole family, uniformly over every odd conductor, every integer cut parameter at least two, every integral square factor and every integral polynomial part satisfying the stated strict conditions.
It requires neither primality of the conductor nor a bound on the degree, height, support or nonzero resultant of the square factor.
The following verification includes the required resultant ceiling and its local supporting chain, with established external inputs accepted at the precise source-interface scope stated below.
This finding does not itself append a Claim assessment or complete the unrestricted Task.

## Arithmetic and quantifier checks

The recurrence starts with monic integral polynomials of consecutive degrees and preserves the absolute resultant one between consecutive terms.
Reduction modulo the monic grid polynomial therefore preserves integrality and gives the stated monic trace polynomial and monic reciprocal lift of degree \(2n+2\).
The full-grid derivative identity gives strictly positive \(D(b_j)/B'(b_j)\).
The rational cut \(-2+1/r\) is not an algebraic integer for \(r\ge2\), so it cannot equal a grid trace.
Together with nonvanishing of \(v\) on every grid point and the presence of both blocks, this verifies exactly the strict transition needed by the ceiling.
The assumed left endpoint sign is carried unchanged into that interface.

The resultant factors as \(r^n|B(c)|\,|\operatorname{Res}(B,v)|^2\), because the extra consecutive-polynomial resultant has absolute value one.
The latter factor is a positive integer, including for composite conductors with imprimitive nodes, so discarding it is a valid lower bound for completely unrestricted \(v\).
The quadratic defining \(\alpha\) is primitive, has negative discriminant, and has conjugate roots of modulus one and leading coefficient \(r\).
Its degree, height \((\log r)/2\) and nontorsion assertions follow with the stated normalizations.
Taking absolute values in the full odd-grid lift identity gives the exact denominator \(|\alpha-1|\le2\).

For \(q=\lceil\log r\rceil\), every choice of a \(q\)-th root \(\beta\) is nonzero and nontorsion, satisfies \(2\le[\mathbb Q(\beta):\mathbb Q]\le2q\), and has height \((\log r)/(2q)\le1/2\).
Thus the adopted height bound one, degree bound at least two and exponent bound at least two all hold when the exponent is \(pq\).
No application uses an unbounded-height extension of the source theorem.
The negative block puts the smallest trace below the cut, giving \(r(2-2\cos(\pi/p))<1\).
The sine inequality yields \(r<p^2/4\), so the degree growth from root extraction is only logarithmic in \(p\).
Consequently the stated error in \(\log\Delta/n\) is absolute and tends to zero uniformly in all allowed parameters.
It gives \(\liminf\Delta^{1/n}\ge2\) on every sequence with \(p\to\infty\), and divergence if \(r\to\infty\).
In the latter case the same inequality already forces \(p\to\infty\).

## Resultant-ceiling and supporting-chain checks

The odd-grid product, quadrature and midpoint normalization in L464 v5 were checked with \(p=2n+1\); none uses that \(p\) is prime.
The bounded first three trace sums follow from disjoint real-root matching and the bounds on the two unmatched trace roots, whether real or nonreal.
They bound the weighted positive mass and supply the compactness used in L464 v2.
The rational-limit argument uses bounded characteristic and integral Taylor coefficients, followed by the zero-free limit and integral-shift argument for the cyclotomic numerator and denominator.
The local deductions were checked; the Cantor input remains an accepted external theorem at its recorded interface.

The transfer of the C881 v1 moment, product-equality and integer-recurrence arguments to the odd grid preserves their factors of two and their integral moments.
The endpoint identity of L464 v5 forces the separator limit to be \(-2\); its limiting rational functions reduce to the displayed five \(H_x\)'s.
The sign and integrability restrictions, including cancellation at \(x=\pm2\), agree with this conclusion.
Only these portions of L464 v5 are needed here; its sampling example, finite-prefix exclusion and other later consequences were not separately certified by this finding.

In L464 v6, \(w=4-t^2\) is positive at every grid point and \(G=2(t-x)^2\) is integral.
Exact polynomial moments yield the claimed density \(f=(4-t^2)(t+2)(t-x)^2\), and \(\prod_jw(b_j)=p\) gives the displayed logarithmic product with the additional \(p\) factor.
The density satisfies \(0\le f\le256\), is positive almost everywhere and has integrable logarithm of mean zero for all five values of \(x\).
The regularized entropy estimate with \(\gamma=2^{-22}\) gives \(2\|f\|_\infty\sqrt\gamma\le1/4\).
This is strictly below the \(1/2\) weighted-error threshold of the integral recurrence.
Its first two moments vanish eventually, and the recurrence forces every residue difference to vanish.
The fixed-weight gap then contradicts a positive shrinking shell.
Excluding a subsequence with limiting norm rate at least the displayed threshold gives the strict limsup ceiling, not merely a non-strict bound.
No unit-resultant premise occurs in this proof.

The required fixed-weight argument in C880 v2 was checked through its weighted remainder, bounded sparse expression, height control and cancellation of a fixed noncyclotomic factor.
The sparse division argument uses a place where a nonzero nontorsion algebraic root has modulus different from one and separation of the fixed exponent blocks.
Primitivity gives integral quotient blocks, including for nonmonic irreducible factors.
The Fourier normalization and the fixed-support height/gap inputs match their retained source units.
The ancestor C880 v1's Fourier/coset and exact-measure identities were also checked at their used scope.
The comparison citation to Lenstra is not a premise of this local sparse-division proof and was not newly source-audited.

## Source inspection and conclusion limits

The reviewer directly extracted, rendered and visually read printed/PDF pages 29--30 of the retained Dimitrov arXiv:1611.04664v2 source.
Equation (9.1), its bounded logarithmic Weil-height premise, algebraic-degree notation, absolute implied constant and the hypothetical stronger estimate on page 30 agree with Dim16-U001 and the use in C880 v3.
This review accepts that reported Baker--Wustholz estimate for the stated guarded interface; it does not claim inspection of the original Baker--Wustholz proof or a numerical constant.
The work and edition identification is reused from the retained source record; no new title-page or whole-paper audit is asserted.
The Cantor, Sanders and Dobrowolski--Smyth statements, hypotheses and normalizations were read in their retained source units and matched to the local applications.
Their original proofs were not re-audited, and their recorded primary-source inspections are reused at those exact scopes.

Failure of a uniform positive gap would supply whole polynomials with \(0<m(P)\to0\) and, after restriction, \(M(P)\le2\).
An unbounded-conductor subsequence contradicts the lower norm rate two and the strictly smaller ceiling.
For bounded conductors, bounded degree and the coefficient estimate \(|a_j|\le2\binom dj\) leave finitely many whole integer polynomials, which excludes such a sequence even though the parameter descriptions may be infinite.
This proves the stated universal quantifier on \(\eta\).
The ancillary \(r=1\) observation correctly uses the already established fixed algebraic cut, and \(3\mid p\) indeed introduces a zero at the cut.

The result supplies no explicit numerical value of the gap.
For any probability law supported on this family, the event \(0<m(P)<\eta\) is empty; this is only the direct qualitative implication of the uniform gap, with no additional probability estimate or computable threshold.
It excludes arbitrarily small positive whole measures from this particular construction, while leaving general nonunit representatives, individual factors of other lifts and the unrestricted Lehmer Task unresolved.
No numerical experiment or finite enumeration is being used as evidence for its unrestricted parameter range.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-family finding](#linear-cut-square-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-family finding](#linear-cut-square-review) | [C880 v3 statement](../../claims/Yin_C_G0880_v3.md#statement) | Full odd-grid family, all parameter quantifiers, whole-measure gap and ancillary r=1 boundary. |
| [Whole-family finding](#linear-cut-square-review) | [C880 v3 inputs](../../claims/Yin_C_G0880_v3.md#inputs) | Exact ceiling and bounded-height external interface. |
| [Whole-family finding](#linear-cut-square-review) | [C880 v3 norm proof](../../claims/Yin_C_G0880_v3.md#norm-bound) | Resultant factorization, height reduction and conductor-uniform asymptotics. |
| [Whole-family finding](#linear-cut-square-review) | [C880 v3 completion](../../claims/Yin_C_G0880_v3.md#gap-proof) | Both conductor cases and the precise qualitative scope. |
| [Whole-family finding](#linear-cut-square-review) | [Odd-grid product](../../ledger/Yin_L_G0464_v5.md#odd-grid-product) | Integral lift, residue signs, full-grid quadrature and midpoint product. |
| [Whole-family finding](#linear-cut-square-review) | [Odd-grid profile transfer](../../ledger/Yin_L_G0464_v5.md#five-cuts-and-original-profiles) | Rational phase, exact moments and product threshold needed for the endpoint analysis. |
| [Whole-family finding](#linear-cut-square-review) | [Left endpoint profiles](../../ledger/Yin_L_G0464_v5.md#only-left-endpoint) | Endpoint forcing and the five H_x profiles used by the ceiling. |
| [Whole-family finding](#linear-cut-square-review) | [Resultant ceiling](../../ledger/Yin_L_G0464_v6.md#norm-ceiling) | Entire stated nonunit ceiling, including both exceptional-root types. |
| [Whole-family finding](#linear-cut-square-review) | [Ceiling product and density](../../ledger/Yin_L_G0464_v6.md#weighted-product) | Full normalization, exact moments and logarithmic density mean. |
| [Whole-family finding](#linear-cut-square-review) | [Ceiling recovery](../../ledger/Yin_L_G0464_v6.md#quantitative-recovery) | Strict numerical deficit, integer recovery and fixed-weight contradiction. |
| [Whole-family finding](#linear-cut-square-review) | [Dimitrov source unit](../literature/Dim16/Yin_U001.md#dim16-u001) | Only the adopted logarithmic-form interface, formula (9.1), directly read on source pp.29--30 with the stated proof limits. |
| [Whole-family finding](#linear-cut-square-review) | [Fixed-weight statement](../../claims/Yin_C_G0880_v2.md#statement) | Applicable fixed nonzero integral weight and finite weighted mass. |
| [Whole-family finding](#linear-cut-square-review) | [Sparse division](../../claims/Yin_C_G0880_v2.md#sparse-division) | Local qualitative block argument and integral division. |
| [Whole-family finding](#linear-cut-square-review) | [Fixed-weight completion](../../claims/Yin_C_G0880_v2.md#filtered-completion) | Weighted remainder, height bound, sparse cancellation and exact whole measure. |
| [Whole-family finding](#linear-cut-square-review) | [Fixed-cut consequence](../../claims/Yin_C_G0880_v2.md#moving-cut) | Applicability to the ancillary r=1 observation. |
| [Whole-family finding](#linear-cut-square-review) | [Fourier interface](../../claims/Yin_C_G0880_v1.md#fourier) | Integral moments and normalized signed-coset decomposition used by C880 v2. |
| [Whole-family finding](#linear-cut-square-review) | [Cleared identity](../../claims/Yin_C_G0880_v1.md#sparse-completion) | Generating-function and exact whole-measure identities. |
| [Whole-family finding](#linear-cut-square-review) | [Moment transfer](../../claims/Yin_C_G0881_v1.md#moments) | Integral limit moments and limiting positive density. |
| [Whole-family finding](#linear-cut-square-review) | [Product equality](../../claims/Yin_C_G0881_v1.md#saturation) | Omitted-node product bound and equality estimate reused on the odd grid. |
| [Whole-family finding](#linear-cut-square-review) | [Integer recovery](../../claims/Yin_C_G0881_v1.md#integer-recurrence) | Cyclotomic phase and exact recurrence threshold. |
| [Whole-family finding](#linear-cut-square-review) | [Rational sign restrictions](../../claims/Yin_C_G0881_v1.md#five-cuts) | Integrability, denominator degrees and sign restrictions used by the profile chain. |
| [Whole-family finding](#linear-cut-square-review) | [Trace matching](../../ledger/Yin_L_G0462_v2.md#central-sign-test) | Disjoint matching and three bounded trace sums, independently of the cut location. |
| [Whole-family finding](#linear-cut-square-review) | [Rational prefix](../../ledger/Yin_L_G0464_v2.md#rational-prefix) | Compactness and Cantor applicability. |
| [Whole-family finding](#linear-cut-square-review) | [Cyclotomic prefix](../../ledger/Yin_L_G0464_v2.md#cyclotomic-prefix) | Zero-free limit and the integral-shift argument. |
| [Whole-family finding](#linear-cut-square-review) | [Cantor source](../literature/Can63/Yin_U001.md#cantor-rationality) | Retained Theorem 1 statement and applicability; original proof not newly audited. |
| [Whole-family finding](#linear-cut-square-review) | [Sanders source](../literature/San20/Yin_U001.md#san20-u001) | Retained Theorem 1.1 and normalized Fourier convention only. |
| [Whole-family finding](#linear-cut-square-review) | [Sparse-gap source](../literature/DS17/Yin_U001.md#ds17-u001) | Retained Corollary 2, Theorem 2 and monomial guard; original foundations not newly audited. |
