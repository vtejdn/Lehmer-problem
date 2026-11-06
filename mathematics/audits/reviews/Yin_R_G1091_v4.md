---
author: Yin
---

# C868 v4: independent whole-proof review of integral Gram determinant and rank costs

Review act: 2026-11-05T20:03, UTC.
The human record author is Yin.
This reviewer did not participate in v4 development and was supplied the frozen candidate without development dialogue, a derivation summary or a suggested conclusion.
The fixed v1-v3 inputs and this reviewer's earlier findings were already in the current context.
They keep their actual old scopes and supply no automatic review of the new arithmetic determinant, rank, covariance or block-family statements.
The entire actual v4 Statement and Complete argument were read and independently checked, including all controls and the final comparison arguments.
No L133 v8 or other v4 development material was consulted.
No substantive proof repair was supplied.

## Inputs and retained scope

- [C868 v4 statement](../../claims/Yin_C_G0868_v4.md#statement) and [complete argument](../../claims/Yin_C_G0868_v4.md#argument): all IG0-IG13 assertions and all six proof sections, including examples, conditional returns and original-input limits.
- [V3 column inequality](../../claims/Yin_C_G0868_v3.md#matrix-column-determinant-gap): vector Parseval, the exact first-coefficient multiplication identity and the column defect before any smallest-singular-value replacement.
  The new Loewner and complete determinant consequences are checked here.
- [V3 metric calculation](../../claims/Yin_C_G0868_v3.md#matrix-metric-and-copy-costs): simultaneous positive-metric conjugation and the exact shear norm.
  The primitive arithmetic determinant and its controls are new v4 assertions, not inherited consequences of the old conditioning bound.
- [V3 normalized companion algebra](../../claims/Yin_C_G0868_v3.md#companion-reversal-cost): the Laurent-coefficient proof of the unitary equivalence.
  Its algebraic extension from integral matrices to real invertible matrices is checked directly below; no integer-germ conclusion is transferred to the general metric-adjoint construction.
- [C228 statement](../../claims/Yin_C_G0228_v1.md#statement) and [mixed-conjugate proof](../../claims/Yin_C_G0228_v1.md#mixed-conjugate-normal-obstruction): checked at the final comparison's exact rational-positive-metric, irreducible mixed-root, single-occurrence and coprime-padding scope.
  This obstruction is not a premise of the damping estimates, and C228's ordinary normal integral entropy theorem and external entropy input are not used.
- [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract): the unrestricted total logarithmic Mahler-gap objective, used only for the original-input and noncompletion comparison.

The earlier [R1091 v3 finding](Yin_R_G1091_v3.md#matrix-whole-proof-finding) is an unchanged predecessor review, not evidence that v4 was already checked.
No Lawton, MS12, C227 numerical interval, Potapov factorization or new external theorem is needed for this proof.
The new independently performed inspection belongs in this physical R version, preserving all previous versions.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | [V4 statement](../../claims/Yin_C_G0868_v4.md#statement) | Entire IG0-IG13 statement: full determinant bound, arithmetic rank price, primitive normalization, covariance, controls, conditional returns and fixed-positive block-family limitations. |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | [V4 argument](../../claims/Yin_C_G0868_v4.md#argument) | All six sections and their substantive interfaces, including actual finite-price constructions and the final metric-adjoint and C228 comparisons. |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | [V3 column estimate](../../claims/Yin_C_G0868_v3.md#matrix-column-determinant-gap) | Exact local-germ coefficient identity, vector Parseval and column defect; the full Loewner/determinant conclusion is newly checked in v4. |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | [V3 metric and shear calculation](../../claims/Yin_C_G0868_v3.md#matrix-metric-and-copy-costs) | Positive-metric conjugation and the exact size2 shear norm only; no old coverage of primitive integral Gram determinants or new rank costs. |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | [V3 companion algebra](../../claims/Yin_C_G0868_v3.md#companion-reversal-cost) | Normalized unitary equivalence from Laurent coefficients, checked also for the real invertible transformed matrix in v4; no unrestricted integral realization conclusion. |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | [C228 statement](../../claims/Yin_C_G0228_v1.md#statement) | Rational positive-metric normality obstruction for an irreducible mixed-real/nonreal factor occurring once, with a coprime rational padding factor; no ordinary normal integral entropy theorem review. |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | [C228 mixed-conjugate argument](../../claims/Yin_C_G0228_v1.md#mixed-conjugate-normal-obstruction) | Cyclic rational centralizer, real-root contradiction and rational reducing-subspace proof at the stated comparison scope, including Salem factors with cyclotomic padding. |
| [Integral Gram whole-proof finding](#integral-gram-whole-proof-finding) | [Original Task contract](../../tasks/Yin_T_G0001_v1.md#contract) | Required original-input supply and total-measure normalization; no Task-completion review or unrestricted positive-gap conclusion. |

## Obligations and decisive checks

### Complete Loewner order before taking determinants

Conjugating by the real positive square root S converts both H-contractions to Euclidean contractions and preserves the germ identity and determinant of Q(0).
The transformed first nonzero coefficient is D=SCS^(-1); its rank remains k.
Radial vector Parseval and monotone convergence apply only to the disk-holomorphic transformed Q and U.
Their equal constant coefficient is Q'_0, and the absence of earlier positive coefficients of F'-I gives U'_N-Q'_N=DQ'_0 in the stated multiplication order.

The squared triangle inequality yields the column defect
\[
 \|DQ'_0v\|^2\le4(\|v\|^2-\|Q'_0v\|^2).
\]
Substituting v=Q_0'^{-1}w gives exactly
\[
 I+D^*D/4\le Q_0'^{-*}Q_0'^{-1}.
\]
There is no interchange of the two inverse factors.
Both sides are positive definite, so conjugating by the inverse square root of the right side proves determinant monotonicity directly.
The right determinant is |det Q'_0|^(-2)=exp(2tau).
The singular values of Q'_0 lie in (0,1], proving tau>=0 as well.

Since D has rank k, its positive squared singular values are precisely lambda_1,...,lambda_k; all other eigenvalues of D*D are zero and contribute factors one.
This establishes the complete determinant and logarithmic expressions IG2-IG3.
The argument never assigns a boundary norm or full-disk continuation to F and never divides the price by dimension or rank.

### Integer polynomial coefficients and the rank refinement

For integral positive H and integral C, C^THC is integral.
With B=H^(-1)C^THC, the similarity SBS^(-1)=D*D is exact.
Thus B has k positive eigenvalues and r-k zero eigenvalues, including when C is singular or nilpotent.

The polynomial f_H(t)=det(H+tC^THC) has integer coefficients and satisfies
\[
 f_H(t)=\Delta\prod_{i=1}^k(1+t\lambda_i).
\]
Its degree is exactly k and its top coefficient is the positive integer Delta times the product of the positive eigenvalues.
Therefore product lambda_i>=1/Delta.
This uses one determinant identity and does not introduce Delta^k or require an integral factorization of H.

The displayed function log(1+exp(x)/4) is increasing and strictly convex with the derivatives given in the candidate.
Applying finite convexity to the logarithms of the positive eigenvalues gives the geometric-mean lower bound, and monotonicity permits insertion of their product bound.
Combined with IG3, this proves IG4 and its determinant-one specialization IG5 for every k>=1.

The coefficient of t is also a positive integer, equal to Delta times sum lambda_i.
Expanding the product at t=1/4 has nonnegative coefficients and gives
\[
 e^{2\tau}\ge1+\tfrac14\sum_i\lambda_i
              \ge1+\frac1{4\Delta}.
\]
This proves IG6 independently of any condition-number estimate.
All zero eigenvalues remain in the complete matrix model; only their unit determinant contributions have been simplified.

### Primitive rays and unimodular integral covariance

Positive scalar multiplication of H preserves the two contraction inequalities and leaves SCS^(-1), tau and the normalized determinant polynomial unchanged.
Clearing rational denominators and dividing the gcd gives the primitive integral representative whenever H is rational.
For a general ray containing an integral matrix, the same normalization applies to that matrix.

Uniqueness is verified by Bezout on all entries of the primitive matrix.
If c times that matrix is integral, an integer linear combination of its entries forces c to be an integer.
Positivity makes c a positive integer, so the primitive matrix has the least positive integral determinant on its ray.
The arithmetic statements consequently use Delta_prim, not a numerically normalized determinant of a nonintegral matrix.

For A in GL_r(Z), integral similarity preserves every Taylor coefficient's integrality and the rank of C.
The metric congruence and simultaneous similarity give the stated exact transformed contraction identity.
They also preserve the germ relation, invertibility of Q(0) and its determinant.
Direct multiplication yields
\[
 \widetilde H+t\widetilde C^T\widetilde H\widetilde C
   =A^T(H+tC^THC)A.
\]
Because det A is a signed unit, both its determinant and the normalized polynomial are preserved.
The integral inverse congruence proves the reverse gcd divisibility, so a primitive integral representative stays primitive and has unchanged determinant.
For a ray that is not itself integral, this applies to its primitive representative when one exists; existence of an integral representative is also preserved by the congruence.
No unsupported Euclidean-contractivity or rational-basis invariance is inferred.

### Every metric control has an actual realization

For H_N=A_N^TA_N with A_N=I+NE_12, positivity, integrality, primitivity and determinant one follow directly.
The largest eigenvalue is at least N^2+1 and the eigenvalue product is one, so the condition number tends to infinity.
The H_N operator norm is computed using A_N as an isometry to Euclidean space; it is unnecessary to assume that the symmetric square root commutes with F.
Since A_N commutes with F=I+zE_12, this norm is exactly the Euclidean norm of the same shear.
Its disk supremum is L=(sqrt5+1)/2.
Thus Q=L^(-1)I and U=FQ supply both actual contractions and finite price 2log L for every N.
This is a nonconstant rank-one example at Delta_prim=1, not a sharpness claim for IG5.

For Hhat_K=diag(1,K), the positive square root transforms E_12 to K^(-1/2)E_12.
The same exact shear norm verifies the asserted Q_K and U_K.
The metric is primitive integral with determinant K, its sole positive squared singular value is 1/K, and Delta lambda=1.
The identity log ell(a)=arsinh(a/2) proves the exact displayed price and its limit zero.
The price is of order K^(-1/2), whereas IG6 is of order K^(-1); the example attains the arithmetic coefficient bound without claiming analytic-price optimality.

Multiplying Hhat_K by K^(-1/2) gives numerical determinant one while preserving these contractions and prices.
For integer K>1 its first diagonal entry lies strictly between zero and one, so the resulting metric is not integral.
Its primitive integral representative is still Hhat_K, with determinant K.
This verifies the distinction between arithmetic Gram determinant and normalized covolume, and the failure of a uniform price bound over all positive integral metrics with unbounded primitive determinant.
These are analytic-germ controls, not original-polynomial counterexamples.

### Complete block-family spectrum, full price and existence

Put d=n+1.
The standard companion S_n has its first d-1 columns equal to successive coordinate vectors and its last column equal to three times the last coordinate vector.
The last two columns have Gram block [[1,3],[3,9]], of eigenvalues10 and0.
The other n-1 columns are orthonormal and orthogonal to those columns.
Thus the squared singular values are exactly10, then1 with multiplicity n-1, then0, including n=1.

Multiplication verifies the stated integral inverse of C_n^tr, so the block matrix is unimodular.
Its normalized reversal germ has first positive coefficient
\[
 D_n=\operatorname{diag}(-S_n^T,S_n).
\]
Both diagonal blocks have the same singular values.
Hence the complete squared singular spectrum is10 twice,1 with multiplicity2(n-1), and0 twice.
The rank is2n and the operator-norm square stays10.
Substitution in IG2 with H=I gives
\[
 e^{2\tau}\ge(7/2)^2(5/4)^{2(n-1)},
\]
which is precisely IG13 after taking logarithms.

The block Schur complement for t nonzero gives
\[
 \det(tI-C_n^{\rm tr})
 =t^{n+1}q_n(t+t^{-1})
 =(t^2-3t+1)(1+t^2)^n.
\]
Polynomial identity then includes t=0.
The first factor has reciprocal positive roots with larger root (3+sqrt5)/2, and the other factors have unit-circle roots.
This proves the exact fixed positive total measure without deleting cyclotomic factors or their multiplicities.

The finite-price existence assertion is also valid.
For each fixed n, h_n(0)=1, and both h_n I and (I-z(C_n^tr)^(-T))adj(I-zC_n^tr) are polynomial matrices with finite norm suprema on the closed disk.
Choose a sufficiently small positive eta, at most one.
The displayed Q and U are then contractions, satisfy the germ identity by the adjugate formula, and have Q(0)=eta I invertible with finite price.
This is an existence proof for each fixed n, not an original-measure upper bound.

Since the exact Mahler measure is fixed but IG13 diverges, no finite constant C_tr can bound the prices by C_tr m(P_n) for all these particular germs with Euclidean metric.
The conclusion is confined to the specified complete block matrices and H=I realizations.
It does not quantify over other matrix candidates, independently chosen Euclidean integral bases or a prior removal of cyclotomic content.
Simultaneous metric covariance does not license changing the metric to a new Euclidean one for free.

### Conditional return and both final comparison arguments

For an actual realization with a primitive integral representative and Delta_prim<=Delta_*, IG6 and the assumed upper price bound imply IG10 by monotonicity.
For Delta_prim^(1/k)<=Ak, IG4 and log(1+x)>=x/(1+x) give
\[
 \tau\ge\frac{k}{2}\log(1+1/(4Ak))
 \ge\frac1{8A+2/k}\ge\frac1{8A+2}.
\]
The stated lower bound for m(P) follows only after using the actual assumption tau<=C_tr m(P).
No primitive metric, arithmetic comparison, uniform constant or original realization is manufactured by these implications.
For a zero-measure P, their positive conclusion simply makes the nonconstant-germ and upper-price premises incompatible.

For the metric-adjoint companion, S C_0^dagger S^(-1)=T^T with T=SC_0S^(-1), so the transformed G_H has exactly the normalized v3 form.
The Laurent-coefficient calculation proving unitarity if and only if T^(-T)=T uses real invertibility, not integrality.
It therefore applies at this new interface.
That condition is equivalent to C_0^dagger C_0=I and makes T orthogonal.
Similarity then puts every eigenvalue of C_0 on T, so its monic characteristic polynomial has zero logarithmic Mahler measure.
The argument does not supply an integer germ for general integral H; inverse Gram denominators can remain.
Positive original measure still excludes this particular all-pass construction.

The C228 comparison was checked at its actual negative-result scope.
For an irreducible rational characteristic polynomial p, cyclicity gives rational centralizer Q[T].
If a rational positive metric made T normal, its rational adjoint would equal f(T).
Unitary diagonalization after real metric conjugation makes f(lambda)=conjugate(lambda) at each root.
At one real root, f(alpha)=alpha; irreducibility then forces this equality at all conjugates, contradicting a nonreal root.
For p occurring once with coprime padding, V=ker p(U) is rational of the required dimension and invariant under both U and its commuting adjoint.
Restriction supplies the forbidden rational positive-metric model.
This validates the stated Salem/cyclotomic-padding comparison, while excluding neither irrational positive metrics nor arbitrary nonnormal models.
C228's separate entropy theorem is not needed.

## Verification and source limits

All new inequalities, determinant coefficients, covariance identities, controls and block-family formulas were checked as exact mathematics.
No numerical experiment, symbolic output or structural tool result substitutes for these derivations.
The supporting v3 calculations are used only at their actual algebraic and finite-germ interfaces.
The relevant C228 negative proof was rechecked directly, without importing its entropy formula or external source assumptions.
No new external theorem, source proof audit, literature-priority conclusion or exhaustive novelty search is asserted.
No unresolved mathematical or source-applicability gap was found within the actual reviewed scope.

## Integral Gram whole-proof finding

The complete frozen C868 v4 Statement and Argument are mathematically supported under their precise hypotheses, with no gap found.
This independently reviewed whole-proof finding includes IG0-IG13, all controls, actual finite-price realizations, covariance, conditional returns and the final comparison limits.
No substantive repair was contributed by the reviewer, and no unfinished mathematical review obligation is identified within this candidate.
The missing original-input realization, compatible contractions, paid primitive determinant/rank comparison and original Mahler upper-price bound remain explicit research obligations.
Neither the fixed-positive block family nor the degenerating metric controls solve or refute G0001.
All earlier C868 and R1091 versions retain their own scopes.
This review changes no Claim assessment, strategy, index, execution boundary or repository configuration.
