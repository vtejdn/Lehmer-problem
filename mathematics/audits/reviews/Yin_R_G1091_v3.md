---
author: Yin
---

# C868 v3: independent whole-proof review of the matrix criterion and original-input obstructions

Review act: 2026-11-05T19:17, UTC.
The human record author is Yin.
This reviewer did not develop the candidate and received the fixed C868 v3 text without additional author derivation summaries, development dialogue or proposed review conclusions.
The scalar v1/v2 proofs and this reviewer's [v1](Yin_R_G1091_v1.md#whole-proof-finding) and [v2](Yin_R_G1091_v2.md#general-blocks-whole-proof-finding) findings were already in the current context.
Those findings retain their exact original scopes and do not review the new matrix results.
The actual v3 statement and all five argument sections were read, their obligations were enumerated, and every step was independently checked.
L133 v6, other development notes and the contributing agents' messages were not read.

After the initial findings, the author narrowed the original-target sentence to the intended domain of every positive-measure original reciprocal P.
The reviewer read back that actual sentence.
This makes the conditional application's domain explicit; it changes none of M1-M10 or their proofs, supplies no realization and requires no substantive proof repair from this reviewer.
The final finding below concerns that actual positive-measure wording.

## Inputs and applicability

- [C868 v3 statement](../../claims/Yin_C_G0868_v3.md#statement) and [complete argument](../../claims/Yin_C_G0868_v3.md#argument): all matrix-germ, metric, replication, companion and rational-pole assertions, their controls and the final conditional original-input interface.
- [C227 statement](../../claims/Yin_C_G0227_v1.md#statement) and [exact retained P0 example](../../claims/Yin_C_G0227_v1.md#no-neutral-symmetric-completion): only P0(t)=t^14-t^12+t^7-t^2+1 and the accepted interval 1<M(P0)<13/10 are used mathematically.
  Its [selected decision](../../claims/Yin_C_G0227_v1.md#decision-complete-retained-proof-adoption) retains that source acceptance and its actual self-review relationship.
  Neither the remaining C227 realization/metric results nor its entire proof are adopted as inputs of this finding.
- [MS12 U001](../literature/MS12/Yin_U001.md#ms12-u001): checked for the retained arXiv:0907.0371v1 edition, the exact polynomial example on page5 and the statement/applicability-only source acceptance.
  The classification and computations behind C227's accepted data remain external inputs; they were not rerun or independently proved here.
- [AJL16 U001](../literature/AJL16/Yin_U001.md#ajl16-u001): checked as related attribution at arXiv:1410.0283v2, Theorem3.1, equations(3.2)-(3.5), printed/PDF pages10-11.
  Its complex rational factorization result is not a premise of the local matrix estimate or pole proof and supplies no rational/integer descent or original-input cost bound.
- [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract): the unrestricted total logarithmic Mahler gap, used only to check the candidate's conditional interface and noncompletion boundary.

The [v2 finite-germ argument](../../claims/Yin_C_G0868_v2.md#germ-first-crossing) is a method predecessor, not a theorem transferring a scalar bound to matrices.
The new proof supplies its own vector Parseval estimates and determinant normalization.
C296, C475, C65, C67, C36, C90 and L133 occur as comparison or motivation references, not unproved mathematical premises in the supplied v3 argument.
Their other theorems, historical contribution claims and exhaustive comparison/priority questions are outside this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Matrix whole-proof finding](#matrix-whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Matrix whole-proof finding](#matrix-whole-proof-finding) | [V3 statement](../../claims/Yin_C_G0868_v3.md#statement) | Entire M1-M10 statement, all metric and replication costs, both companion restrictions, rational-pole rigidity and the conditional application to positive-measure original reciprocal inputs. |
| [Matrix whole-proof finding](#matrix-whole-proof-finding) | [V3 argument](../../claims/Yin_C_G0868_v3.md#argument) | All five sections and all substantive interfaces, including the exact varying-metric control, P0 companion comparison and original-input limitations. |
| [Matrix whole-proof finding](#matrix-whole-proof-finding) | [C227 statement](../../claims/Yin_C_G0227_v1.md#statement) | Exact P0 and accepted multiplicative-measure interval 1<M(P0)<13/10 only; no new review of C227's full theorem or source classification. |
| [Matrix whole-proof finding](#matrix-whole-proof-finding) | [C227 retained example](../../claims/Yin_C_G0227_v1.md#no-neutral-symmetric-completion) | Source-backed exact P0 identity and interval, distinguished from a positive root or rounded numerical certificate; other realization conclusions are unused. |
| [Matrix whole-proof finding](#matrix-whole-proof-finding) | [MS12 retained source scope](../literature/MS12/Yin_U001.md#ms12-u001) | Exact source edition/example and the original statement-only acceptance boundary supporting the C227 interface; no classification or computation proof audit. |
| [Matrix whole-proof finding](#matrix-whole-proof-finding) | [AJL16 attribution](../literature/AJL16/Yin_U001.md#ajl16-u001) | Related complex rational circle-isometry and Blaschke-Potapov attribution only; no theorem use, original-proof audit, descent or determinant-cost conclusion. |
| [Matrix whole-proof finding](#matrix-whole-proof-finding) | [Original Task contract](../../tasks/Yin_T_G0001_v1.md#contract) | Scope comparison and actual missing original-input supply; explicitly not a Task-completion review. |

## Obligations and decisive checks

### Matrix coefficient gap and the complete determinant cost

The first obligation is to justify estimates on Q and U without extending F beyond its given germ.
For each vector v and radius rho<1, vector Parseval bounds the sum of rho^(2n)||Q_n v||^2 by ||v||^2.
Monotone convergence of this nonnegative series gives the corresponding coefficient estimate at radius1.
The same reasoning applies to U, and the germ identity gives U_0=Q_0.
Hence each positive coefficient of either function has squared column norm at most ||v||^2-||Q_0 v||^2.

For the first nonzero C_N, all earlier positive coefficients of F vanish.
The exact local multiplication therefore gives U_N-Q_N=C_N Q_0 in the stated order.
The squared triangle inequality bounds ||C_N Q_0 v||^2 by four times the shared column defect.
It uses neither the full tail of F nor a boundary H2 assumption on F.

Every singular value s_i of the invertible contraction Q_0 lies in (0,1].
Thus tau=-sum log s_i>=0 and min s_i>=product s_i=exp(-tau).
Substituting v=Q_0^(-1)w yields
\[
 \|C_Nw\|^2
 \le 4\bigl(\|Q_0^{-1}w\|^2-\|w\|^2\bigr)
 \le 4(e^{2\tau}-1)\|w\|^2.
\]
Taking the supremum over unit w proves the operator-norm estimate in M2.
A nonzero integer matrix has a column with Euclidean norm at least1, so its operator norm is at least1.
Rearranging gives precisely tau>=(1/2)log(1+||C_N||op^2/4)>=c_mat.
Neither the Parseval estimate nor the minimum-singular-value bound introduces a factor r.
The assertion also handles tau=0 correctly: no positive coefficient of a nonconstant germ can then exist.

### Positive metrics, the exact degenerating control and scalar replication

For positive Hermitian H, S=H^(1/2) is invertible and the metric inequalities are equivalent to Euclidean contractivity after simultaneous conjugation by S.
The transformed identity remains U_tilde=F_tilde Q_tilde, and determinant Q_0 is unchanged.
The first transformed coefficient need not be integral, but
\[
 1\le\|C_N\|_{\mathrm{op}}
 \le\sqrt{\kappa}\,\|S C_N S^{-1}\|_{\mathrm{op}}.
\]
The previous coefficient estimate, before its integrality step, applies to the transformed functions.
Combining these inequalities gives 1/kappa<=4(exp(2tau)-1), exactly M3.
This argument uses a positive definite Hilbert metric; an indefinite symplectic identity does not provide the same contraction premise.

For the explicit size2 control, conjugating I+zE_12 by diag(kappa^(-1/2),1) gives the shear with off-diagonal entry a z.
A shear with entry w has squared singular values of product1 and sum2+|w|^2.
Solving this quadratic gives largest singular value (sqrt(4+|w|^2)+|w|)/2.
Its disk supremum is L and L>=1.
Thus Q=L^(-1)I_2 and U=FQ satisfy the metric contractions, are disk-holomorphic and have invertible Q_0.
Their determinant cost is exactly 2log L and tends to0 as kappa tends to infinity, while the size and integral nonconstant germ stay fixed.
This proves failure of a bound uniform over all positive metrics in this model.
It makes no claim that the particular bound M3 is sharp or that this family realizes original integer polynomials.

For a scalar copy Q=qI_r with q(0)=exp(-a), the determinant at0 is exp(-ra), so tau=ra exactly.
The universal consequence of M2 is therefore a>=c_mat/r.
Replacing the total cost by a would be a normalization error; the candidate does not make that replacement.
No degree-independent original Mahler bound is obtained from scalar copying alone.

### Companion identities, boundary unitarity and the constant-term obstruction

Unimodularity makes C^(-1) integral.
The local Neumann series for (I-zC)^(-1) proves analyticity near0 and the asserted integral Taylor germ for G_C.
Left multiplication by -C^(-T) gives the stated formula for G_C with constant coefficient I_r.

On T, direct multiplication of N_C=zI-C^T and D_C=I-zC gives the two products displayed in the proof.
Their difference is CC^T-C^TC.
Conjugation by D_C^(-1) proves M7 at every regular point.
There are only finitely many exceptional points because det D_C is a nonzero polynomial with value1 at0.
A unitary identity on a full-measure regular subset therefore forces the constant commutator to vanish; conversely a zero commutator gives boundary unitarity.
This checks both directions and does not confuse normality with orthogonality.

For G_C, the difference K_C*K_C-D_C*D_C is
\[
 z(C-C^{-T})+z^{-1}(C^T-C^{-1})+C^{-1}C^{-T}-C^TC.
\]
A Laurent polynomial vanishing almost everywhere on T has every Fourier coefficient zero.
Its coefficient of z gives C=C^(-T).
Conversely this equality makes G_C the identity as a rational function, proving M8.
Orthogonal integer columns have a single signed unit in distinct rows, so such C is a signed permutation matrix of finite order and has zero characteristic-polynomial Mahler measure.

For reciprocal P with P(0)=1, det D_C=z^rP(1/z)=P(z), while det(zI-C^T)=P(z).
Hence det R_C=1.
Also det(-C^(-T))=1/P(0)=1, proving det G_C=1.
These rational determinant identities alone impose no unitary or operator-norm control.

For the unnormalized realization, U(0)=-C^TQ_0.
The singular-value estimate for Q_0 needs only its contraction and invertibility, so it still applies although R_C(0) is not I_r.
The operator inequality
\[
 1\ge\|C^TQ_0\|_{\mathrm{op}}
 \ge \sigma_{\min}(Q_0)\|C\|_{\mathrm{op}}
 \ge e^{-\tau}\|C\|_{\mathrm{op}}
\]
proves M9.
The middle inequality follows also by writing C^T=(C^TQ_0)Q_0^(-1), so the side of multiplication causes no gap.

For the stated standard companion of P0, the last column contains precisely the four nonzero coefficients at exponents0,2,7,12, each of modulus1.
It has Euclidean norm2 and therefore ||C||op>=2.
The accepted C227 interval gives 0<m(P0)<log(13/10), while M9 forces tau>=log2.
Thus equality tau=m(P0) is impossible for this particular unnormalized candidate.
The control is one fixed positive-measure polynomial; it neither excludes all larger uniform comparison constants nor requires irreducibility of P0.
Failure of circle unitarity for G_C also does not exclude every possible nonunitary Schur-quotient realization of that germ.

### Rational circle-pole rigidity at every allowed multiplicity

Boundary unitarity bounds the modulus of each rational entry of W by1 almost everywhere at regular points of T.
A genuine pole at the chosen circle root beta has a nonzero leading polar coefficient and diverges along every sufficiently short punctured circle arc toward beta.
It therefore contradicts that almost-everywhere bound.
No cancellation between different matrix entries can hide the pole, because each entry is individually bounded.

A reduced entry has denominator dividing z^k P^m.
If a positive power of P remains, its reduced numerator is not divisible by P.
Irreducibility over Q and the rational numerator imply that this numerator is nonzero at beta; otherwise P would divide it as the minimal polynomial of beta.
The remaining denominator would then create a genuine pole at beta.
Thus all powers of P disappear.
Holomorphy at0 removes the possible remaining power of z, so each entry is a polynomial.
This is the exact point where rational coefficients and the restriction on finite nonzero pole factors are used.

For polynomial W, Parseval on each row gives total coefficient square energy1 from boundary unitarity.
The constant row of W(0)=I_r already has energy1.
All nonconstant coefficients vanish, proving W=I_r.
The final argument does not need integral coefficients, a support bound or a degree bound.
It applies equally to a linear irreducible factor with circle root and to higher-degree irreducible P with only some conjugates on T.
Additional denominator factors or a larger coefficient field invalidate the stated cancellation argument and are correctly left outside M10.

### Original-input supply and the scope of the controls

If a positive-measure original reciprocal P actually supplies all of M1 with nonconstant integral F and tau<=C_tr m(P), combining the two inequalities gives m(P)>=c_mat/C_tr.
Uniformity requires the same positive C_tr independent of the original degree.
The final statement explicitly restricts this proposed universal supply to positive-measure inputs.
For a zero-measure input the same nonconstant-germ and cost assumptions would be incompatible; no conclusion for such an input is manufactured by that conditional interface.

No argument in the candidate constructs Q,U with that uniform original-input price.
The metric control is a valid model family with deteriorating conditioning, not an original-polynomial family with positive measures tending to zero.
The companion comparison is a fixed-positive obstruction to one normalization price, not a rejection of every possible construction.
The pole argument excludes the stated rational circle-unitary denominator class and does not apply to every nonunitary quotient UQ^(-1).
Consequently the candidate supplies neither a new positive sequence tending to zero nor a proof of the unrestricted G0001 gap.

## Source completeness and verification limits

The proof of M1-M10 is local except for the explicitly isolated exact P0 measure interval used in the fixed companion comparison.
That interval is reused from the current adopted C227 statement at its retained MS12 acceptance scope.
No source classification, original numerical computation, P0 root approximation or irreducibility assertion was newly checked or needed.
AJL16 supplies related attribution only, and its complex factorization theorem is not used to claim rational descent or a determinant price.
The scalar predecessors motivate a finite-germ method but do not supply new matrix review coverage.
No unresolved mathematical or source-applicability gap was found for the actual inputs and uses examined.
This is not an exhaustive novelty or historical-attribution review, a formal verification, or a new audit of the external source proofs.

## Matrix whole-proof finding

The full current C868 v3 statement and complete argument are mathematically supported under their exact hypotheses, with no gap found.
This is an independently reviewed whole-proof finding for M1-M10, the exact controls and the final conditional positive-measure original-input interface.
No substantive repair was contributed by the reviewer.
No further mathematical review obligation is identified within this candidate's stated scope.
The missing uniform original-input realization is explicitly retained as unsupplied research work and is not silently discharged by this finding.
C868 v1/v2 and R1091 v1/v2 keep their original scopes; this new review changes no C assessment, index, strategy, execution boundary or repository configuration.
