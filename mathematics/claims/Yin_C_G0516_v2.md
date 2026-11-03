---
author: Yin
---
# Exact inverse rank-energy decomposition and fully optimized collective-column limits

The entire fixed [L281 author proof](../ledger/Yin_L_G0281_v1.md#complete-retained-proof-and-review) is retained below with its complete original hypotheses, finite and limiting quantifiers, costs, source/contribution facts and negative boundaries.
Material organization selects no Task/E and preserves the research pause.
Dated active/pending/adoption wording inside the retained argument describes its original historical context.
The original [R134 complete finding](../audits/reviews/Yin_R_G0134_v1.md#inverse-rank-energy-complete-independent-review) retains its known separate broad-question-only/frozen-direct-input arrangement and independently reviewed target scope; it is not a new independent review of its reviewer's own fixed upstream proofs.

The [preceding fixed Statement](Yin_C_G0516_v1.md#statement) left the integer index and golden constant implicit in its final actual-control paragraph.
This version explicitly restores the original integer v>=0 and phi=(1+sqrt5)/2 there; the entire original proof is unchanged.
The v1 precision limitation remains at its fixed input and is not a defect in the retained original argument.

## Statement

Let P be the actual monic irreducible minimal polynomial of a nonzero algebraic integer alpha, degree d, total logarithmic Mahler measure m>0.
Let r>=1 count ALL exterior conjugates, including both members of every complex pair, and put s=exp(-m).
For the actual normalized finite Blaschke factor Bcal(0)=s, set

    F=Bcal/s=sum_(j>=0)c_j z^j, c_0=1,
    H=1/F=sum_(j>=0)h_j z^j, h_0=1,
    sum_(j>=1)c_j^2=s^(-2)-1,
    sum_(j>=1)j c_j^2=r s^(-2).

The coefficients are real by conjugation symmetry.
F is analytic on a neighborhood of the closed disk; H is used only formally at0 or before its first interior pole, with no inverse boundary square-sum.
For every integer b>=1, let C_b and F_b be the upper b-by-b Toeplitz matrices of h_(j-i) and c_(j-i), respectively.
Then C_bF_b=F_bC_b=I_b and

    D_b=C_b-I_b=R_b+E_b,
    R_b=C_b-s^2 F_b^T, E_b=s^2 F_b^T-I_b,
    rank R_b=min(b,r)=r_b,
    e_b^2:=||E_b||_F^2
      =b(1-s^2)^2+s^4sum_(j=1)^(b-1)(b-j)c_j^2
      =b(1-s^2)-s^4sum_(j>=1)min(j,b)c_j^2,
    0<=e_b^2<=b(1-s^2),
    e_b^2=b(1-s^2)-r s^2+s^4sum_(j>b)(j-b)c_j^2
          =b(1-s^2)-r s^2+o_P(1) as b->infinity.

The final asymptotic is fixed-input only and its nonnegative tail remains at small b.
Neither nonsymmetric summand is asserted positive semidefinite.
For ANY p distinct rows I and q distinct columns J inside the b-window, p>=q>=1, including overlapping or interlaced sets, if ||(D_b)_(I,J)v||>=sigma||v|| for every real v, sigma>=0, then

    (q-r_b)_+ sigma^2<=||(E_b)_(I,J)||_F^2<=e_b^2.

For q>r, sigma^2<=e_b^2/(q-r)<=b(1-exp(-2m))/(q-r).
If q/b>=theta>0 and b>=2r/theta, this is at most2(1-exp(-2m))/theta<=4m/theta.
No lower bound on a singular value is asserted.

For every A>=log2 retain the positive constants

    kappa(A)=min{sqrt(pi/A)exp(-pi^2/log2),
                 exp(-25A/16)(1-2^(-3/2))},
    gamma(A)=kappa(A)/32, K(A)=2+4A^2/gamma(A),
    c_A=1+2exp(-A),
    J_A(sigma)=sup_(lambda>0)
        log[c_A/c_(A+lambda sigma^2)]/[K(A)+lambda/gamma(A)],
    cap_A=log(c_A)/K(A),
    slope_A=2gamma(A)exp(-A)/c_A.

For every such sigma, 0<=J_A(sigma)<=min{cap_A,slope_A sigma^2}.
For EVERY above submatrix and after optimizing all row/column sets, q, certified sigma and lambda inside this ONE limiting b-block,

    (q/b)J_A(sigma)
      <=(r_b/b)cap_A+slope_A e_b^2/b
      <=(r/b)cap_A+slope_A(1-exp(-2m))
      <=[r/(2b)]log2+(1-exp(-2m))/64.

Whenever eta>slope_A(1-exp(-2m)), a certified increment at least eta therefore requires b<=r cap_A/[eta-slope_A(1-exp(-2m))].
This is a necessary window for this specific lower-certificate recipe, not a sufficient or actual entropy bound.
With g(m)=log[2/(1+2^(1-exp(2m)))], there exist universal m_*>0 and epsilon_*>0 such that for0<m<m_* and b>=2r/m the displayed certificate plus g(m) is at most(1-epsilon_*)m.
Indeed its normalized upper expression tends to(5/4)log2+1/32<31/32<1.
This supplies no upper bound on true h_2, full pressure, Mahler measure or other probability mechanisms.

For the ACTUAL finite-position upper digit-coordinate matrix T=R_GS U^(-1), let D_b^(i) be its b-window minus I, and epsilon_i=||D_b^(i)-D_b||_F.
For each fixed P,b, epsilon_i->0 and every actual selected submatrix with minimum singular value at least sigma_i obeys

    (q-r_b)_+ sigma_i^2<=(e_b+epsilon_i)^2,
    (q/b)J_A(sigma_i)
       <=(r_b/b)cap_A+slope_A(e_b+epsilon_i)^2/b.

Every fixed epsilon>0 has an input-dependent all-future i_0(P,b,epsilon); no uniform onset or exchange with growing b is asserted.
Preserve the original independent difference law mu(0)=1/2, mu(+/-1)=1/4 and p_N=Pr(sum_(j=0)^(N-1)eta_j alpha^j=0).
For N<=d, p_N=2^(-N).
For N>d, k=N-d and the exact integer quotient/full Gaussian bound retain2^(-N), all original quadratic rows, T=R_GS U^(-1), and drop only the first d coefficient inequalities.
The pivot product is at most2^(-d)exp[-(N-d)g(m)].
For fixed geometry with limiting sigma>0, A>(log2)exp(2m) and0<epsilon<sigma, after the actual singular-value/exponent onset, every N>d satisfies

    p_N<=2^(-d)exp[-(N-d)g(m)]
      exp[-q J_A(sigma-epsilon)
                    max{0,floor((N-d-i_0)/b)}].

Holding lambda fixed, then taking N->infinity, epsilon->0 and only then the lambda supremum gives h_2>=g(m)+(q/b)J_A(sigma).
No continuity of the optimized supremum or uniform onset is assumed.
Different DISJOINT blocks can add their separately paid losses; repeated rank boundaries and residual energies remain charged.
Arbitrary overlapping choices cannot be summed from one whole-law budget.
Nonunits remain valid at original return-word scope, without importing unit-only state/operator conclusions.
The exact full unshifted pressure identity is left intact and is not evaluated by these bounds.

For every integer v>=0 put r=2^v and phi=(1+sqrt5)/2.
The genuine irreducible family P_r=t^(2r)-t^r-1 has d=2r, m=log phi, s=phi^(-1), c_(jr)=-phi^(-(j-1)) for j>=1 and all other positive c_l=0.
At b=r, E_r=(s^2-1)I_r, e_r^2=r(1-s^2)^2, C_r=I_r, R_r=(1-s^2)I_r and D_r=0.
At b=2r its first-r-row/final-r-column cross-matrix is I_r, whose q=r is not prohibited by the inequality.
For larger windows the rank remains r, the full residual identity above applies, e_b^2/b->1-phi^(-2), and its fixed-input additive correction is-r phi^(-2).
This is a fixed-positive-measure control, not a near-one family or new entropy value.
The present result leaves degree-scale/short-block arithmetic, genuinely different conditional mechanisms, exact pressure evaluation and the unrestricted gap unresolved.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:08 |
| status | open |
| reason | Retain the complete original theorem and unchanged proof with the original integer radical index and golden constant explicitly stated in the new summary; actual written whole-v2 inspection, current formal finding and adoption remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual rank-energy statement](#statement) | All actual positive-measure nonzero algebraic integers/all b and r cases/any distinct intersecting row-column sets/full lambda optimization/finite errors-onsets/original probabilities/disjoint costs/exact radical and every negative scope. |
| argument | [Entire original argument](#argument) | Entire original Sections1--6/equations1--16/reuse/source/contribution/self-check, exact decomposition and full tails, arbitrary-submatrix kernel proof, full optimized certificate, finite original-law transfer and exact actual cancellation. |
| dependency | [Complete direct coefficient budgets](Yin_C_G0461_v1.md#exact-blaschke-two-moment-budget) | Only the full actual direct unweighted and weighted coefficient identities/real conjugate closure/analytic boundary and direct-inverse guard, plus exact fixed-positive-measure radical coefficients. |
| dependency | [Complete finite compression rank](Yin_C_G0475_v1.md#finite-inner-compression-exact-rank) | Actual upper/lower inverse singular-value/positive defect rank min(b,r) for every finite b; no direct budget is imposed on the full inverse. |
| dependency | [Complete collective-column certificate](Yin_C_G0498_v1.md#collective-column-gaussian-loss) | Entire arbitrary intersecting row/column product-law conditioning/relative-entropy constants/lambda family, not independence of rows under the whole Gibbs law. |
| dependency | [Complete original-law transfer](Yin_C_G0498_v1.md#collective-column-original-law) | Exact integer quotient/original2^(-N)/all rows except first d inequalities/finite rational T/pivots/arbitrary outside shifts and disjoint chronological assembly. |
| dependency | [Complete fixed-window limiting transfer](Yin_C_G0498_v1.md#collective-column-limiting-certificate) | Fixed-lag convergence/all-future exponent-singular-value onset/full floor and fixed-input limit; no growing-window or uniform onset assertion. |
| support | [Exact pressure comparison](Yin_C_G0503_v1.md#statement) | Complete unshifted full-expanding REAL form and original collision exponent only, not an evaluation/upper bound on true entropy or a translated actual-block substitution. |
| support | [Actual radical control](Yin_C_G0498_v1.md#actual-inverse-separated-cut-rank) | Exact irreducible dyadic golden family/full rank-r coefficient and cross-block identities at fixed total log phi; no zero-gap sequence. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:11 |
| status | proved |
| reason | Adopt the entire exact rank-energy theorem and unchanged16-equation proof after actual written whole-v2 inspection and the explicit current whole SELF finding. The v1 summary precision limit remains open; original author SELF and R134 independent target scope remain distinct, with all finite-law/onset/optimization costs and no research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual rank-energy statement](#statement) | All actual positive-measure nonzero algebraic integers/all b and r cases/any distinct intersecting row-column sets/full lambda optimization/finite errors-onsets/original probabilities/disjoint costs/exact radical and every negative scope. |
| argument | [Entire original argument](#argument) | Entire original Sections1--6/equations1--16/reuse/source/contribution/self-check, exact decomposition and full tails, arbitrary-submatrix kernel proof, full optimized certificate, finite original-law transfer and exact actual cancellation. |
| dependency | [Complete direct coefficient budgets](Yin_C_G0461_v1.md#exact-blaschke-two-moment-budget) | Only the full actual direct unweighted and weighted coefficient identities/real conjugate closure/analytic boundary and direct-inverse guard, plus exact fixed-positive-measure radical coefficients. |
| dependency | [Complete finite compression rank](Yin_C_G0475_v1.md#finite-inner-compression-exact-rank) | Actual upper/lower inverse singular-value/positive defect rank min(b,r) for every finite b; no direct budget is imposed on the full inverse. |
| dependency | [Complete collective-column certificate](Yin_C_G0498_v1.md#collective-column-gaussian-loss) | Entire arbitrary intersecting row/column product-law conditioning/relative-entropy constants/lambda family, not independence of rows under the whole Gibbs law. |
| dependency | [Complete original-law transfer](Yin_C_G0498_v1.md#collective-column-original-law) | Exact integer quotient/original2^(-N)/all rows except first d inequalities/finite rational T/pivots/arbitrary outside shifts and disjoint chronological assembly. |
| dependency | [Complete fixed-window limiting transfer](Yin_C_G0498_v1.md#collective-column-limiting-certificate) | Fixed-lag convergence/all-future exponent-singular-value onset/full floor and fixed-input limit; no growing-window or uniform onset assertion. |
| support | [Exact pressure comparison](Yin_C_G0503_v1.md#statement) | Complete unshifted full-expanding REAL form and original collision exponent only, not an evaluation/upper bound on true entropy or a translated actual-block substitution. |
| support | [Actual radical control](Yin_C_G0498_v1.md#actual-inverse-separated-cut-rank) | Exact irreducible dyadic golden family/full rank-r coefficient and cross-block identities at fixed total log phi; no zero-gap sequence. |
| review | [Entire current whole SELF](../audits/reviews/Yin_R_G0725_v1.md#current-complete-rank-energy-self-finding) | Entire actual Statement and complete original Argument with all hypotheses/quantifiers/positive-negative controls/source-native limits/full costs and affected interfaces; actual current SELF, not isolated independent replacement or new execution. |

## Complete original argument

<a id="argument"></a>

The retained original proof and its necessary fixed L inputs preserve the actual old review target and historical precision.
All mathematical statements below retain their original scope.

## Complete pressure evaluation and actual expanding-column geometry

### Scope and status

Developing the [G0001 mathematical question](../tasks/Yin_T_G0001_v1.md#contract).
All candidate routes remain active.
The complete author results below are initially self-reviewed only; no independent review, fixed adoption or unrestricted conclusion is asserted.

<a id="inverse-low-rank-reuse-and-domain"></a>
### 1. Reuse and the changed actual geometry question

Date:2026-10-10.
The task is to evaluate actual collective geometry after [L275](../ledger/Yin_L_G0275_v1.md#collective-column-fixed-scope) and the complete original-pressure identity [L277](../ledger/Yin_L_G0277_v1.md#full-expanding-gaussian-fixed-scope).
The latter identifies the exact unshifted exponent but does not evaluate it.
L275's separated-cut rank theorem restricts one particular placement of columns; it leaves interlaced rows/columns and many weak directions open.
This round asks whether extending a window can sustain many well-conditioned columns for THAT quantitative loss mechanism.

The local reuse screen reread L275's whole-law inequality and original finite block/onset transfer, [L268's exact inverse Gram rank](../ledger/Yin_L_G0268_v1.md#finite-inner-compression-exact-rank), and [L264's DIRECT coefficient energy and first moment](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget).
L277 confirms the upper inverse orientation and the actual all-expanding real form, but its pressure evaluation is not assumed.
These existing inputs suffice.
No new source theorem, source-wide audit, computation or J is required.
L264's classical finite-Blaschke attribution and source-inspection limits remain unchanged; its already fixed coefficient equalities are reused rather than newly attributed as original discoveries.

The coordinator supplied the broad actual-pressure/column question only.
Its current translated-pressure D145 was not read or used.
All new low-rank-plus-small-energy decomposition, arbitrary-submatrix consequences, optimized-certificate bounds and their costed limits below are by structural_research for Yin.
The author's earlier L275 theorem and L277 review retain their recorded roles; they are not an independent review of this draft.
No literature-priority claim is made for the elementary matrix manipulations.

Let P be the ACTUAL monic irreducible minimal polynomial of a nonzero algebraic integer alpha, degree d, total logarithmic measure m>0.
Let r>=1 be its number of exterior conjugates, counting both members of every complex pair.
The actual roots are simple, but the consumed compression and coefficient equalities already retain multiplicity at their wider scopes.
Put

    s=exp(-m), 0<s<1,
    F(z)=Bcal(z)/s=sum_(j>=0)c_j z^j, c_0=1,
    H(z)=1/F(z)=sum_(j>=0)h_j z^j, h_0=1.           (1)

Bcal is the normalized actual finite Blaschke factor with Bcal(0)=s.
The c_j,h_j are real by conjugation symmetry.
F is analytic on a neighborhood of the closed disk, whereas H is formal at0 or analytic only up to its first interior pole.
No inverse boundary series or inverse square-sum is used.
L264 supplies exactly

    sum_(j>=1)c_j^2=s^(-2)-1,
    sum_(j>=1)j c_j^2=r s^(-2).                    (2)

The original degree d, neutral conjugates and digit law will remain present in the consuming probability statements; r is not substituted for d there.

<a id="actual-inverse-low-rank-decomposition"></a>
### 2. An exact finite decomposition for every window

For b>=1 let C_b be the upper triangular b-by-b Toeplitz matrix with entries h_(j-i) for j>=i, and let F_b be the corresponding upper matrix of c_(j-i).
Finite convolution proves C_b F_b=F_b C_b=I_b.
Define

    D_b=C_b-I_b,
    R_b=C_b-s^2 F_b^T,
    E_b=s^2 F_b^T-I_b.

Then

    D_b=R_b+E_b,
    rank R_b=min(b,r).                              (3)

The rank statement is exact, not a bound on a chosen separated cut.
To prove it put K_b=C_b C_b^T-s^2 I_b.
L268's compression identity gives K_b positive semidefinite of rank min(b,r), since the upper and lower inverse matrices have the same singular values.
This includes b<r and b=r.
Direct multiplication shows

    R_b=K_b C_b^(-T),

because C_b^(-T)=F_b^T.
Invertibility proves (3).
No assertion that R_b is symmetric or positive semidefinite is made.
Its large entries need not be bounded; the statement isolates them into a rank min(b,r) term.

The complementary matrix E_b is lower triangular.
Its diagonal is s^2-1 and its j-th strict lower diagonal is s^2 c_j, with b-j entries.
Thus its exact squared Frobenius norm is

    e_b^2:=||E_b||_F^2
       =b(1-s^2)^2+s^4 sum_(j=1)^(b-1)(b-j)c_j^2
       =b(1-s^2)-s^4 sum_(j>=1)min(j,b)c_j^2.
                                                               (4)

The last equality follows by inserting the first total in (2); no term of the DIRECT tail is deleted.
In particular

    0<=e_b^2<=b(1-s^2),
    e_b^2=b(1-s^2)-r s^2
                     +s^4 sum_(j>b)(j-b)c_j^2,
    e_b^2=b(1-s^2)-r s^2+o_P(1) as b->infinity.     (5)

The second equality uses the entire weighted total in (2).
Its final sum is nonnegative and tends to0 because it is at most the tail of the convergent first-moment series.
The asymptotic is fixed-input only.
When the expression b(1-s^2)-r s^2 is negative at small b, the retained tail repairs it; no negative upper bound or omitted small-window case is inferred.

Equations(3)--(5) are the changed structure: they separate all potentially large inverse amplification from a residual whose mean square is at most1-exp(-2m), even though H itself has interior poles.
This is NOT applying L264's direct budget to the full inverse.
The rank term R_b is exactly the missing part and is neither discarded nor claimed inexpensive in probability.

One can also see why the separated-cut statement of L275 is compatible with this identity: E_b has no entries strictly above the diagonal, so a cross-matrix between an earlier row interval and a later column interval sees only R_b.
The present theorem additionally controls arbitrary interlaced selections, where E_b no longer vanishes.

<a id="arbitrary-column-rank-energy-obstruction"></a>
### 3. Every row/column selection pays a rank-plus-energy budget

Select any p distinct rows I and q distinct columns J inside the b-window, p>=q>=1.
The two index sets may overlap.
Let M=(D_b)_(I,J), and suppose a certified sigma>=0 satisfies

    ||M v||_2>=sigma||v||_2 for every v in R^q.

Then, with r_b=min(b,r),

    (q-r_b)_+ sigma^2<=||(E_b)_(I,J)||_F^2<=e_b^2.
                                                               (6)

Proof.
The selected R-submatrix has rank at most r_b.
If q>r_b, its kernel contains at least q-r_b orthonormal vectors v_1,...,v_(q-r_b).
On each, M v_a=(E_b)_(I,J)v_a.
Summing their squared norms gives at least(q-r_b)sigma^2 and at most the full squared Frobenius norm of that residual submatrix, by completing these vectors to an orthonormal basis of R^q.
Restricting distinct rows and columns cannot increase the sum of squared entries.
If q<=r_b the left side is0 and the claim is immediate.
This elementary proof uses neither an uninspected low-rank approximation theorem nor independence of any random variables.

For q>r this implies the fully explicit bound

    sigma^2<=e_b^2/(q-r)
          <=b(1-exp(-2m))/(q-r).                    (7)

It applies to EVERY allowed row/column placement, including interlaced sets; it is not confined to a contiguous left/right cut.
For example if q/b>=theta>0 and b>=2r/theta, then q-r>=theta b/2 and

    sigma^2<=2(1-exp(-2m))/theta<=4m/theta.          (8)

Thus in windows long compared with r, positive-density collections of actual inverse columns cannot all have a minimum singular value bounded away from0 as m tends to0.
A large operator norm, many large entries or a large total inverse energy cannot refute (8): such growth can lie in the rank-r component.

There is also an exact finite-position statement.
Let T be the actual rational upper digit-coordinate matrix of L263/L275.
For a b-block beginning at i put D_b^(i)=T_(i+[0,b),i+[0,b))-I.
For fixed P,b, entrywise convergence gives

    epsilon_i=||D_b^(i)-D_b||_F ->0 as i->infinity.

Using the SAME rank term R_b and residual E_b+(D_b^(i)-D_b) in the preceding proof yields

    (q-r_b)_+ sigma_i^2<=(e_b+epsilon_i)^2           (9)

for every selected actual finite submatrix with minimum column singular value at least sigma_i.
For any fixed epsilon>0 there is an all-future i_0(P,b,epsilon) with epsilon_i<=epsilon for every i>=i_0.
No uniform bound for that onset, no exchange with b growing alongside i, and no rank assertion for the full actual finite matrix are being made.

<a id="optimized-collective-certificate-window"></a>
### 4. The entire one-submatrix Gaussian certificate has a paid window

Keep L275's Gaussian exponent bound A>=log2 and its explicit positive constants

    kappa(A)=min{sqrt(pi/A)exp(-pi^2/log2),
                 exp(-25A/16)(1-2^(-3/2))},
    gamma(A)=kappa(A)/32,
    K(A)=2+4A^2/gamma(A), c_A=1+2exp(-A).

For a column singular-value lower bound sigma define the FULL lambda-optimized L275 loss per selected column by

    J_A(sigma)=sup_(lambda>0)
        log[c_A/c_(A+lambda sigma^2)]/[K(A)+lambda/gamma(A)].

This optimization includes its explicit Psi_A, rather than considering only one selected lambda.
Put

    cap_A=log(c_A)/K(A),
    slope_A=2gamma(A)exp(-A)/c_A.

Then

    0<=J_A(sigma)<=min{cap_A, slope_A sigma^2}.      (10)

Indeed the numerator is at most log c_A.
Also its derivative with respect to t=lambda sigma^2 is2exp(-(A+t))/(1+2exp(-(A+t)))<=2exp(-A)/c_A, so the numerator is at most(2exp(-A)/c_A)lambda sigma^2.
Dividing respectively by K(A) and lambda/gamma(A) and taking the supremum proves BOTH bounds.
This is an upper bound on the value of a specified valid lower-loss certificate, not on the actual Gaussian loss.

For ANY submatrix in Section3, its chronologically normalized certified increment consequently satisfies

    (q/b)J_A(sigma)
         <=(r_b/b)cap_A+slope_A e_b^2/b
         <=(r/b)cap_A+slope_A(1-exp(-2m)).           (11)

For q>r_b split q=r_b+(q-r_b), use the cap for the first term and the quadratic bound together with(6) for the second.
For q<=r_b the cap alone proves the same conclusion.
Thus (11) holds after taking a supremum over ALL row selections, column selections, column counts, certified singular-value bounds and lambda>0 inside this ONE actual limiting b-block.
It also holds if the best submatrix is chosen after inspecting every coefficient.
No favorable finite selection is omitted.

All A>=log2 have the safe uniform numerical bounds

    cap_A<=log2/2,
    slope_A<=1/64,

because K>=2, c_A<=2, gamma<1/32, and2exp(-A)/c_A<=1/2.
Therefore

    (q/b)J_A(sigma)
         <=(r/(2b))log2+(1-exp(-2m))/64.            (12)

In particular large windows with r/b->0 and m->0 cannot produce a fixed positive correction by this entire one-submatrix recipe, even when lambda and all selected rows/columns are optimized.
The actual full Gaussian partition can have additional loss; (12) does not bound it above.

For a fixed desired certified increment eta>0, (11) gives the precise necessary window, whenever eta>slope_A(1-exp(-2m)):

    b<=r cap_A/[eta-slope_A(1-exp(-2m))].           (13)

This is a necessary window for the L275 lower-singular-value recipe, not a sufficiency theorem, an exclusion of early exceptional positions, a time bound on the original chain, or a requirement on every possible probability mechanism.
For small m and fixed eta it is O(r), at most O(d).
The fixed-input all-future onset needed to consume a limiting geometry is an ADDITIONAL cost and is not bounded by(13).

At the scale relevant to comparison with the usual actual h_2<=m bound, there is a stronger simple discriminator.
If b>=2r/m, then every selection and A in(12) satisfy

    g(m)+(q/b)J_A(sigma)
         <=g(m)+m(log2)/4+m/32,
    g(m)=log[2/(1+2^(1-exp(2m)))].                 (14)

Direct differentiation gives g(0)=0 and g'(0)=log2, so the right side divided by m tends to(5/4)log2+1/32<1.
For an elementary strict comparison, log2=integral_1^2 dt/t<3/4 by the strict trapezoid inequality for1/t, and hence(5/4)log2+1/32<31/32.
Thus there exist universal m_*>0 and epsilon_*>0 such that for0<m<m_* and b>=2r/m, the displayed lower-rate CERTIFICATE in(14) is at most(1-epsilon_*)m.
A number less than m cannot by itself contradict an independently known h_2<=m.
This is NOT a proof that h_2 is at most that number: the actual rate can exceed a lower bound, and no upper bound on true entropy is obtained here.

The point of (11)--(14) is not optimization of a constant.
They show that even arbitrarily interlaced collective columns cannot use the growing inverse rank-r amplification to create uncharged extensive information in long windows through this criterion.
The remaining candidates include degree-scale windows, additional integer lower constraints, multiple genuinely conditional statistics with a newly justified budget, or arithmetic evaluation of the full L277 expectation.
None is excluded by this theorem.

<a id="rank-energy-original-law-boundary"></a>
### 5. Original law, finite position and disjoint assembly remain distinct

For clarity retain the original iid difference law mu(0)=1/2, mu(+/-1)=1/4 and

    p_N=Pr(sum_(j=0)^(N-1)eta_j alpha^j=0).

For N>d, the exact integer quotient identity and retained full Gaussian upper bound have normalization2^(-N), k=N-d, all original quadratic energy rows, and digit-coordinate matrix T=R_GS U^(-1); only the first d coefficient inequalities were dropped.
No modification to that L275 interface is made.
Its pivot product U_N obeys U_N<=2^(-d)exp[-(N-d)g(m)].
On a selected block of length b beginning at i, its valid incremental logarithmic loss is q J_A(sigma_i), interpreted as the supremum of its separately valid lambda bounds.
Continuity is not needed to retain any fixed lambda; the supremum follows because the same probability upper bound holds for every lambda.
Distinct chronological blocks can be multiplied exactly as in L275, with every finite outside shift retained.

Equation(9) and the same proof of(11) give the FINITE-position certificate-value bound

    (q/b)J_A(sigma_i)
         <=(r_b/b)cap_A+slope_A(e_b+epsilon_i)^2/b. (15)

For a fixed geometry and A>a_infinity=(log2)exp(2m), both the exponent bound and epsilon_i<=epsilon hold after an input-dependent all-future onset.
Repeated b-blocks then retain the complete floor max{0,floor((N-d-i_0)/b)} and all degree/unused-position expenses from L275.
Passing to their fixed-input limiting certificate gives precisely the geometry restricted by(11).
The estimate does not replace a finite error by0 before that limit and does not uniformly control epsilon_i while b changes.

More explicitly, if the chosen limiting submatrix has minimum column singular value sigma>0, fix0<epsilon<sigma.
After its actual all-future singular-value and exponent onset, L275 gives for every N>d

    p_N<=2^(-d)exp[-(N-d)g(m)]
          exp[-q J_A(sigma-epsilon)
                         max{0,floor((N-d-i_0)/b)}].

For N<=d the exact value remains2^(-N).
To pass to the rate without assuming an unproved continuity of an optimized supremum, first hold any lambda>0 fixed in the defining expression for J_A.
Take N to infinity, then epsilon to0, and only then take the supremum in lambda.
Every fixed-lambda expression is continuous in sigma.
This gives h_2>=g(m)+(q/b)J_A(sigma) for the fixed selected geometry and A; letting A decrease to a_infinity can likewise be performed first at each fixed lambda if desired.
The value of this sufficient correction, not h_2 itself, is what(11)--(14) bound above.

One may use different DISJOINT blocks and add their valid logarithmic losses.
Applying(15) to each separately charges at most r_b cap_A per block plus that block's residual energy contribution; it does not erase these repeated boundaries.
Dividing a long window into many short blocks may therefore avoid the single-long-block restriction, but then each short block's actual geometry and its chronological count must be established.
No theorem here rules that out, and no arbitrary overlapping collection can be summed using the same whole-law entropy budget.
Repeated raw rank counts alone do not supply a new probability inequality.

The complete unshifted limiting partition of L277 has exactly the original collision exponent, with its retained input-dependent arithmetic packing costs.
The present upper bounds apply only to one defined LOWER estimate of its loss, and to its translated finite-block use through L275.
They do not modify that exact pressure identity, assign a new upper ceiling to the full loss, or transfer arbitrary translated pressure without proof.
Nonunit inputs stay at original return-word scope; unit-only state/operator theorems remain separate.

<a id="actual-rank-energy-control-and-next-gate"></a>
### 6. An exact actual control and the remaining discriminator

Use the already adopted dyadic golden-radical actual family, with r=2^v,

    P_r(t)=t^(2r)-t^r-1,
    d=2r, m=log phi, s=phi^(-1),
    c_(jr)=-phi^(-(j-1)) for j>=1,
    c_l=0 if r does not divide l, phi=(1+sqrt5)/2.

These are genuine irreducible polynomials with fixed positive total measure.
At the window b=r there is no nonconstant direct coefficient below b, and hence

    E_r=(s^2-1)I_r,
    e_r^2=r(1-s^2)^2,
    C_r=I_r,
    R_r=(1-s^2)I_r,
    D_r=0.                                         (16)

This checks the essential cancellation in the decomposition: a full-rank R at b=r does NOT itself force any useful inverse coupling.
It also explains why the rank contribution cannot be read as information income independently of E.
At b=2r the actual selected first-r-row/final-r-column cross-matrix is I_r, as L275 proves, so its nonzero collective loss remains valid.
Formula(6) has q=r and therefore does not prohibit it.
At all larger b the exact rank term stays r and the full residual energy is exactly(4), with all coefficients in this family explicit.
The per-length limit is1-phi^(-2), and its additive fixed-input correction in(5) is-r phi^(-2).
No new enumeration or floating approximation is used for these equalities.

This actual control is not repeated as evidence of a small-m family or a new entropy value; its purpose is to discriminate an incorrect inference from low-rank amplification alone and verify the boundary at the degree-scale window.
The rational Hadamard model of L275 remains a valid general matrix example, but actual matrices obey(3)--(8), which an arbitrary weak-entry model need not satisfy.

The next concrete open gate is a useful arithmetic or collective loss on windows b=O(r), or on the O(r/m) scale with constants sufficient for the desired comparison, after all finite-position onset and full original-law costs are paid.
One can instead seek an estimate of the actual endpoint weights in the complete positive kernel of L277, or retain lower integer coefficient rows.
The present proof supplies no lower singular-value bound for those shorter windows and no contradiction for actual near-one inputs.
It also does not forbid a changed conditional/multiscale method that avoids this one-submatrix sufficient criterion.
All candidate routes and G0001 remain active and unresolved.

Author self-check covers: upper/lower orientation in R=K C^(-T); all b<r, b=r and b>r rank cases; distinction between direct and inverse energy; every term of the finite Frobenius identity and weighted tail; real kernel dimensions for arbitrary intersecting selections; the q<=r and q>r split; the FULL lambda supremum and its numerical caps; every necessary-window inequality direction; the rate-certificate versus actual-rate distinction; finite error/onset and disjoint-block charges; and the actual cancellation control(16).
No external theorem, source intake, program run, numerical observation or claimed uniform onset is part of this author proof.
A complete separately organized noncontributor review is required before adoption.


Author freeze: 2026-10-10T03:39.
Complete Sections1--6 and equations(1)--(16), including all finite original-law and limiting-certificate costs, are held for separately organized full noncontributor review.
Author self-check found no unresolved mathematical defect.
Scoped material check passed before this final time/status paragraph and is repeated on the frozen file.
No J, numerical experiment or new source was used.
