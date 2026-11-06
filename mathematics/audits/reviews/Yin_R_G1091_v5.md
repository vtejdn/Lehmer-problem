---
author: Yin
---

# C868 v5: independent whole-proof review of the exact rational Schur price

Review act: 2026-11-05T20:40, UTC.
The human record author is Yin.
This reviewer did not participate in v5 development and received the fixed candidate without development discussion, a derivation summary or a suggested mathematical conclusion.
The fixed v1-v4 inputs and this reviewer's earlier independent findings were already in context.
Their scopes remain unchanged; they do not automatically cover the new rational optimization theorem.
The complete actual v5 Statement and Argument were read, the obligations below were reconstructed, and an initial mathematical conclusion was formed before comparing with retained review evidence.
No L133 v8 or author development dialogue was consulted.
No substantive repair was supplied.
The present finding is a new independent review of the actual v5 proof, including its examples, inherited arithmetic interface, attribution and original-input limits.

## Inputs and retained scope

- [C868 v5 statement](../../claims/Yin_C_G0868_v5.md#statement) and [complete argument](../../claims/Yin_C_G0868_v5.md#argument): all RP1-RP11 assertions and all seven proof sections.
- [DR10 U002](../literature/DR10/Yin_U002.md#dr10-u002): the accepted polynomial matrix Fejer--Riesz statement, adjoint orientation and outer convention for the retained 33-page author survey, Theorem 2.1 and context on pages 4-7.
  Its statement and finite-matrix applicability are accepted inputs; its original operator proof is not independently re-audited here.
- [C F0008 finite-matrix bridge](../../claims/Yin_C_F0008_v1.md#matrix-finite-gram-capacity): only the argument under Matching feasible matrix and the outer boundary, from the source's outer convention to disk invertibility and scalar polynomial Jensen.
  That bridge was directly rechecked; the rest of the capacity theorem, its normalization and its historical review relationship are not newly assessed.
- [C868 v4 statement](../../claims/Yin_C_G0868_v4.md#statement) and [Loewner determinant argument](../../claims/Yin_C_G0868_v4.md#gram-loewner-determinant): only the Euclidean specialization H=I of the full determinant bound needed for RP11.
  Its finite-germ coefficient identity, Parseval estimate and determinant interface were rechecked.
- [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract): original total logarithmic Mahler measure and the unrestricted positive-gap objective, used only for the noncompletion comparison.

The earlier [R1091 v4 finding](Yin_R_G1091_v4.md#integral-gram-whole-proof-finding) retains its actual scope.
No v4 metric, covariance, block-family or C228 comparison assertion is needed for the new analytic price theorem.
The L133 references in v5 identify earlier constructions; their stated scalar prices are checked directly from the explicit v5 models below, without treating unread development material as evidence.
This review does not audit the historical wording or provenance of that ledger.

Two external passages were directly text-read for attribution only.
Olavi Nevanlinna, [Growth of operator valued meromorphic functions](https://www.acadsci.fi/mathematica/Vol25/nevanli.pdf), Annales Academiae Scientiarum Fennicae Mathematica 25 (2000), 3-30, Definition 2.4 on printed page 8 and Definitions 2.7, 2.9 and Lemmas 2.8-2.9 on pages 12-16, identifies the total logarithmic singular-value size and its pole characteristic.
The finite-dimensional specialization matches the quantities used here; it is not adopted as a Schur optimization theorem.
Vanni Noferini and Paul Van Dooren, [Computing a compact local Smith McMillan form](https://arxiv.org/pdf/2303.10403v1), arXiv:2303.10403v1, Section 2.1, equation (1) and following text on pages 2-3, confirms the local-form terminology, invertible local factors and negative pole indices.
This supplements the terminology locator, without importing its later algorithms or replacing v5's local valuation proof.
Neither passage supplies a literature-priority claim or a full-source proof audit.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Rational price whole-proof finding](#rational-price-whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Rational price whole-proof finding](#rational-price-whole-proof-finding) | [V5 statement](../../claims/Yin_C_G0868_v5.md#statement) | Entire RP1-RP11 statement: total determinant price, all local multiplicities, rational approximation, circle-unitary attainment, both exact integral model prices, arithmetic consequence and original-input limits. |
| [Rational price whole-proof finding](#rational-price-whole-proof-finding) | [V5 argument](../../claims/Yin_C_G0868_v5.md#argument) | All seven sections, including local elimination, interior Jensen, polynomial cancellation module, exact inner factor, boundary majorants and limits, complete model calculations and final scope comparison. |
| [Rational price whole-proof finding](#rational-price-whole-proof-finding) | [DR10 U002](../literature/DR10/Yin_U002.md#dr10-u002) | Accepted finite square polynomial factorization B=H*H and the exact source outer convention at statement/applicability depth; no new audit of the original operator proof, uniqueness or coefficient-field conclusion. |
| [Rational price whole-proof finding](#rational-price-whole-proof-finding) | [C F0008 bridge](../../claims/Yin_C_F0008_v1.md#matrix-finite-gram-capacity) | Only the finite-dimensional deduction that a nonzero-determinant outer polynomial has dense full Hardy-space multiplier range, hence no disk determinant zero, followed by scalar polynomial Jensen; no whole capacity-theorem review. |
| [Rational price whole-proof finding](#rational-price-whole-proof-finding) | [V4 statement](../../claims/Yin_C_G0868_v4.md#statement) | H=I specialization of IG2-IG3 for a nonconstant integral germ and any disk-holomorphic admissible pair, used only to obtain RP11. |
| [Rational price whole-proof finding](#rational-price-whole-proof-finding) | [V4 determinant proof](../../claims/Yin_C_G0868_v4.md#gram-loewner-determinant) | Exact first nonzero coefficient identity, vector Parseval, column defect, inverse-factor order and determinant monotonicity at the Euclidean interface. |
| [Rational price whole-proof finding](#rational-price-whole-proof-finding) | [Original Task contract](../../tasks/Yin_T_G0001_v1.md#contract) | Original-input supply, positive total-measure scope and noncompletion comparison only; no Task-completion or unrestricted gap review. |

## Obligations and decisive checks

### Local cancellation length and the lower bound

The statement requires the actual pole-cancellation colength, including simultaneous zeros and poles, rather than the net determinant order.
For t=z-a, a sufficiently large k gives t^k O_a^r contained in K_a(F), so the colength is finite.
Colength zero makes every coordinate vector belong to K_a and therefore makes every column of F holomorphic.
This also verifies the claimed equivalence between positive multiplicity and an actual matrix pole.

The least-valuation pivot has holomorphic quotients into the other entries in its row and column.
The elementary elimination is therefore invertible over O_a even when its pivot order is negative.
The remaining block has no entry of smaller order, and full rational rank prevents an identically zero residual pivot.
This proves the stated diagonal form with nondecreasing integer exponents.
Invertible holomorphic transformations preserve the least valuation of the nonzero minors of every size, by the minors formula applied in both directions.
Their successive sums determine the ordered exponents uniquely.

In the right-factor coordinates, precisely the negative exponents impose coordinate divisibility.
The quotient dimension is their negative sum, proving RP4.
For a holomorphic Q with FQ holomorphic, the same row divisibilities force ord_a det Q>=delta_a(F).
For a holomorphic full-rank M, the nonnegative diagonal orders similarly give colength(M O_a^r)=ord_a det M.
None of these conclusions discards a positive exponent against a negative one.

For an admissible pair, the identity U=FQ continues meromorphically from the germ throughout the disk.
On each allowed interior circle, the determinant and rational exceptional sets are avoided.
With V=QQ* and K=F*F, contractivity gives V<=I and V<=K^(-1).
The latter follows by multiplying FVF*<=I by F^(-1) and F^(-*), in that order.
In a unitary eigenbasis of K, the diagonal bounds and Hadamard's inequality imply
\[
 |\det Q|^2\le\prod_j\min(1,\sigma_j(F)^{-2}).
\]
This is the full unnormalized determinant bound.

Scalar Jensen on the interior circle counts every forced zero of det Q with its multiplicity.
Discarding only the other nonnegative zero terms gives the displayed lower bound (5).
The permitted radii can approach one because det Q is not identically zero and its zeros are discrete.
The finite disk-pole sum converges to N(F), while Fatou applies to the nonnegative singular-value integrands.
This proves tau(Q)>=J(F)+N(F) without any boundary theorem for Q or U.
Rational boundary poles give at worst finite logarithmic singularities, so J(F) is finite.
There is no pole at zero and no missing infinite disk sum.

### The polynomial module and its exact inner denominator

Lambda contains d_0 C[z]^r.
The coordinate-projection induction produces a polynomial basis: each nonzero projected ideal is principal, subtraction removes that coordinate, and the residual module still contains the remaining d_0 coordinate vectors.
The constructed columns are independent and span the whole module, not merely a finite-index polynomial submodule.

At each disk pole, the Chinese remainder jet argument gives M O_a^r=K_a(F).
Matching the jet through k_a-1 at a and vanishing through k_b-1 at the other poles puts the chosen polynomial in Lambda.
The remaining local error belongs to t^k_a O_a^r, which lies in M O_a^r because d_0/t^k_a is a unit.
Thus the exact local determinant multiplicity follows from the previously proved holomorphic colength identity.

The polynomial identity M K_0=d_0 I excludes all other determinant zeros.
Consequently det M=c product_a(z-a)^delta_a, including the empty-pole case.
In particular M is invertible on the circle and at zero.

M*M is a nonnegative finite matrix Laurent polynomial of the size required by DR10 U002.
The factor orientation H_0*H_0 is the one needed for B=M H_0^(-1).
Its determinant is not identically zero.
Under the accepted outer convention, a proper range subspace would contain every value of H_0 and contradict that nonzero determinant.
The range subspace is therefore the full C^r.
Continuous, onto point evaluation and dense multiplier range then exclude every disk zero of det H_0.
Circle invertibility follows separately from M*M=H_0*H_0.
This checks the precise C F0008 bridge; no normalized capacity formula is used.

It follows that B is rational and holomorphic on a neighborhood of the closed disk.
The factorization makes B unitary on the circle, and scalar maximum principles for w*Bv give disk contractivity.
FM has no disk poles, so G=FB is disk-holomorphic.
Scalar polynomial Jensen for det H_0 and det M gives
\[
 -\log|\det B(0)|=\sum_a\delta_a\log(1/|a|)=N(F).
\]
The determinant zeros of B are exactly the prescribed ones.
Right multiplication by its circle-unitary values preserves all singular values of F and therefore J(G)=J(F).

### Boundary cancellation, rational approximation and limit interchange

A disk-holomorphic rational G has a reduced scalar common polynomial denominator d with no disk zeros and d(0) nonzero.
Circle zeros of d remain allowed.
The field W=max(|d|^2 I,N*N) is well defined because the first argument is scalar.
Its absolute-value expression proves continuity.
It dominates both arguments and is positive definite except possibly at the finitely many circle zeros of d.

Off that exceptional set, diagonalization gives
\[
 \log\det W=2r\log|d|+2\sum_j\log^+\sigma_j(G).
\]
The field is bounded above, and W>=|d|^2 I gives an integrable lower logarithmic bound.
This verifies integrability even when the rational germ has genuine boundary poles.

Uniform entrywise Fejer approximation gives a Hermitian Laurent polynomial approximation in operator norm after choosing the entrywise error sufficiently small.
Adding 2 epsilon I gives W+epsilon I<=W_epsilon<=W+3 epsilon I.
The accepted factorization and the same outer bridge give an H_epsilon whose inverse is rational and holomorphic on a neighborhood of the closed disk.

The order of the factors in Q_epsilon=BdH_epsilon^(-1) and U_epsilon=NH_epsilon^(-1) is correct.
They satisfy FQ_epsilon=U_epsilon, and Q_epsilon(0) is invertible.
Conjugating W_epsilon>=|d|^2 I and W_epsilon>=N*N by H_epsilon^(-1) proves both circle contraction inequalities.
The maximum principle extends them throughout the disk.
The d factor explicitly cancels the remaining boundary poles; the argument does not infer disk holomorphy from a boundary estimate.

Taking determinants and using zero-free polynomial Jensen gives the exact price (16), with the term -r log|d(0)|.
For epsilon<=1, log det W_epsilon has a uniform finite upper bound and lower bound 2r log|d|.
Thus a constant plus 2r log^-|d| dominates its absolute value.
Dominated convergence is valid despite the possible circle zeros of d.
Jensen for d still gives mean log|d|=log|d(0)| when its zeros include circle points but none inside.
The limiting price is N(F)+J(F).

The lower bound applies to every admissible holomorphic pair, while the constructed sequence is rational and holomorphic beyond the closed disk.
This proves both asserted infima and nonemptiness.
It proves arbitrarily close rational prices, without asserting general attainment or any arithmetic field for the factors.
No division by r enters the calculation.

### Circle-unitary attainment

A rational scalar entry with a genuine boundary pole is unbounded on a punctured circle arc.
This contradicts its almost-everywhere modulus bound inherited from unitarity.
Thus a circle-unitary rational F has no circle poles and J(F)=0.

The previously constructed B has exact price N(F).
The rational G=FB has no disk or circle pole and is unitary on the circle.
Both B and G are contractions by the maximum principle and are holomorphic on a neighborhood of the closed disk.
They give the claimed exact minimum and retain every determinant-zero multiplicity.
The proof requires no coefficient-field descent.

### Both integral models and the scalar-price comparisons

The identities A-P=2z and A+P=2(z-1)^2 imply A^2-4z(1-z)^2=P^2.
Hence det T=1 and its inverse is exactly (18).
On the circle, conjugate(a)=a and conjugate(b)=-zb give T*=T^(-1).
The same holds for the pullback and embeddings.
Because P(0)=1, all Taylor coefficients of T and its inverse are integers.

For F_pull, T(0)=I+2E_12 and the derivative of T(z^2)^(-1) at zero vanishes.
Direct multiplication with T(0)^(-1) gives first coefficient [[2,0],[2,-2]], confirming the displayed expansion, constant I and nonconstancy.
For F_same, the two constant embedded shears commute, so the constant coefficient is I.
Writing c=zb, direct multiplication gives its entries
\[
 (F_{\rm same})_{11}=a^4-2abc=a^4-2azb^2,\qquad
 (F_{\rm same})_{32}=-bc=-zb^2.
\]
The latter confirms nonconstancy.

The roots of P are rho and lambda=rho^(-1), with 0<rho<1.
At rho, the numerator of T is nonzero, has rank one and has a genuine simple pole after division by P.
The smallest local exponent is -1 and their sum is zero, so they are (-1,1).
The same holds for T^(-1).

For F_pull, the other factor is locally holomorphic and invertible at each of rho and the two square roots of rho.
The map z to z^2 is unramified at those square roots.
Consequently the only disk poles are rho, sqrt(rho) and -sqrt(rho), each with delta=1.
Their weighted sum is 2 log lambda.

For F_same, every entry has denominator P^4.
The a^4 term in the first entry has genuine order four at rho, while 2azb^2 has order at most three.
Thus the least exponent is exactly -4.
The coordinate permutation interchanging two and three conjugates F_same to its inverse.
The three exponents are therefore invariant under sign change and are precisely (-4,0,4).
The cancellation colength is four, not the zero net determinant order.
Its only disk contribution is 4 log lambda.

Both models have J=0, so the attainment result proves the exact prices 2m(P) and 4m(P).
Here scalar polynomial Jensen gives m(P)=log lambda.

The larger scalar prices can also be verified without using the ledger.
A scalar finite Blaschke product with simple zeros at the three poles cancels F_pull, is unitary on the circle, and has scalar price 2 log lambda.
Repeating it on both coordinates gives total price 4 log lambda.
A fourth-order scalar zero at rho cancels F_same; repeating that scalar product on all three coordinates gives total price 12 log lambda.
The resulting products are disk-holomorphic and circle-unitary, so they are actual admissible contractions.
These comparisons do not assert that those scalar copies are optimal matrix multipliers or audit the ledger's provenance.

### The inherited arithmetic bound and the original Task boundary

For the H=I interface, v4 requires only the same germ identity, constant I, two holomorphic contractions and invertible Q(0).
It does not require Q or U to be rational or integral.
With C_N the first nonzero positive coefficient, vector Parseval gives the two coefficient deficits.
Their difference is C_N Q_0 in the correct multiplication order.
The squared triangle bound and substitution v=Q_0^(-1)w give
\[
 I+C_N^*C_N/4\le Q_0^{-*}Q_0^{-1}.
\]
Determinant monotonicity therefore proves the v4 inequality for every admissible pair.
Passing to the infimum is legitimate because the same fixed lower bound applies to every pair and RP6 has already established the infimum's value.

A nonzero integer C_N has a column of squared Euclidean norm at least one, hence an operator norm at least one.
One eigenvalue of C_N* C_N is at least one and all others are nonnegative.
Thus det(I+C_N* C_N/4)>=5/4, proving RP11.

Neither exact model varies the underlying positive measure log lambda.
For an integer power substitution, the circle covering preserves the mean defining total logarithmic Mahler measure.
It therefore does not produce a positive-measure sequence tending to zero.

The optimization theorem tests a supplied rational integer germ.
It supplies neither that germ for every original positive-measure reciprocal input nor an absolute comparison J(F)+N(F)<=C_tr m(P).
Boundary poles remain included in the actual boundary cost and cancellation construction.
A change of coefficient field or metric supplies no free arithmetic or norm comparison.
These limitations match the original Task rather than solving a weaker normalization of it.

## Verification and source limits

Every substantive step of the v5 local proof, all limiting operations and both model calculations were checked as exact mathematics.
No numerical experiment, symbolic computation or structural validation substitutes for the deductions above.
The matrix factorization theorem remains an explicitly accepted external statement at DR10 U002's recorded edition and applicability depth.
Its original proof, general infinite-dimensional extensions, uniqueness and coefficient-field questions were not newly audited.

The directly checked Nevanlinna passages support the attribution of the singular-value characteristic.
In finite dimension the negative local orders give its pole slope: bounded invertible local factors alter the logarithmic singular-value size by a bounded amount, while the diagonal form contributes exactly delta_a log(1/|z-a|).
This is an applicability deduction from the local proof, not an attribution of RP6 to that source.
The original 1996 article and the complete operator argument were not reviewed.
The Smith--McMillan passage confirms the terminology only.
No exhaustive novelty or historical-priority search is claimed.

Mathematical validity and source applicability are both supported at these stated depths.
No unresolved mathematical or source-applicability gap was identified within the candidate's actual proof obligations.
The historical L133 text is outside this review, while the mathematical scalar-price comparisons are independently checked above.

## Rational price whole-proof finding

The complete frozen C868 v5 Statement and Argument are mathematically supported under their stated hypotheses, with no gap found.
This independent whole-proof finding covers RP1-RP11, all seven proof sections, exact local multiplicities, rational approximation, circle-unitary attainment, both optimal model prices, the inherited Euclidean arithmetic consequence and the original-input limits.
The accepted DR10 theorem and the narrowly checked inherited interfaces retain the source and review boundaries stated above.
No substantive repair was contributed by the reviewer and no candidate proof obligation remains unresolved in this scope.
The uniform supply of suitable integral germs and an original Mahler upper-price comparison remain research obligations.
G0001 remains unresolved; these examples neither solve it nor furnish a vanishing-positive-measure counterexample.
All earlier Claim and review versions keep their own exact scopes.
This finding changes no Claim assessment, strategy, index, execution boundary or repository configuration.
