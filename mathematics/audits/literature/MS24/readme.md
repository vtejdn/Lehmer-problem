<a id="yin-source-edition"></a>
# MS24: Determinants and Capacity

Audit date: 2026-09-12.
The sole bibliographic record identifies the user-supplied [MS24 PDF](../../../literature/pdf/MS24.pdf).
The reviewed artifact is arXiv:2406.15922v1, with margin date 22 June 2024 and title-page date 25 June 2024.
Printed and one-based PDF page numbers agree throughout its 19 pages.

The entire source was read.
The local proof chains for the determinant formula and the integer-capacity estimate were reconstructed, with the explicit corrections and external interfaces below.
The source's Section 5 questions remain questions; this review does not determine their present research status.
Numerical algorithms from other papers and subsequent developments are outside this audit.

## MS24-Focused Dependency Review

The user subsequently designated MS24 as the principal source and research input for this study.
The [main-proof dependency map](../../../ledger/Yin_L_F0003_v1.md#ms24-dependency-chain) is the recommended starting point: it separates the determinant formula, the integer-capacity theorem, and their combined corollary, and identifies the actual upstream premise at each arrow.

The retained supplements give [finite-dimensional scaling](Yin_U006.md#ms24-scaling-dependency-review), [bounded determinant foundations](../FK52/Yin_U001.md#fk52-u001), [hermitization and logarithmic limits](Yin_U005.md#retained-analytic-proof-interfaces), and [integer/Haar inputs](Yin_U004.md#complete-retained-algebra-and-haar-interfaces).
They retain the complete selected source-interface reconstructions; the original formal second checks and their unknown development context are recorded in [R_F8](../../reviews/Yin_R_F0008_v2.md#review-relationships) and R_F0125.
The Haar/full-pencil step retains the precisely identified MSY23 and Cohn algebra interfaces, with their existing proof-review boundaries.

The reconstructed main proofs have no unresolved dependency on the questioned Gur04 auxiliary claims or GGOW20 numerical constants and quantitative continuity details.
This assessment concerns the two MS24 proof chains under the explicit foundations; it does not certify every original proof in the upstream bibliography.
No new project Claim or goal is created.

## Affine Follow-Up

The user-requested offline exploration on 2026-09-12 produced [Yin_C_F0002](../../../claims/Yin_C_F0002_v1.md#yin_c_f0002), a project deduction extending the determinant identity to arbitrary deterministic coefficient matrices through a uniquely specified finite-dimensional Dyson equation.
The functional equals ordinary capacity at zero drift.
A scalar counterexample shows that the original covariance and the deterministic coefficient alone are insufficient for general complex coefficients.
A comparably simple global optimization representation remains unresolved.

The [additional MS17 source interfaces](../MS17/Yin_U001.md#offline-affine-extension-additional-source-interfaces), [main contributor review](../../reviews/Yin_R_F0001_v1.md#scope-of-the-passed-review) and [monotonicity author check](../../reviews/Yin_R_F0006_v1.md#monotonicity-self-review) record the exact evidence and distinct self-review scopes.
This follow-up changes neither the statement of MS24 nor the existing centered proof's audit scope, and it makes no literature-priority claim.

## Reusable Units

| Unit | Source coverage | Reusable input and review depth |
| --- | --- | --- |
| [MS24-U001](Yin_U001.md#ms24-u001) | Definitions 1.1, 2.1, 2.5; Propositions 2.3-2.10; pp. 3-9 | Exact trace, determinant, positivity, capacity and scaling conventions; elementary determinant consequences and normalization repairs checked; Gur04 and determinant foundations explicitly imported. |
| [MS24-U002](Yin_U002.md#ms24-u002) | Propositions 3.2-3.3, Lemma 3.5, Remark 3.6; pp. 10-12 | Complete local pairing induction, norm control, hermitization and corrected arbitrary scaling formulas. |
| [MS24-U003](Yin_U003.md#ms24-u003) | Theorem 1.2, Remark 3.1, Proposition 3.4, Sections 3.2-3.4; pp. 3, 9, 11-14 | Exact and approximate scaling plus both determinant inequalities; all local steps reconstructed with the positive-operator repair. |
| [MS24-U004](Yin_U004.md#ms24-u004) | Theorems 1.3/4.1 and Corollary 1.4; pp. 4, 15-16 | Integer Haar model and determinant/trace argument; complete local proof with the free-group determinant input and its normalization explicit. |
| [MS24-U005](Yin_U005.md#ms24-u005) | External references used in Sections 2-4; introduction; Section 5, pp. 16-17 | Exact accepted interfaces, source-version distinctions, complete retained hermitization/logarithmic arguments, stated open questions, and project-use limits. |
| [MS24-U006](Yin_U006.md#ms24-u006) | MS24 pp.8-16; Gur04 pp.462-465; GGOW20 pp.242,257-258 | Complete finite-dimensional scaling reconstructions with exact original source-reading and coordinating-check boundaries. |

## Findings and Corrections

These are local reading findings, not an author-issued erratum.

| Finding | Source passage | Correction and effect |
| --- | --- | --- |
| F01 | p. 4 twice attributes the explicit determinant formula to Theorem 1.3 | The formula is Theorem 1.2; Theorem 1.3 is the integer-capacity lower bound. |
| F02 | Proposition 2.4, p. 7, prints `sup_n ||T_n|| <= infinity` | Use a finite uniform norm bound.
The actual applications supply it. The reconstructed ordinary-determinant argument is in U001. |
| F03 | p. 8, sentence immediately after Proposition 2.8 | The normalized map is automatically unital; its adjoint is not automatically unital for an arbitrary positive matrix. U001 gives the correct formula and a counterexample. Capacity minimizers and the quantified approximation input supply the missing adjoint normalization in the proof. |
| F04 | Definition 2.5(v), Remark 2.6(iii), and Proposition 2.8, pp. 7-8 | For matrix size one the printed indecomposability test is vacuous, including the zero map. Require positive capacity when using the scaling conclusion, or handle this scalar zero case separately. The main theorem already separates zero capacity. |
| F05 | Lemma 3.5(i), pp. 11-12, compared with the scaling definition on p. 8 | For coefficients `c1 ai c2` the covariance is `eta_{c1,c2*}`, with the corresponding adjoint correction. All scaling factors actually used later are positive matrices, so the main proof is unaffected. U002 records the full formulas. |
| F06 | Equation (3.7), p. 14, invokes the positive-operator Proposition 2.4 on selfadjoint hermitizations | Apply it to their squares and to the square of a standard semicircular element, then take square roots. |
| F07 | Section 4, p. 16, says both determinant factors are “bigger than 1” | The proof only has and only needs “at least 1”; the determinant of the normalized positive matrix is exactly 1. |

## Review Record

The [original root finding](../../reviews/Yin_R_F0008_v2.md#capacity-ms24-finding) checks the main determinant and integer-capacity chains, selected normalization corrections, and the exact quantified GGOW input.
Its inherited mathematical-development context remains unknown; relocation does not turn it into a new isolated review.
It retains the external foundations and scope limits stated in the units.

The assigned source reviewer read pp. 1-19 in the local extraction and visually inspected the key statements and formula/normalization passages on pp. 3-4, 7-9 and 11-17.
The reviewer also checked the named primary MS17 and HS07 passages, reused the existing MSY23 audit, and coordinated the Gur04 and GGOW20 interfaces with their assigned reviewers.
The root reviewer separately identified the p. 8 adjoint and arbitrary-scaling errors and read all five unit records during cross-source review.
This is an AI source review, not formal verification or external human review.

The authoritative mathematical content and dependency qualifications belong to the units.
The normalized determinant formula and capacity estimate supply logarithmic control of small singular values.
They do not by themselves supply a spectral gap, a bounded inverse, or rational L2-to-boundedness for the active Yin_T_F0001.

<a id="notation-recheck"></a>
## Notation Recheck, 2026-09-13

The retained 19-page arXiv:2406.15922v1 PDF was re-read at the relevant passages below; printed and one-based PDF page numbers agree.
Text extraction was checked against rendered pages 3, 7, 8, 12, 14 and 15.
These are observations of the source.

| Object or use | Actual source notation and locator | Scope of the observation |
| --- | --- | --- |
| Matrix coefficients and evaluated pencils | `a_i` in `M_m(C)`, `s_i` for semicircular variables, `S = sum a_i tensor s_i`; formal pencil `A`, other operators `T`; pp. 1, 3 and 15 | Distinguish coefficient matrices from pencils/operators by their roles. The introductory finite matrix is also called `B` on pp. 1-2, so there is no absolute ban on uppercase finite-matrix names. |
| General matrix argument and positive trial | `b`, also `b_1,b_2`; Definition 1.1 and Theorem 1.2, p. 3; Section 2.2, pp. 7-8; proof of Theorem 4.1, p. 15 | Lowercase `b` is used in the capacity infimum and later positive trials, not merely in the map definition. |
| Selected matrices and scaling factors | `c`, `c_1,c_2`, `c_delta`; Proposition 2.8, p. 8; Proposition 2.10, p. 9; Sections 3.2/3.4, pp. 13-14 | The source uses `eta(c)` and `eta(c_delta)` for these distinct objects. It does not require every literal argument of eta to be the letter b. |
| Hermitization and block covariance | `S^h`, `eta^h`, blocks `b_11,b_12,b_21,b_22`, and `rho,rho*`; Lemma 3.5(ii), p. 12 | The block covariance is `[[eta(b_22),rho(b_21)],[rho*(b_12),eta*(b_11)]]`. |
| Identities and traces | `1_m`, `1_{2m}`; `tr_m = Tr_m/m`; `(M_m(M),tr_m tensor tau)`; Remark 2.2(iii), p. 5, and Section 2.2, pp. 7-9 | Lowercase tr is normalized, uppercase Tr is not. The matrix size remains visible when hermitizing. |
| Determinants, expectation and adjoints | `det(b)` is ordinary; `Delta(b) = abs(det(b))^(1/m)`; `E = id tensor tau`; the map adjoint is defined using `tr_m(x y*)`; Proposition 2.3, p. 6, Section 2.2, p. 7, and Remark 3.6, p. 12 | Writing `Delta_m` makes the matrix size explicit. The adjoint maps are unchanged when using the unnormalized conjugate-first Hilbert--Schmidt pairing instead. |

<a id="presentation-observations"></a>
## Selected introduction and terminology observations

The original writing reading directly inspected printed/PDF pp. 1–4 and compared determinant and capacity definitions with the existing passage-level audit.
The introduction motivates spectral-mass detection through finite matrices, explains the information lost by a plausible model transfer and introduces capacity before its determinant formula.
The nomenclature on p. 3 explicitly extends semicircular terminology to nonselfadjoint coefficient matrices.
Definition 1.1 and Theorem 1.2 specify coefficient spaces, positive optimization domain and covariance before the determinant identity; p. 4 explains the formula's quantitative meaning and boundary.
The [ordinary determinant and capacity definitions](Yin_U001.md#determinant-convention) retain the zero mass, normalized matrix trace and distinction from the kernel-removing variant.
The [capacity entry](Yin_U001.md#capacity-and-scaling) permits positive maps, with complete positivity a stronger property.
A positive-definite matrix trial has a bounded inverse and a positive spectral gap.
An affiliated inverse of a general operator need not be bounded, and a regularized formula need not assume injectivity of the unregularized operator.
These observations are source presentation evidence; local letter choices and prose permissions belong to their actual writing-choice homes.
