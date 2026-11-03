---
author: Yin
---
# Exact order-content scaling and a persistent energy floor under full packet operations

Date: 2026-10-12T15:51.
Human author Yin.
Fixed internal extraction under the continuing G0001 authorization.
g0001_review_recovery supplied ALL new mathematics in the complete original D34; g0001_matrix_recovery now authors this exact statement and extraction wrapper and is therefore a contributor to the present artifact.
Root supplied the original broad question only and independently WHOLE-reviewed the actual original22:45 body in R406.
That finding supports the original proof only; the new statement/wrapper requires a separate actual extraction review.
Initial status is proof draft / under review.
The entire original mathematical body, including candidate and reuse material, costs, limits and freeze, is retained below.

## Statement

Fix ANY monic irreducible nontorsion integer-unit polynomial P in Z[t] of original degree d>=2, a root alpha, K=Q(alpha), O0=Z[alpha] and nu=Norm_(K/Q)(alpha) in{+1,-1}.
No reciprocal or root-location restriction is added.
A packet consists of finitely many rational Laurent polynomials f_i, positive rational weights omega_i summing1, and nonzero ACTUAL values u_i=f_i(alpha) in O0.
Require exact complementary covariance

    sum_i omega_i |f_i(exp(i theta))|^2=E>0

for every real theta.
Let T be the ACTUAL common support width, the largest exponent present anywhere minus the smallest.
Make one common monomial normalization when writing ordinary polynomial resultants.
Let q>=1 be the actual least coefficient denominator, F_i=q f_i in Z[t], M the actual least FINAL indexed weight denominator, and m_i=M omega_i positive integers with sum m_i=M and gcd_i m_i=1.
All labels, coefficients and original roots are retained.
Define

    D_i=Norm_(K/Q)(u_i) in Z minus{0},
    Lambda=(1/d)sum_i omega_i log abs(D_i),
    sigma=Lambda-(1/2)log E,
    S_int=sum_i omega_i ||F_i||_2^2=q^2 E,
    I_int=(1/(dM))log abs(product_i Res(P,F_i)^(m_i))
         =log q+Lambda.

Here D_i refers to the values after the declared common polynomial normalization; if values are instead tracked before that normalization, its nu powers below remain explicit.
The full signed identities are Res(P,F_i)=q^d D_i and copied product q^(dM)product_i D_i^(m_i).
No selected-root norm or changed degree replaces them.

**A. Exact admissible common rational scalars for every such packet.**
Expand every actual u_i in the unique integer basis1,alpha,...,alpha^(d-1) of O0, and let g>=1 be the gcd of ALL these integer coordinates.
Let C>=1 separately be the common gcd of ALL coefficients of the integer numerator polynomials F_i.
Actual leastness gives gcd(q,C)=1; C and g are different quantities.
Then

    {r in Q minus{0}: all r u_i in O0}
         =(1/g)(Z minus{0}).

For EVERY nonzero integer z, the legal scale r=z/g gives EXACTLY

    E'=z^2 E/g^2, T'=T, M'=M,
    q'=qg/gcd(qg,abs(z) C),
    D_i'=(z/g)^d D_i,
    Lambda'=log abs(z/g)+Lambda, sigma'=sigma,
    S_int'=(q')^2 z^2 E/g^2.

Its full signed copied norm is (z/g)^(dM)product_i D_i^(m_i), and the copied numerator resultant is (q')^(dM) times that integer product.
Negative scalars retain their odd-degree signs.
In particular the least energy reachable by a legal common rational scalar is E/g^2, attained at r=+/-1/g.
Reduction to E<1 is possible iff E<g^2; reduction to E<=1 iff E<=g^2; and exact E1 iff g/sqrt(E) is a positive INTEGER, equivalently E=g^2/z^2 for a positive integer z.
Rational squareness of E alone is insufficient.

A common monomial t^b preserves g,E,q,M,T and the absolute income, since multiplication by alpha^b is an integer unimodular map of O0.
It multiplies each signed D_i by nu^b and the full copied product by nu^(bM).
Actual order membership is coordinatewise integrality, not merely integrality of a norm.

**B. Closure of a specified content-ideal class above primitive energy one.**
Start with one or several INTEGER Laurent packets on the SAME actual alpha.
For each packet let c>=1 be its common coefficient content and suppose its generated actual value ideal satisfies

    (f_i(alpha): all indexed i)=c O0,
    e=E/c^2>=e0,

where the SAME fixed real number e0>1 works for every starting packet.
No maximal-order, Dedekind or principal-ideal assumption on other ideals is imposed.
For this specified class the value gcd of A is exactly g=c.

EVERY finite expression formed from the following operations remains an integer-coefficient, positive rational-weight complementary packet with nonzero actual O0 values, actual q=1, the SAME content-ideal equality, and e>=e0:

1. Complete indexed tensor products of two existing packets, retaining EVERY ordered pair of labels.
2. Disjoint mixtures of finitely many existing packets with strictly positive rational mixing weights summing1, retaining every label and its actual exponent positions.
3. Coordinate sign changes and one common integer monomial shift of a packet.
4. ANY common nonzero rational scaling that preserves all actual O0 values.

For a tensor, c_new=c_A c_B and e_new=e_A e_B.
For a mixture with component contents c_b and weights lambda_b, c_new=gcd_b c_b and

    e_new=sum_b lambda_b (c_b/c_new)^2 e_b>=e0.

This does not assume that one c_b equals their gcd or that some individual value is a unit.
Signs and a common monomial preserve c,e and the ideal.
Every admissible rational scalar on this class is z/c, with nonzero integer z; it gives integer polynomials z(f_i/c), content abs(z), ideal abs(z)O0, energy z^2 e and unchanged primitive energy e.
Thus each generated packet has E>=e0>1, even after its most favorable legal common rational normalization.
No such finite expression reaches E<=1.

**C. Exact arithmetic copies and physical width through the closure.**
For complete tensor inputs with actual indexed denominators M_A,M_B, multiplicities m_i,n_j and signed norms D_i,H_j,

    M_new=M_A M_B, copies m_i n_j,
    D_ij=D_i H_j, E_new=E_A E_B,
    Lambda_new=Lambda_A+Lambda_B,
    sigma_new=sigma_A+sigma_B,
    product_ij D_ij^(m_i n_j)
      =(product_i D_i^m_i)^(M_B)
       (product_j H_j^n_j)^(M_A),
    T_new=T_A+T_B.

The denominator is ACTUAL least, not merely an upper bound; common primitivity of the multiplicities prevents cancellation.
The width is actual because full indexing retains both extreme support sums, even if different labels attain the endpoints.
Original degree remains d.
Each output has q1 and S_int=E; its coefficient content c and norm factors c^d remain charged.

For a disjoint mixture write its actual normalized mixing weights as lambda_b=a_b/A, where a_b are positive integers, sum a_b=A and gcd_b a_b=1.
For component denominators M_b and multiplicities m_bi put

    L=lcm_b M_b,
    n_bi=a_b (L/M_b)m_bi, H=gcd_(b,i) n_bi.

Then the EXACT final indexed denominator and copies are

    M_new=A L/H, copies n_bi/H,
    E_new=sum_b lambda_b E_b,
    Lambda_new=sum_b lambda_b Lambda_b,
    sigma_new=Lambda_new-(1/2)log E_new
             <=sum_b lambda_b sigma_b.

Every signed norm appears with its displayed new positive copy count.
The mixed common width is the largest component right endpoint minus the smallest component left endpoint in their ACTUAL positions; it is not assigned a component width or an average.
Positive surplus need not survive every mixture.
A legal common scale z/c multiplies copied norms by(z/c)^(dM); a common monomial contributes nu^(bM), and coordinate signs contribute their original degree-d signs.
Further label merging or positive splitting requires recalculating the actual indexed denominator and all copies.

**D. A credited old positive control instantiates the new obstruction at every tensor depth.**
Use C66's EXISTING exact example

    P=t^2-3t+1, d=2, alpha=(3+sqrt5)/2,
    f_+=1+t, f_-=1-t, omega_+=omega_-=1/2.

Its actual q1,M2,T1,E=S_int=2 and signed norms5,-1 give copied product-5, Lambda=I_int=(1/4)log5 and sigma=(1/4)log(5/4)>0.
Since (1-alpha)(2-alpha)=1, its value ideal is O0 and coefficient content is c1.
Hence B applies with e0=2: EVERY declared finite full-tensor/mixing/sign/common-monomial/legal-scaling expression from this packet has q1 and E/c^2>=2, and cannot enter E<=1.

For EVERY integer k>=1 the complete k-th tensor has ALL2^k labels, actual M_k=2^k, q_k=1, EXACT width k, energy2^k and original degree STILL2.
A label with a plus factors has norm5^a(-1)^(k-a), and

    product_labels D_label=(-5)^(k 2^(k-1)),
    Lambda_k=(k/4)log5,
    sigma_k=(k/4)log(5/4)>0.

The all-minus value(1-alpha)^k is an actual O0 unit, so any admissible common rational scalar is an INTEGER.
The proposed energy normalization2^(-k/2) is irrational for odd k.
For even k>=2 it is rational but inadmissible: its all-minus scaled norm is(-1)^k 2^(-k), not an integer.
At k2 the already credited indexed norms25,-5,-5,1 give product625,E4,q1,M4,T2; division by2 formally gives E1 and coefficient q2 but the all-minus value has norm1/4.
This fails the actual O0 hypothesis of the E1 selector.
It is an exact normalization obstruction at T=d with positive starting surplus(1/2)log(5/4), not a contradiction to C71.

Any nonempty finite product of original integer-coefficient atoms is itself a nonzero integer polynomial and has squared coefficient norm at least1.
This elementary spacing observation supplies no unrestricted auxiliary barrier and does not license arbitrary rational divisions or representative changes.

**E. Old full-root bound, attribution and exact limits.**
Every packet above still obeys the already established C10 direct inequality

    sigma<=T m(P)/d

at its ACTUAL final common width and using ALL original roots.
A separately supplied uniform positive surplus at T<=B d would imply m(P)>=sigma/B; this record does not supply such a construction.
C57's complete indexed tensor mechanism, C66's positive quadratic and doubled controls, the generic covariance bound and L229 coefficient-energy estimates are credited prior work.
The new deduction is A's exact order-content scaling gate and B's specified closure obstruction, not a newly discovered binomial packet or tensor identity.

The counterexample has FIXED m(P)=log((3+sqrt5)/2)>0, not m(P) approaching zero.
Increasing k increases width and income together and supplies no improved surplus per width.
C66's separate small-measure obstruction retains its stated scope.
No theorem here says that every packet's ideal is cO0, that the power-basis gcd controls tensor ideals outside B, or that every positive-surplus packet has this normalization obstruction.

Representative changes modulo P, nonprincipal value ideals outside the specified invariant, division by nonrational field elements, arbitrary rational coordinate mixing/paraunitary rotations, coordinate addition, weight-dependent scaling, and operations deleting or reweighting a selected subset of labels lie outside this closure.
They require their own integrality, covariance, width and full-cost arguments.
General all-energy quantitative existence, near-one arithmetic income, height/denominator sufficiency, a uniform gap and G0001 remain unresolved.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T15:57 |
| status | proved |
| reason | Adopt actual original whole R406 and separate actual extraction finding in Yin_R_G0408_v1.md. Fix the all-packet exact common-scaling gate and the specified integer content-ideal energy-floor closure, with complete q/M/sign/width costs and old positive control credited. Only the stated transformation class is excluded; near-one income and unrestricted G0001 remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual original order/root/degree/denominator/width hypotheses, every closure operation and exclusion, signed copied costs and exact fixed-input limits. |
| argument | [Entire retained original body](#argument) | COMPLETE original candidate and reuse material, Sections1--6/equations1--11, both general propositions, full costs, old-example attribution and actual22:45 freeze. |
| dependency | [C10 direct exact-covariance bound](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only the direct original-root polynomial Poisson/reversal bound for a supplied complementary packet at its actual common width, not any reciprocal lifting or profile-existence claim. This is the valid generated heading anchor. |
| dependency | [C66 retained exact controls](Yin_C_G0066_v1.md#argument) | Existing quadratic binomial and complete doubled-tensor norms/energies/positive surplus, directly reread and retained as old mathematical controls, not new examples or near-one counterexamples. |
| support | [C57 indexed tensor antecedent](Yin_C_G0057_v1.md#first-window-tensor-capacity-transfer) | Prior full-label algebra at its actual below-one scope. The present all-energy identities and closure are proved completely in the retained body; no old capacity theorem is silently broadened. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0794_v2.md#all-energy-content-whole-independent-finding) | Root's actual NONCONTRIBUTOR whole reconstruction of the complete original22:45 D34 and its direct interfaces, performed before this wrapper. It does not review or adopt this extraction prospectively. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c78-order-content-actual-extraction-finding) | Entire ACTUAL A--E, complete original preservation and all exact direct interfaces independently inspected after registration; R406 remains original-whole scope. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:47 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain known sufficient independent findings in their original homes and original unknown findings at their actual checking scope. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | Entire A--E, actual original order/root/degree/denominator/width hypotheses, every closure operation and exclusion, signed copied costs and exact fixed-input limits. |
| argument | [Argument: argument](#argument) | COMPLETE original candidate and reuse material, Sections1--6/equations1--11, both general propositions, full costs, old-example attribution and actual22:45 freeze. |
| dependency | [Dependency: direct-exact-covariance-window-inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only the direct original-root polynomial Poisson/reversal bound for a supplied complementary packet at its actual common width, not any reciprocal lifting or profile-existence claim. This is the valid generated heading anchor. |
| dependency | [Dependency: argument](Yin_C_G0066_v1.md#argument) | Existing quadratic binomial and complete doubled-tensor norms/energies/positive surplus, directly reread and retained as old mathematical controls, not new examples or near-one counterexamples. |
| support | [Support: first-window-tensor-capacity-transfer](Yin_C_G0057_v1.md#first-window-tensor-capacity-transfer) | Prior full-label algebra at its actual below-one scope. The present all-energy identities and closure are proved completely in the retained body; no old capacity theorem is silently broadened. |
| support | [Support: all-energy-content-whole-independent-finding](../audits/reviews/Yin_R_G0794_v2.md#all-energy-content-whole-independent-finding) | Root's actual NONCONTRIBUTOR whole reconstruction of the complete original22:45 D34 and its direct interfaces, performed before this wrapper. It does not review or adopt this extraction prospectively. |
| review | [Current isolated finding](../audits/reviews/Yin_R_G0794_v2.md#g78-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:47 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The [original entire D34 freeze](#all-energy-transfer-limits-and-author-freeze) is extraction ancestry, not an additional proof dependency.
Its complete saved source has24855 characters,190 lines and7 explicit anchors.
The ENTIRE body follows with only the duplicate author/framework front matter removed and the original first title demoted by one hash.
Ordinary line-ending and separating/terminal blank-line normalization is allowed.
Every original substantive paragraph, formula, explicit anchor, candidate/failure/reuse statement, source limit, contribution disclosure and freeze is retained.
Existing ../claims/ and ../ledger/ links remain valid from this directory and require no rebasing.
No missing proof is replaced by a summary.

Original g0001_review_recovery remains the proof author.
Root contributed the broad question only, wrote the actual independent original R406, and may separately inspect this newly authored extraction.
g0001_matrix_recovery contributes this wrapper only; its other mathematical work and previous review/extraction roles supply no independent certification of the new artifact.
Historical pending-review prose in the preserved22:45 body retains its historical date; the present decision states the extraction's actual pending review.

C50/C71/C77 compare the old energy domains; C14 and L193 record the original elementary precautions and a different content question.
They are not additional hidden premises of the directly proved gcd/ideal closure.
C10's accepted Poisson attribution/source-access limits remain unchanged, and no external theorem or new source acquisition is introduced.

Structural checks and exact body preservation do not constitute mathematical acceptance.
This allocation makes no adoption, D retirement or native mathematical run.

## Argument

## Testing all-energy packet normalization against actual order content

Date: 2026-10-12T14:35.
Human author Yin.
New AUTHOR investigation by g0001_review_recovery.
Root assigned the broad all-energy packet bottleneck and supplied no formula, candidate or proof.
This author previously reviewed C50/C71/C77-related interfaces and now contributes new research; those review roles do not independently certify the present argument.
No native mathematical program, source acquisition or external theorem is proposed.

## Responsible question

The requested domain consists of all finite positive rational-weight complementary packets with arbitrary E>0, actual nonzero O0 values, actual coefficient denominator q and FINAL indexed weight denominator M.
The interest is uniform positive FULL surplus at degree-linear common width, with every original root and signed norm charged.
Existing fixed-input capacities or a restated L229 corollary would not resolve that bottleneck.

## Bounded reuse and the proposed residual transfer question

The actual [L229 coefficient-energy estimate](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) already bounds a full original resultant by its coefficient norm and explicit angular/radial error.
Averaging that inequality is existing direct reuse, not a new main result here.
[C50](Yin_C_G0050_v1.md#statement) gives the actual denominator obstruction at E<1 without requiring complementary lags.
[C71](Yin_C_G0071_v1.md#statement) gives the finite atom/cross-product selector at EXACT E1, expressly excluding E>1.
[C66](Yin_C_G0066_v1.md#statement) gives arbitrary-energy estimates for a specified complete independent-sign product family, including only ACTUALLY admissible rational scalings.
[C77](Yin_C_G0077_v1.md#statement) covers a legal E1 rank-one word from monomial seeds, not every complementary packet or every energy.
Those results and their original source limits remain credited.

A bounded G-only search for common scalar normalization, tensor/scalar transfers, integer energy and unit atoms found these scopes, the existing common-monomial/rational-integrality precautions, and the familiar fixed quadratic input.
No claim of a new binomial packet or new tensor identity is made.
No exhaustive literature novelty search is intended for the elementary content calculation proposed below.

<a id="all-energy-normalization-responsible-candidate"></a>
## Candidate before proof

Test the tempting transfer that a positive-surplus packet at arbitrary E>0 can be reduced to the C50/C71 energy range by finite complete indexed tensor powers, positive rational mixing and a legal common rational scaling.
The proposed diagnostic must retain actual O0 membership, not merely an algebraic covariance normalization, and must use a genuine positive-surplus packet rather than a zero-income constant control.
A useful stronger obstruction would persist after tensor powers even when their energies become rational squares, and would separate common actual value content from coefficient height.

The next steps are to specify this transformation class exactly, calculate the actual rational scaling set in the original power basis, and either prove an admissible normalization or preserve an exact counterexample with all q/M, signed norms and widths.
If the old interfaces already settle this entire question, the responsible account will state that reuse and stop duplicating it.
This allocation asserts no new theorem, near-one family, unrestricted obstruction or independent acceptance.


<a id="all-energy-reuse-resolution"></a>
## 1. Resolved old interfaces and the exact proposed transfer

Further bounded reading located the EXACT positive quadratic binomial and its doubled tensor already in [C66's retained controls](Yin_C_G0066_v1.md#argument): P=t^2-3t+1, norms5,-1, E2, and four indexed norms25,-5,-5,1 at E4.
They are prior mathematics, NOT a new construction here.
The old [C57 indexed product argument](Yin_C_G0057_v1.md#first-window-tensor-capacity-transfer) already supplies the finite multiplication and full q/M/copy mechanism in its stated below-one domain; its algebraic mechanism also has the explicitly adopted E1 use in C71.
The all-energy finite identities needed below are verified directly rather than pretending that the old capacity statement already asserts a normalization theorem.
[C14's rational monomial integrality argument](Yin_C_G0014_v2.md#statement) supplies the familiar rational-algebraic-integer precaution.
[L193](../ledger/Yin_L_G0193_v1.md#resultant-content-collapse-fixed-scope) concerns a DIFFERENT resultant-versus-polynomial-content loss; no near-one claim is inherited from its fixed-measure family.

The general exact complementary estimate sigma<=Tm(P)/d is already the [C10 direct bound](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality), for ALL E>0.
Thus uniform positive sigma at T<=B d would itself give m>=sigma/B.
Repeating that implication or averaging L229 is not a new quantitative construction or obstruction.
The missing issue is how to obtain or exclude actual integral-value packets with such surplus.
In particular one cannot reduce E>1 to E1 merely by dividing by sqrt(E): that number might be irrational, and even a rational scalar must preserve every actual O0 value.

The specific transfer tested here is: starting from a positive-surplus complementary packet, use a finite expression of COMPLETE indexed tensor products, disjoint positive rational mixtures, coordinate sign changes, common monomial shifts and admissible common nonzero rational rescalings, to reach E<=1.
Every original label is retained in tensors and mixtures.
No deletion, replacement of a value by another representative, coordinate addition, rational paraunitary rotation, weight-dependent coordinate scaling or division by a nonrational field element is included.
Common width is remeasured after every actual operation; a mixture does not identify the widths of its components.

The new result below is a counterexample to THIS scalar/tensor/mixing transfer, together with an exact general rational-scaling gate.
It is not a theorem that every positive-surplus packet has this obstruction, nor a new upper Mahler bound or a near-one family.

<a id="all-energy-actual-content-scaling-gate"></a>
## 2. An exact all-packet rational-scaling gate

Fix ANY actual monic irreducible nontorsion integer-unit polynomial P of original degree d>=2, alpha a root, K=Q(alpha), O0=Z[alpha] and nu=Norm_K(alpha) in{+1,-1}.
Consider a finite rational Laurent packet f_i with positive normalized rational weights omega_i, nonzero actual u_i=f_i(alpha) in O0, exact constant covariance E>0, actual common width T and coefficient denominator q.
Normalize once by a common monomial when ordinary polynomials/resultants are used.
Let M be the ACTUAL least FINAL indexed weight denominator and m_i=M omega_i positive integers, with sum m_i=M and gcd_i m_i=1.
Write

    F_i=q f_i in Z[t], D_i=Norm_(K/Q)(u_i) in Z minus{0},
    Lambda=(1/d)sum_i omega_i log abs(D_i),
    sigma=Lambda-(1/2)log E, S_int=q^2 E.                 (1)

The original d and every sign/content/copy are retained.
The usual exact identities are Res(P,F_i)=q^d D_i, copied product q^(dM)product_i D_i^(m_i), and I_int=log q+Lambda.
No approximation or source theorem is used for these algebraic identities.

Expand EACH actual u_i in the unique integer power basis1,alpha,...,alpha^(d-1), and let g>=1 be the gcd of ALL their integer coordinates.
These coordinates are not the original coefficient vectors of f_i.
Monicity and minimality make this an actual Z-basis of O0, and the unit hypothesis permits Laurent evaluation in it.
Let C>=1 instead be the common gcd of ALL coefficients of the integer polynomials F_i.
Actual leastness of q implies gcd(q,C)=1, but C and g are otherwise different data.

**Proposition 1.**
The complete set of admissible common nonzero RATIONAL scalars is

    {c in Q minus{0}: every c u_i in O0}=(1/g)(Z minus{0}). (2)

For c=z/g, z a nonzero integer, the exact resulting quantities are

    E'=z^2 E/g^2, T'=T, M'=M,
    q'=qg/gcd(qg,abs(z) C),
    D_i'=(z/g)^d D_i,
    Lambda'=log abs(z/g)+Lambda, sigma'=sigma,
    S_int'=(q')^2 z^2 E/g^2.                              (3)

The signed copied product of the D_i' is (z/g)^(dM)product_i D_i^(m_i), and the signed copied numerator resultant is (q')^(dM) times that integer product.
The scalar sign in odd original degree is not removed before taking absolute income.

**Proof.**
Membership in O0 is coordinatewise integrality in the displayed basis.
Since every coordinate is a multiple of g, cg integer is sufficient.
Conversely an integer Bezout combination of the coordinates equals g, so if every scaled coordinate is integral, cg is an integer.
This proves(2), without replacing order membership by an integer norm test.
The collected coefficients after scaling are z times those of F_i divided by qg.
Their actual common denominator is qg divided by gcd(qg,abs(z)C), proving q' in(3), with no inferred equality to a preliminary denominator.
Covariance, width and weights give the first line; degree-d norm homogeneity gives the rest.
All u_i remain nonzero under nonzero c.

Consequently the LEAST energy reachable by an admissible common rational scalar is EXACTLY

    E_min,scalar=E/g^2, attained at c=+/-1/g.             (4)

A scalar reduction to E<1 exists iff E<g^2; one to E<=1 exists iff E<=g^2.
Exact E1 is possible iff g/sqrt(E) is a positive INTEGER, equivalently E=g^2/z^2 for some positive integer z.
Rational squareness alone is insufficient.
The general criterion uses the actual value content; a large coefficient denominator or large coefficient norm cannot replace g.
This proposition is an elementary all-packet scaling calculation, not an L229 estimate or a claimed new integral-basis theorem.

A common monomial t^b multiplies every value by the actual O0 unit alpha^b.
Its multiplication matrix in this power basis is unimodular over Z, so it preserves g as well as E,q,M,T.
It multiplies D_i by nu^b and the copied product by nu^(bM).
Thus the gate is compatible with the single common polynomial normalization already charged in(1).

<a id="integer-ideal-energy-closure"></a>
## 3. A transformation class with a persistent primitive energy floor

For a finite INTEGER Laurent packet, let c>=1 be its common coefficient content, the gcd of all coefficients across all labels.
Impose the following additional, EXACT property on its actual values:

    I=(f_i(alpha): all i) in O0 equals c O0.             (5)

Here the ideal means finite sums sum_i a_i f_i(alpha), a_i in O0.
This is a statement in the actual monogenic order, with no assumption that it is maximal or Dedekind.
Dividing all coefficients by c gives integer Laurent polynomials whose values generate the unit ideal.
In particular their power-basis coordinates have gcd1: an integer n>1 dividing all of them would make the generated ideal lie in nO0, which does not contain1.
Thus the g of Section2 is exactly c on this class.

Define e=E/c^2, the energy after maximal common INTEGER content is removed, and suppose e>=e0 for some fixed real e0>1.
This is a measured energy, not a free normalization of arbitrary packets.

**Theorem 2.**
Starting with one or several packets satisfying(5) and e>=e0>1, every finite construction from the following operations again has integer coefficients, actual q=1, property(5), and e>=e0:

1. Complete indexed tensor products of two existing packets on the SAME actual alpha.
2. Disjoint mixtures of finitely many existing packets with strictly positive rational mixing weights summing1, keeping every indexed label and its actual position.
3. Coordinate sign changes and a common integer monomial shift.
4. ANY common nonzero rational scaling that keeps ALL actual values in O0.

Every intermediate packet remains finite, rational-weight, complementary and nonzero in O0.
In particular its actual E>=e0>1, even AFTER its most favorable admissible common rational normalization.
Thus no construction in this class reaches E<=1.

**Proof: tensor.**
For input contents c_A,c_B, the integer coefficient content of ALL products f_i h_j is exactly c_A c_B.
After dividing by this product, the coefficient collections of each input have gcd1.
For every rational prime p choose a polynomial from each collection that is nonzero modulo p; their product is nonzero in F_p[t,t^-1], since this ring has no zero divisors.
Therefore p cannot divide all product coefficients, proving the exact content assertion.
No factorial or per-label content is discarded.

The ideal of all value products is exactly I_A I_B: expanding finite sums proves both inclusions directly in O0.
Equation(5) therefore gives c_A c_B O0.
Covariance and energy multiply, so e_new=e_A e_B>=e0^2>=e0.
Every actual product value is nonzero because K is a field.
The physical common width is EXACTLY T_A+T_B: extreme product coefficients are nonzero, and full indexing retains labels realizing both extreme sums, even when different labels witness the two endpoints.

**Proof: mixture.**
If the component contents are c_b, the disjoint union's coefficient content is c=gcd_b c_b.
Its value ideal is the sum of c_b O0, which equals cO0 by the ordinary integer Bezout identity.
If lambda_b>0 are its normalized mixing weights, covariance and energy give

    e_new=(sum_b lambda_b E_b)/c^2
         =sum_b lambda_b (c_b/c)^2 e_b>=e0.             (6)

No positive lower bound on the individual weights is needed.
No assertion is made that a component of least content c must occur; gcd(2,3)=1, for example, is handled by the ideal sum rather than by assuming a unit-valued label survives.

**Proof: signs, common monomial and rational scaling.**
Signs preserve coefficient content and the value ideal.
A common monomial permutes coefficient positions and multiplies the ideal by an O0 unit, so(5), E and e persist with its full norm sign.
For a legal scalar, Section2 with g=c gives scalar z/c.
The new polynomials are z(f_i/c), hence are INTEGER with content abs(z).
Their ideal is zO0=abs(z)O0, and their energy is z^2 e.
The new normalized energy is still e.
This includes rational scalings that undo a previous integer multiplication, not just integer scalars.

Each permitted operation preserves the asserted properties, proving every finite expression by induction.
The argument does not require the existence of a unit-valued atom in every generated mixture.
It uses the actual ideal equality, which is the stronger invariant needed after mixing differently scaled packets.

<a id="all-energy-closure-complete-costs"></a>
## 4. Complete arithmetic and physical costs of the closure

The tensor and mixture formulas are finite algebra for every E>0; the old C57/C71 formulas are credited antecedents, not newly claimed analytic results.
All outputs in Theorem2 are coefficient-integral with actual q1, so their paid integer coefficient energy is their actual E.
Their common content c is not dropped: energy is c^2 e, and every full norm and resultant includes c^d.

For two packets with ACTUAL final indexed denominators M_A,M_B, copies m_i,n_j and full signed norms D_i,H_j, a COMPLETE tensor has

    omega_ij=(m_i/M_A)(n_j/M_B),
    M_new=M_A M_B, copies m_i n_j,
    D_ij=D_i H_j, E_new=E_A E_B,
    Lambda_new=Lambda_A+Lambda_B,
    sigma_new=sigma_A+sigma_B,
    product_ij D_ij^(m_i n_j)
       =(product_i D_i^m_i)^(M_B)
        (product_j H_j^n_j)^(M_A).                       (7)

Leastness of M_new follows because gcd_i m_i=gcd_j n_j=1: for any prime one can choose both multiplicities not divisible by it, so no common cancellation exists in their full product collection.
Actual q remains1 here; this is not a new claim that an arbitrary subset has the complete tensor denominator.
Every norm remains in the original field and degree d.

For a mixture, write its actual rational mixing weights as lambda_b=a_b/A, with positive integers a_b summing A, gcd_b a_b=1.
Put L=lcm_b M_b and

    n_bi=a_b (L/M_b) m_bi, H=gcd_(b,i) n_bi,
    M_new=A L/H, copies n_bi/H,
    E_new=sum_b lambda_b E_b,
    Lambda_new=sum_b lambda_b Lambda_b,
    sigma_new=Lambda_new-(1/2)log E_new.                 (8)

These are the ACTUAL reduced indexed weights, not an assumed product bound.
Every signed norm appears to its displayed new positive copy count.
The actual common width is max over all component right endpoints minus min over all left endpoints.
It need not equal a component width, sum or average, and is remeasured.
Jensen's inequality also gives sigma_new<=sum_b lambda_b sigma_b, because log E_new>=sum_b lambda_b log E_b; this ordinary concavity consequence supplies no missing positivity.
Theorem2 does not assert that every mixture preserves positive surplus.

A common scale z/c multiplies each original norm by(z/c)^d and the copied product by(z/c)^(dM); its integer-valuedness follows from(5), not an omitted division.
It changes Lambda by log abs(z/c) and energy by(z/c)^2, preserving full surplus.
Its new q is1 because the coefficient content c is also present.
A common shift t^b contributes nu^b per norm and nu^(bM) to the copied product, while preserving E and physical width.
Coordinate signs similarly contribute their degree-d signs.
Arbitrary positive splitting or merging after these declared operations requires recalculation of the actual indexed denominator and does not alter the weighted mathematical quantities.

Every generated packet still satisfies the OLD direct estimate sigma<=Tm(P)/d with its ACTUAL final width.
None of these exact identities controls T or M uniformly over an unknown construction.
There is no interpretation of a tensor numerator as free income or of coefficient integrality as an all-input gap.

<a id="positive-all-energy-normalization-counterexample"></a>
## 5. The actual positive control and failure at every tensor depth

Use precisely C66's existing fixed positive control

    P=t^2-3t+1, d2, alpha=(3+sqrt5)/2,
    f_+(t)=1+t, f_-(t)=1-t, omega_+=omega_-=1/2.          (9)

The discriminant5 is nonsquare, so P is irreducible.
Its two roots are alpha>1 and alpha^-1, hence it is an original nontorsion integer unit and m=log alpha>0.
On the circle the exact covariance is2.
Actual q1, common width T1, FINAL M2 and copies1,1 give

    D_+=5, D_-=-1,
    copied signed resultant product=-5,
    E=S_int=2, Lambda=I_int=(1/4)log5,
    sigma=(1/4)log(5/4)>0.                              (10)

These values and positivity are already proved in C66 and are rechecked here only to instantiate the new transfer obstruction.
The constant coefficients1 give common coefficient content c1.
The value1-alpha is an O0 unit: from alpha^2=3alpha-1 one checks

    (1-alpha)(2-alpha)=1.

Thus the values generate O0, verifying(5).
Theorem2 applies with e0=2.
Every finite construction from this packet by the specified full tensor/mixing/sign/common-monomial/legal-rational-scaling operations has q1 and E/c^2>=2.
It therefore cannot reach E<=1.
This is a genuine positive-surplus starting example, not an inflated zero-income constant packet, and the obstruction survives arbitrarily deep finite operations even with arbitrary positive rational mixture weights.

For transparency, the complete k-th tensor itself has ALL2^k labels, true M_k=2^k, q_k=1, width EXACTLY k, energy2^k and original degree STILL2.
A label with a plus factors and k-a minus factors has signed norm5^a(-1)^(k-a).
The full copied quantities are

    product_labels D_label=(-5)^(k 2^(k-1)),
    Lambda_k=(k/4)log5,
    sigma_k=(k/4)log(5/4)>0.                             (11)

The all-minus label is the actual unit(1-alpha)^k, so its presence alone forces any admissible common rational scalar to be an integer.
A proposed c=2^(-k/2) covariance normalization is irrational for odd k.
For even k>=2 it is rational but not admissible: the all-minus scaled value has norm(-1)^k 2^(-k), which is not an integer.
Thus a rational-square energy does not repair the order-membership obstruction.

At k2, already C66's four indexed norms are25,-5,-5,1, their product625, energy4, q1,M4,T2.
Dividing every polynomial by2 formally gives E1 and coefficient q2, but the all-minus value has norm1/4 and is not an algebraic integer.
This is an explicit exact failure of the E>1-to-E1 transfer at a degree-linear window T=d, with positive starting surplus(1/2)log(5/4).
It does not contradict C71 because the normalized packet fails its actual O0 premise.

Nor can a C71-style selector be blindly extended by choosing just a finite nonempty product of original integer-coefficient atoms and expecting coefficient energy<1.
Every such product is a nonzero integer polynomial, whose squared coefficient norm is a positive integer and hence at least1.
This observation is elementary integer spacing, not a new unrestricted auxiliary barrier.
Arbitrary rational divisions, new value representatives or coordinate transformations may change that situation and are outside the proved closure.

<a id="all-energy-transfer-limits-and-author-freeze"></a>
## 6. What this resolves and what remains open

The all-packet result here is the EXACT common rational-scaling criterion(2)--(4), with actual q/M, value-content, coefficient-content and full signed norms kept separate.
The specific new negative theorem is the closure in Theorem2: a coefficient-integral packet whose values generate its content ideal and whose normalized energy exceeds one cannot be moved into E<=1 by the stated finite operations.
It supplies a concrete failure of transferring arbitrary-energy positive-surplus questions wholesale into the E1 selector.
The numerical binomial/tensor controls, generic covariance formulas and L229 source theorem are credited old inputs or elementary algebra, not repeated as new discoveries.

The fixed input has m=log((3+sqrt5)/2), NOT m approaching zero.
Its balanced sign product is already subject to C66's separate small-measure obstruction, so the present positive control neither disproves an exclusively near-one theorem nor supplies the requested uniform positive surplus over unrestricted inputs.
Growing k raises width as well as income and preserves surplus per width.
General all-packet quantitative existence, near-one norm income and height/denominator sufficiency remain unresolved.

No claim is made that every actual value ideal is cO0 or that power-basis content alone determines tensor-ideal behavior outside(5).
Nonprincipal ideals, integral representative changes modulo P, new division gates, arbitrary rational coordinate mixing, nonproduct/reweighted operations that delete labels, and other packet constructions may escape this closure.
They require their own actual integrality and full cost arguments.
No native search, new source theorem or external acquisition was used.

Author self-check reconstructed every rational-coordinate and coefficient gcd, least denominator, true sign, full tensor norm copy, mixture weight reduction, ideal product/sum, coefficient-content primitivity argument, common physical width and the exact quadratic unit inverse.
The strongest theorem is developed wholly by g0001_review_recovery; root supplied only the broad research question and receives the result.
A different noncontributor must review the ENTIRE original allocation/reuse history and Sections1--6/equations1--11 before fixed extraction or adoption.
This is author work, not independent acceptance.

No prior proof was edited.

2026-10-12T14:45: the entire author freeze includes the original candidate and reuse material, Sections1--6/equations1--11, all existing-result attribution, the exact general scaling proposition, complete closure theorem and costs, fixed-input counterexample and remaining scope.
The bounded structural check passed with checked9.
No independent review has yet occurred.

## Historical assessments

<a id="decision-initial"></a>

### Historical assessment initial

| Field | Value |
| --- | --- |
| date | 2026-10-12T15:51 |
| status | proof draft |
| review-status | under review |
| reason | Register the precise all-packet rational-scaling gate, the specified content-ideal energy-floor closure, complete arithmetic/physical costs and the credited positive control at every tensor depth. The complete original22:45 D34 is retained. R406 independently inspected that original body only; this actual new statement/wrapper awaits separate extraction review and is not adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual original order/root/degree/denominator/width hypotheses, every closure operation and exclusion, signed copied costs and exact fixed-input limits. |
| argument | [Entire retained original body](#argument) | COMPLETE original candidate and reuse material, Sections1--6/equations1--11, both general propositions, full costs, old-example attribution and actual22:45 freeze. |
| dependency | [C10 direct exact-covariance bound](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only the direct original-root polynomial Poisson/reversal bound for a supplied complementary packet at its actual common width, not any reciprocal lifting or profile-existence claim. This is the valid generated heading anchor. |
| dependency | [C66 retained exact controls](Yin_C_G0066_v1.md#argument) | Existing quadratic binomial and complete doubled-tensor norms/energies/positive surplus, directly reread and retained as old mathematical controls, not new examples or near-one counterexamples. |
| support | [C57 indexed tensor antecedent](Yin_C_G0057_v1.md#first-window-tensor-capacity-transfer) | Prior full-label algebra at its actual below-one scope. The present all-energy identities and closure are proved completely in the retained body; no old capacity theorem is silently broadened. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0794_v2.md#all-energy-content-whole-independent-finding) | Root's actual NONCONTRIBUTOR whole reconstruction of the complete original22:45 D34 and its direct interfaces, performed before this wrapper. It does not review or adopt this extraction prospectively. |
