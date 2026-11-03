---
author: Yin
---
# Uniform all-height binary weighted delay rigidity from two integral auxiliaries

Date: 2026-10-12T16:58.
Human author Yin.
Fixed internal extraction under the continuing G0001 instruction.
Root is the sole author of the new arbitrary-height D40 proof, including the second integral auxiliary, integer coefficient margin, complete local branches and word induction.
g0001_matrix_recovery independently WHOLE-reviewed the actual00:44 original in R311 and NOW authors this exact statement/extraction wrapper, becoming a contributor to this new artifact.
R311 supports the original whole proof only; a different noncontributor must actually review this extraction.
Initial status is proof draft / under review.
The complete original initial candidate, failed coarse estimates, special-H test, proof, costs, controls and freeze are retained below.

## Statement

Fix an ACTUAL monic irreducible nontorsion integer-unit polynomial P of original degree d>=2, a root alpha, K=Q(alpha), O0=Z[alpha], nu=Norm_K(alpha) in{+1,-1} and total logarithmic measure m=m(P)>0.
Reciprocity is not required.
Every norm uses ALL d original embeddings.
For rational Laurent matrices, star is transpose together with t->t^-1.

Keep the actual accepted function and constants

    c0=log2/4, h0=c0 exp(-20),
    b0(u)=max{u,sqrt(u/c0)log(sqrt(c0/u))},
    epsilon(u)=min{1,15sqrt(b0(u))+4u}, 0<u<=h0,
    K0=c0/[2*36^8*5^64]>0,
    Ferr(u)=1+epsilon(u)+8u.

The functions used here are increasing on that domain.
C74's resolved R1 numerical interface gives

    K0<h0/2, K0<1/20,
    exp(2K0)[4/5+8epsilon(K0)+32K0]<1,
    5^8[epsilon(2K0)+12K0]<1.

No old dimension/multiplicity word theorem is used to supply the new uniform conclusion.

**A. Arbitrary primitive binary factor and TWO actual integral values.**
Let r,s be positive coprime integer relative weights and(x,y) a primitive integer direction with BOTH coordinates nonzero.
Define

    S=r*x^2+s*y^2, c_g=gcd(abs(r*x),abs(s*y)),
    A=r*x/c_g, B=s*y/c_g, gcd(abs(A),abs(B))=1,
    L=A*x+B*y=S/c_g>0,
    Pi=(1/L)[[x*A,x*B],[y*A,y*B]],
    U_k=Id-Pi+t^k Pi, k in Z minus{0}.

The four numerator entries have collective gcd1, so L is the ACTUAL Laurent matrix coefficient denominator for k!=0.
It need not be the output packet's coefficient denominator.
The identities Pi^2=Pi, Pi^T diag(r,s)=diag(r,s)Pi and U_k^star diag(r,s)U_k=diag(r,s) hold, and det U_k=t^k.

For any input f(alpha),g(alpha) in the SAME O0, put delta=alpha^k-1.
Both output values are integral if and only if

    z=delta*(A*f(alpha)+B*g(alpha))/L in O0.

Indeed their increments are x*z and y*z, and gcd(x,y)=1.
Whenever this holds, the SECOND value

    w=delta*(y*f(alpha)-x*g(alpha))/L

also belongs to O0, because

    delta*f(alpha)-x*z=B*w,
    y*z-delta*g(alpha)=A*w,

and gcd(A,B)=1.
These are whole-order integer Bezout implications, without a maximal-order or selected-residue substitution.
Output nonvanishing is a separate requirement.

When z,w are both nonzero, their product gives the complete original norm floor

    1<=abs Norm_K(z*w)^(1/d)
      =abs Norm_K(delta)^(2/d)
       *abs Norm_K(A*f(alpha)+B*g(alpha))^(1/d)
       *abs Norm_K(y*f(alpha)-x*g(alpha))^(1/d)/L^2.

Before taking absolute values the exact signed product has denominator L^(2d), and delta appears twice.
Original monomial and negative-delay unit signs remain; no degree of a powered unit replaces d.

**B. Uniform integer coefficient margin and its constant-input version.**
Conjugate the coordinates by sign x and sign y for estimates, then restore them.
Put

    X=abs x, Y=abs y, a=abs A, b=abs B,
    L=aX+bY,
    R=sqrt((a^2+b^2)(X^2+Y^2))/L^2.

For ALL positive integers a,b,X,Y,

    R<=1/4+1/L^2,
    L>=3 implies R<=13/36.

The exceptional L=2 forces a=b=X=Y=1 and, in A's primitive weighted setting, r=s=1.
For epsilon,eta in{+1,-1}, whenever both factors are nonzero, the separate collected-constant estimate is

    abs((a*epsilon+b*eta)(Y*epsilon-X*eta))/L^2<=1/4.

The first bound follows from L^2+(aY-bX)^2=(a^2+b^2)(X^2+Y^2) and abs(aY-bX)<=L^2/4-1; the second uses positivity/integrality to bound the appropriate product u*v by L^2/4.
Neither bound assumes a lower bound on normalized weights or a bound on direction heights.

**C. Uniform local TRUE-polynomial classification.**
Take CLEAN signed monomial inputs

    f=epsilon*t^(a0), g=eta*t^(b0),
    epsilon,eta in{+1,-1}, h=abs(a0-b0),
    U=(h+abs(k))*m/d.

Require BOTH output values under A to be NONZERO elements of O0.
If U<=K0, EXACTLY one of the following polynomial identities and actions occurs:

1. A*f+B*g=0: the two selected coordinates remain unchanged.
   Their exponents coincide, their direction-aligned signs are opposite, and the primitive weights satisfy r=abs y,s=abs x.
   Unequal and arbitrarily large direction heights are allowed in this cancellation branch.
2. y*f-x*g=0: the two selected coordinates acquire the common factor t^k.
   Their exponents coincide, abs x=abs y=1, and their signs are aligned with the direction.

Both branches conversely give legal nonzero signed monomial outputs for every original input and nonzero delay, without a small-cost hypothesis.
Each ORIGINAL individual coordinate sign is preserved.
The two zero-factor cases cannot both occur since the coefficient determinant is-L!=0.
Nontorsion and the rational-unit property ensure that a factor's vanishing at alpha is its actual Laurent-polynomial vanishing, rather than an invisible nonzero multiple of P.

For completeness, the entire nonzero-product exclusion retains three separate cases.
After common monomial normalization, L229 gives for a nonvanishing integer binomial F of positive width t_F and coefficient Euclidean norm S2,

    abs Norm_K(F(alpha))^(1/d)
       <=S2 exp(u_F)sqrt(Ferr(u_F)),
    u_F=t_F*m/d, 0<u_F<=h0.

Its effective support is at most2, and ALL original radial and coefficient costs remain.
If h>0,L>=3, apply this to delta and both other binomials in A to get

    1<=abs Norm_K(z*w)^(1/d)
      <=2R exp(2U)Ferr(abs(k)*m/d)Ferr(h*m/d)
      <=(13/18)exp(2U)Ferr(U)^2<1.

If h=0, the other two factors are collected constants times the same monomial, so B's1/4 estimate instead gives

    1<=abs Norm_K(z*w)^(1/d)
       <=(1/2)exp(2U)Ferr(U)<1.

For0<u<=K0, x0=epsilon(u)+8u<=7/5 and(1+x0)^2<=1+(17/5)x0 give the exact strict comparison

    (13/18)Ferr(u)^2
       <=13/18+(221/90)(epsilon(u)+8u)
        <4/5+8epsilon(u)+32u.

Also(1/2)Ferr(u)<4/5+8epsilon(u)+32u.
The displayed accepted K0 margin makes both contradictions strict.
No epsilon value at0 is used.

The remaining h>0,L2 case has actual q_pair dividing2, weights1/2, E1 and nonzero O0 values.
C71 and C74 force signed monomial outputs at the actual width T<=h+abs(k); width0 is handled by O0 intersection Q=Z and the exact mean square1.
The retained two-term classification then excludes distinct exponents for k!=0.
Thus every nonzero-product branch is exhausted without using the parallel unit-direction theorem as a premise.

**D. Arbitrary finite words, uniform in N/J/M and ALL primitive heights.**
Fix ANY finite N>=2, ANY positive normalized rational indexed weights omega_i and their ACTUAL least denominator M, with positive primitive copies m_i=M omega_i and sum m_i=M.
Start with TRUE Laurent monomials

    F_i^(0)=epsilon_i*t^(a_i), epsilon_i in{+1,-1},
    A0=max_i a_i-min_i a_i.

At each of ANY finite J>=1 steps select distinct labels, use their ACTUAL reduced positive weight ratio r:s, ANY primitive two-nonzero-coordinate integer direction(x,y), and ANY nonzero signed delay k_j.
Keep all labels and weights fixed.
Require EVERY coordinate at EVERY stage, including unchanged coordinates, to have a NONZERO value in the SAME original O0.
Set

    B_word=A0+sum_(j=1)^J abs(k_j),
    U_word=B_word*m/d.

If U_word<=K0, EVERY TRUE intermediate polynomial remains a signed monomial with its ORIGINAL sign.
Every factor has one of C's two actions.
Hence

    actual q_final=1, E=1,
    Lambda=(1/d)sum_i omega_i log abs Norm_K(F_i^(J)(alpha))=0,
    full surplus=Lambda-(1/2)log E=0.

The SAME K0 is uniform in N,J,M, all weight ratios, initial exponent multiplicities and primitive direction heights.
The proof charges the PRE-step common support by A0 plus all prior absolute delays, then applies C to the TRUE current pair.
No value-equivalent clean replacement is inserted into another polynomial vector's covariance identity.

Every positive-income word in this specified class consequently satisfies the STRICT necessary price U_word>K0.
For any fixed B0>0,

    B_word<=B0*d and Lambda>0 imply m>K0/B0.

Thus the class supplies no positive-income words eventually along any hypothetical m(P_l)->0 sequence with fixed degree-linear cumulative budgets, regardless of growth of N,J,M or heights.
This is a construction-class obstruction, not an unrestricted gap or existence assertion about such a sequence.

If primitive ONE-coordinate projection delays are additionally allowed, they only shift that one monomial.
Including their abs(k_j) in the SAME cumulative sum leaves the induction unchanged.
This optional extension includes no rational constant rotations or factors with three or more active coordinates.

**E. Full original denominators, copies, signs and actual widths.**
For an arbitrary legal word before imposing U_word<=K0, let L_j be each actual matrix coefficient denominator from A.
Then

    q_final divides product_j L_j,
    T_final<=B_word,
    FINAL indexed M and every positive copy m_i remain unchanged.

Divisibility is not equality.
All labels remain, and no artificial equal-copy expansion or reweighting is used.
After ONE common monomial t^b makes the final coordinates ordinary, put

    D_i=Norm_K(alpha^b F_i^(J)(alpha)),
    H_i=q_final*t^b F_i^(J) in Z[t].

The complete SIGNED arithmetic and coefficient energy are

    Res(P,H_i)=q_final^d D_i,
    product_i Res(P,H_i)^(m_i)=q_final^(dM)product_i D_i^(m_i),
    sum_i omega_i ||H_i||_2^2=q_final^2,
    I_int=log q_final+Lambda,
    I_int-(1/2)log(q_final^2)=Lambda.

All original contents, degree-d norms and signs remain.
Under D, pre-normalization raw norms are epsilon_i^d nu^(a_i').
The copied exponent sum changes only by(m_i+m_j)k for an actually shifted pair, and by m_i k for an optional one-coordinate shift.
Common normalization contributes nu^b to each norm and nu^(bM) to the copied product.
The matrix determinant is not substituted for the coordinate-norm product.
The separately reused C10 direct covariance bound gives only the additional supplied-packet expense Lambda<=T_final*m/d at the ACTUAL final width.

**F. Positive and unequal-height unchanged controls.**
C71's EXISTING exact positive example lies in this wider class:

    P=t^2-4t+1, d=2, alpha=2+sqrt3,
    weights1/2,1/2, seed(1,t), direction(1,-1), k=1,
    output((1+2t-t^2)/2,(1+t^2)/2),
    actual values(1-alpha,2alpha), signed norms(-2,4),
    q2, FINAL M2, E1, T_final=B_word=2,
    numerator resultants(-8,16), copied product-128,
    Lambda=full surplus=(3/4)log2>0.

Its fixed U_word=m=log(2+sqrt3)>K0, so it is outside the exclusion, not a new packet or a near-one sequence.

For a genuinely unequal-height unchanged control, take direction(2,1), weights1/3,2/3 and seed(1,-1).
Then r1,s2,S6,c_g2,A=B1,L3 and A*f+B*g=0.
The output equals the input for EVERY nonzero k, with actual q1, FINAL M3, E1 and zero income despite matrix denominator3.
More generally r=Y,s=X and opposite direction-aligned equal-exponent signed seeds give the unchanged branch for EVERY coprime positive X,Y.
The theorem therefore restricts the ACTUAL operation at small cumulative cost, not the bare direction height.

**G. Precise remaining classes and sources.**
The result excludes neither three-or-more active coordinates nor rational constant rotations, changing metrics/weights, nonmonomial seeds, final-only integral products, zero intermediate coordinates or small final width obtained by large cumulative cancellation.
It does not assert that every rational weighted paraunitary matrix has a LEGAL factorization in the permitted class.
D37/C82 is comparison and motivation only; the exceptional unit-height classification is proved directly here.
No uniform positive same-exponent income, all-packet positive surplus or unrestricted G0001 result follows.

L229 supplies its accepted complete coefficient-energy bound; C74 supplies its actual numerical margins; C71 supplies only the L2 E1 selector and old positive control; C10 supplies the optional final expense.
L380/C53 credit the prior projection and particular-vector order mechanisms whose needed identities are computed locally.
Their existing Pri11/Dim19/AJL and other source-inspection boundaries remain unchanged.
No unadopted extension, new source theorem or native experiment is a premise.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T16:58 |
| status | open |
| reason | Register the two actual integral auxiliaries, all-height coefficient margin, complete local classification and true-polynomial zero-income theorem uniform in N/J/M/heights, retaining every original cost and exception. The ENTIRE original00:44 D40 remains. R311 inspected that original whole proof; its reviewer now authors this new statement/wrapper, requiring a different noncontributor's actual extraction review before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--G, actual original unit/order/degree, arbitrary primitive binary heights and fixed positive rational weights, all-stage nonzero legality, cumulative budget, complete constants/branches/costs and limitations. |
| argument | [Entire retained original body](#argument) | COMPLETE initial candidate, failed coarse bound and H-subfamily, Sections1--7/Theorems1--2/equations1--17, seven anchors, all controls/source/contribution limits and actual00:44 freeze. |
| dependency | [L229 actual coefficient-energy bound](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Only nonvanishing integer binomials after common monomial normalization, Euclidean norm, effective support at most2 and valid positive actual width; all original roots/radial costs remain. |
| dependency | [C74 fixed numerical section](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY K0 at R1, its h0 and1/20 bounds, and the two strict inequalities; no multiplicity-dependent word theorem supplies the new all-height result. |
| dependency | [C71 all-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Only the L2 exceptional pair with q dividing2, nonzero O0 values and actual common width; zero width is handled separately. |
| dependency | [C71 adopted positive control](Yin_C_G0071_v1.md#statement) | ONLY PartF's exact old quadratic one-step values/norms/resultants and positive surplus, at its fixed outside-threshold measure. |
| dependency | [C10 direct covariance expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Additional Lambda<=T_final*m/d for a supplied legal E1 packet at actual width, not a profile or packet existence theorem. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0311_v1.md#binary-height-whole-independent-finding) | Actual complete00:44 D40 and direct interfaces independently reconstructed by g0001_matrix_recovery before this wrapper. It is not prospective extraction review or adoption. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:09 |
| status | proved |
| reason | Adopt original whole R311 and separate ACTUAL extraction R420. Fix the all-height binary weighted true-polynomial zero-income obstruction, with exact two-integral-auxiliary proof and uniform N/J/M/direction heights, retaining every fixed-weight/nonzero-order/cumulative-cost hypothesis and both zero-factor branches. Root authored this proof and relies on actual separate noncontributor findings. No unrestricted gap or positive main-gate construction follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--G, actual original unit/order/degree, arbitrary primitive binary heights and fixed positive rational weights, all-stage nonzero legality, cumulative budget, complete constants/branches/costs and limitations. |
| argument | [Entire retained original body](#argument) | COMPLETE initial candidate, failed coarse bound and H-subfamily, Sections1--7/Theorems1--2/equations1--17, seven anchors, all controls/source/contribution limits and actual00:44 freeze. |
| dependency | [L229 actual coefficient-energy bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Only nonvanishing integer binomials after common monomial normalization, Euclidean norm, effective support at most2 and valid positive actual width; all original roots/radial costs remain. |
| dependency | [C74 fixed numerical section](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY K0 at R1, its h0 and1/20 bounds, and the two strict inequalities; no multiplicity-dependent word theorem supplies the new all-height result. |
| dependency | [C71 all-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Only the L2 exceptional pair with q dividing2, nonzero O0 values and actual common width; zero width is handled separately. |
| dependency | [C71 adopted positive control](Yin_C_G0071_v1.md#statement) | ONLY PartF's exact old quadratic one-step values/norms/resultants and positive surplus, at its fixed outside-threshold measure. |
| dependency | [C10 direct covariance expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Additional Lambda<=T_final*m/d for a supplied legal E1 packet at actual width, not a profile or packet existence theorem. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0311_v1.md#binary-height-whole-independent-finding) | Actual complete00:44 D40 and direct interfaces independently reconstructed by g0001_matrix_recovery before this wrapper. It is not prospective extraction review or adoption. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c84-binary-height-actual-extraction-finding) | ENTIRE actual A--G, complete original D40 and all exact direct interfaces independently inspected by a noncontributor; root proof authorship and original R311 scope remain explicit. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:48 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain known sufficient independent findings in their original homes and original unknown findings at their actual checking scope. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | Entire A--G, actual original unit/order/degree, arbitrary primitive binary heights and fixed positive rational weights, all-stage nonzero legality, cumulative budget, complete constants/branches/costs and limitations. |
| argument | [Argument: argument](#argument) | COMPLETE initial candidate, failed coarse bound and H-subfamily, Sections1--7/Theorems1--2/equations1--17, seven anchors, all controls/source/contribution limits and actual00:44 freeze. |
| dependency | [Dependency: actual-resultant-coefficient-energy-bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Only nonvanishing integer binomials after common monomial normalization, Euclidean norm, effective support at most2 and valid positive actual width; all original roots/radial costs remain. |
| dependency | [Dependency: multiplicity-delay-explicit-threshold](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY K0 at R1, its h0 and1/20 bounds, and the two strict inequalities; no multiplicity-dependent word theorem supplies the new all-height result. |
| dependency | [Dependency: all-weight-unit-energy-product-theorem](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Only the L2 exceptional pair with q dividing2, nonzero O0 values and actual common width; zero width is handled separately. |
| dependency | [Dependency: statement](Yin_C_G0071_v1.md#statement) | ONLY PartF's exact old quadratic one-step values/norms/resultants and positive surplus, at its fixed outside-threshold measure. |
| dependency | [Dependency: direct-exact-covariance-window-inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Additional Lambda<=T_final*m/d for a supplied legal E1 packet at actual width, not a profile or packet existence theorem. |
| support | [Support: binary-height-whole-independent-finding](../audits/reviews/Yin_R_G0311_v1.md#binary-height-whole-independent-finding) | Actual complete00:44 D40 and direct interfaces independently reconstructed by g0001_matrix_recovery before this wrapper. It is not prospective extraction review or adoption. |
| review | [Current isolated finding](../audits/reviews/Yin_R_G0794_v2.md#g84-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:48 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The [original entire D40 freeze](#binary-height-entire-author-freeze) is extraction ancestry, not another proof dependency.
The complete saved original has24393 characters,231 lines and7 explicit anchors.
Its ENTIRE body follows after removing only duplicate author/framework front matter and demoting the original first title by one hash.
Ordinary line-ending and separating/terminal blank-line normalization is allowed.
Every original candidate/failed-bound paragraph, special-H subfamily calculation, proof case, formula,17 numbered equations, seven anchors, role/source limit, control and freeze remains.
All original ../ledger/ and ../claims/ links remain valid from this directory without rebasing.
No proof passage is replaced by a summary.

Root remains the sole new-proof author.
R311 supplies the separately organized original whole review, including the reviewer's prior C74-antecedent review and C82-wrapper context and root's independently accepted C71/C74 ancestor contributions.
The same R311 reviewer NOW contributes this statement/wrapper and cannot independently review this new artifact.
A separate actual extraction inspection is pending.
Historical author-check and pending-review prose in the retained original remains at its actual date and is not changed into a prospective finding.

D37/C82 remains a comparison only.
The new deduction invokes exactly the adopted interfaces listed above and proves its own elementary projection/order/coefficient/classification steps.
Existing source-proof inspection limits remain.
Structural checks and complete retention do not constitute mathematical acceptance.
This allocation performs no adoption, draft retirement or mathematical native execution.

## Argument

## Unequal-height binary weighted delays and actual order divisibility

Date: 2026-10-12T16:28.
Human author Yin.
Root AUTHOR inquiry under the continuing original G0001 instruction.
The separate D37 author investigates binary unit directions; this inquiry tests the explicitly remaining unequal-height case and does not treat that pending theorem as an accepted premise.
No native program, source acquisition or independent finding is asserted.
All substantive tentative algebra and failed bounds remain here.

## Responsible question and initial reuse

The accepted C71 all-positive-weight E1 denominator dichotomy, C72's unweighted single-step restriction, C74/C77 equal-weight legal words and C78 common content normalization leave unequal-height weighted binary factors outside their specified classes.
L380 already gives weighted rational projection/delay algebra, so that mechanism is credited prior work.
The question is whether original-order divisibility supplies a dimension/weight/height independent small-cumulative-cost obstruction for arbitrary primitive TWO-coordinate directions, or whether an explicit legal control defeats that extension.
A whole proof and independent review are outstanding.

For fixed positive coprime integer relative weights r,s and primitive integers x,y, both nonzero, put S=r*x^2+s*y^2 and direction v=(x,y).
For input f,g the weighted projection delay with nonzero signed k has increments

    (x,y)*(t^k-1)*(r*x*f+s*y*g)/S.

If both old values lie in O0 and both output values are integral, Bezout for gcd(x,y)=1 implies the common scalar increment belongs to O0.
Conversely that scalar membership gives both integral outputs; nonvanishing must be imposed separately.
This is the accepted particular-vector gate specialized directly, not a norm-only replacement for actual order membership.

For clean signed monomial inputs with exponent spread A, a first full norm bound gives

    S <= 2*(r*abs(x)+s*abs(y))*exp((A+abs(k))*m/d)

unless the numerator vanishes at alpha.
This bound alone is NOT enough to bound the heights uniformly: very unequal weights can put most coefficient mass on the smaller direction.
It is retained as an insufficient first estimate, not a completed rigidity theorem.
Rational signed power relations and the possible zero numerator require explicit treatment.

## Candidate arithmetic refinement and its present limits

Let c=gcd(r*x,s*y)>0, a=r*x/c, b=s*y/c, so gcd(a,b)=1 and S=c*(a*x+b*y).
The exact scalar denominator is L=a*x+b*y>0, with expression (t^k-1)*(a*f+b*g)/L.
This is an algebraic rewriting, NOT an assertion that L is the actual packet denominator or that a is invertible modulo L.
Indeed gcd(a,L)=gcd(a,y) can be nontrivial.
Any reduction must keep those prime powers and the actual monogenic order.

When y=1 and signs are aligned, L=a*x+b and gcd(a,L)=gcd(a,b)=1.
Modulo L, the membership condition becomes (alpha^k-1)*(f(alpha)-x*g(alpha)) in L*O0.
A naive norm bound then only gives L<=2*(1+abs(x))*exp(U), which still allows x to grow with the weights.
Thus cancelling the weight numerator by itself does not reproduce D37's constant4 bound for unequal heights.

A tempting family x=H,y=1,r=1,s=H^2 illustrates why the naive bound loses arithmetic: the reduced scalar is (t^k-1)*(f+H*g)/(2H).
Actual divisibility implies (alpha^k-1)*f(alpha) in H*O0, since H*g vanishes modulo H.
For clean monomial f, its unit inverse gives alpha^k-1 in H*O0 and hence H<=2*exp(abs(k)*m/d).
Therefore this particular unbounded-height escape fails at small U even though the coarse weighted Cauchy/norm bound does not exclude it.
This is only a candidate subfamily calculation until the full directions/signs/weights are treated.

The remaining issue is to extract a full arithmetic modulus from the general x,y,r,s prime-power pattern without losing the original degree, signed norms, actual integrality, positive fixed weights or cumulative width.
No p-adic saturation argument or global two-coordinate theorem is yet supplied.
Final-only integral composites, zero intermediate coordinates, changing weights and cancellation between long delays remain separate exclusions.
Any positive result must retain actual q, FINAL M and copied signed norms.
No uniform Mahler gap or actual positive same-exponent income has been achieved by this allocation.


<a id="binary-height-exact-two-integer-auxiliaries"></a>
## 1. The missing second integral auxiliary

Date: 2026-10-12T16:42.
The coarse first norm bound above is insufficient.
A DIFFERENT direct Bezout identity supplies two integral auxiliaries, which together retain a uniform coefficient margin.
This resolves the unequal-height candidate below without a p-adic factor-by-factor classification or a new native calculation.

Fix an actual monic irreducible nontorsion integer unit alpha of ORIGINAL degree d>=2, K=Q(alpha), O0=Z[alpha], nu=Norm_K(alpha) in{+1,-1}, and total m=m(P)>0.
Fix positive coprime integer pair weights r,s and a primitive integer direction(x,y) with BOTH coordinates nonzero.
Set

    S=r*x^2+s*y^2, c=gcd(abs(r*x),abs(s*y)),
    A=r*x/c, B=s*y/c, gcd(abs(A),abs(B))=1,
    L=A*x+B*y=S/c>0,
    Pi=(1/L)[[x*A,x*B],[y*A,y*B]],
    U_k=Id-Pi+t^k Pi, k in Z minus{0}.                (1)

All quantities A,B,L are integers, with sign A=sign x and sign B=sign y.
The four numerator entries in Pi have collective gcd1: Bezout for x,y and A,B gives this, or take the product of their primitive ideals in Z.
Therefore L is the ACTUAL matrix coefficient denominator of U_k when k!=0.
It need not be the actual OUTPUT denominator.
Directly Pi^2=Pi and Pi^T diag(r,s)=diag(r,s)Pi, so U_k preserves that exact weighted Laurent form and has determinant t^k.
This is the retained L380/C53 projection mechanism, specialized directly.

Let the input f,g have actual values in O0, and put delta=alpha^k-1.
If both output values lie in O0, the two increments are x*z,y*z, where

    z=delta*(A*f(alpha)+B*g(alpha))/L.

Bezout for x,y implies z in O0; conversely z in O0 gives both integral outputs.
Define a SECOND value

    w=delta*(y*f(alpha)-x*g(alpha))/L.                (2)

It is also in O0.
Indeed

    delta*f(alpha)-x*z=B*w,
    y*z-delta*g(alpha)=A*w,

and the two left sides lie in O0.
Bezout for A,B then puts w in O0.
This uses full original-order membership, not only integer norms, a maximal order, squarefree residues or a prime-by-prime heuristic.
Nonzero output values remain a separate hypothesis for the stated word class.

Whenever z,w are nonzero, their product is a nonzero algebraic integer and

    1<=abs Norm_K(z*w)^(1/d)
      =abs Norm_K(delta)^(2/d)
       *abs Norm_K(A*f(alpha)+B*g(alpha))^(1/d)
       *abs Norm_K(y*f(alpha)-x*g(alpha))^(1/d)/L^2.  (3)

All original signed norms in this identity occur BEFORE taking absolute values; Norm(L^2)=L^(2d).
Negative delay and monomial normalization contribute only their genuine unit-norm signs.
No field degree is replaced by a powered degree.

<a id="binary-height-integer-coefficient-margin"></a>
## 2. A uniform coefficient margin from four positive integers

For proof estimates conjugate the two coordinates by their individual signs sign x,sign y.
This preserves the diagonal metric, all coefficient magnitudes and absolute norms, while turning the direction into X=abs x,Y=abs y and A,B into a=abs A,b=abs B.
Input/output coordinate signs are restored afterward.
Thus

    a,b,X,Y are positive integers,
    L=a*X+b*Y,
    R=sqrt((a^2+b^2)*(X^2+Y^2))/L^2.                 (4)

The following estimate is uniform in ALL their heights and weights:

    R<=1/4+1/L^2; in particular L>=3 gives R<=13/36. (5)

To prove it, put D=a*Y-b*X.
The two-dimensional identity gives

    (a^2+b^2)*(X^2+Y^2)=L^2+D^2.

Both positive cross products aY,bX are at least1, and their product equals(aX)(bY)<=L^2/4.
Hence each cross product is at most L^2/4, so abs(D)<=L^2/4-1.
Therefore

    L^2+D^2<=L^2+(L^2/4-1)^2=(L^2/4+1)^2,

which proves(5).
The exceptional L2 forces a=b=X=Y=1; the original weights are then r=s=1 and the direction has two unit entries up to signs.
No assumption that one of the original weights is bounded below enters this arithmetic inequality.

A separate constant-input inequality will be needed.
For epsilon,eta in{+1,-1}, if both factors are nonzero, then

    abs((a*epsilon+b*eta)*(Y*epsilon-X*eta))/L^2
       <=1/4.                                      (6)

If epsilon=eta, put v=abs(Y-X)>0 and u=a+b.
Assuming Y>X gives L=X*u+b*v>=u+v; if X>Y exchange the roles.
The product numerator is u*v<=L^2/4.
If epsilon=-eta, put v=abs(a-b)>0 and u=X+Y; assuming a>b gives L=b*u+X*v>=u+v, and interchange otherwise.
Again u*v<=L^2/4.
The zero factors are excluded only to use this estimate in(3); they are classified separately below.

<a id="binary-height-accepted-small-cost-inputs"></a>
## 3. Exact analytic inputs and the strict constant

Use the already adopted [L229 coefficient-energy bound](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound), retaining its stated Pri11/Dim19 source limits and ORIGINAL powered-field multiplicities.
For any nonvanishing integer binomial F with actual normalized width h>0, coefficient Euclidean norm S2 and effective support rho<=2, at0<u=h*m/d<=h0 it gives

    abs Norm_K(F(alpha))^(1/d)
        <=S2*exp(u)*sqrt(Ferr(u)),
    Ferr(u)=1+epsilon(u)+8u.                         (7)

The actual source has the possibly stronger rho-dependent error; replacing rho by2 is monotone.
Negative exponents are removed by a common monomial unit, retaining absolute norms and width.
A constant polynomial is handled exactly, without using epsilon at0.

Use precisely the accepted C71/L229 quantities

    c0=log2/4, h0=c0*exp(-20),
    b0(u)=max(u,sqrt(u/c0)*log(sqrt(c0/u))),
    epsilon(u)=min(1,15*sqrt(b0(u))+4u), 0<u<=h0,
    K0=c0/[2*36^8*5^64].                             (8)

The [C74 explicit margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) already prove K0<h0/2, K0<1/20 and

    exp(2K0)*(4/5+8epsilon(K0)+32K0)<1,
    5^8*(epsilon(2K0)+12K0)<1.                       (9)

Root is an author of that accepted predecessor, which has its own independent original and actual extraction findings; the new proof reuses exactly this resolved numerical interface.
The new independent reviewer must inspect applicability, without treating the old authorship as independent recertification.

For0<u<=K0, put x0=epsilon(u)+8u<=7/5.
Since(1+x0)^2<=1+(17/5)x0 and221/90<4,

    (13/18)*Ferr(u)^2
      <=13/18+(221/90)*(epsilon(u)+8u)
      <4/5+8epsilon(u)+32u.                          (10)

Also(1/2)*Ferr(u)<4/5+8epsilon(u)+32u.
These exact elementary comparisons and monotonicity make the right side of either comparison, multiplied by exp(2u), strictly below1 by(9).
No numerical approximation or new angular assertion is introduced.

<a id="binary-height-uniform-local-rigidity"></a>
## 4. Complete local rigidity for arbitrary primitive binary heights

Take CLEAN signed monomial inputs f=epsilon*t^a0,g=eta*t^b0, put h=abs(a0-b0), and assume BOTH output values under(1) are nonzero in O0.
Put

    U=(h+abs(k))*m/d.

**Theorem 1.**
If U<=K0, precisely one of the following polynomial identities occurs:

    A*f+B*g=0: both coordinates remain unchanged;
    y*f-x*g=0: both coordinates acquire the common factor t^k. (11)

In the second case abs x=abs y=1, the two original signed inputs are aligned with the direction, and their exponent is the same.
In the first case the exponent is also the same, and the two signed weighted direction contributions cancel.
For primitive weights/direction this requires r=abs y,s=abs x with opposite aligned signs.
Both cases conversely give legal nonzero signed monomials at every parameter, with no threshold needed.
Original individual coordinate signs are preserved.

**Proof.**
A rational relation between two signed powers of an algebraic integer UNIT at different exponents would put a nontrivial power of alpha in Q.
A rational algebraic integer unit is+/-1, forcing alpha to be torsion.
Thus each of A*f(alpha)+B*g(alpha) and y*f(alpha)-x*g(alpha) can vanish only when its Laurent polynomial vanishes, and only at equal input exponents.
Their vanishing gives exactly the alternatives in(11), with the stated primitive classification.
They cannot both vanish, since their coefficient determinant is-L!=0.

Suppose neither vanishes.
Then z,w from(2) are nonzero algebraic integers.
First take h>0 and L>=3.
The three binomials in(3) have widths abs(k),h,h and coefficient norms sqrt2,sqrt(a^2+b^2),sqrt(X^2+Y^2), respectively.
Apply(7) separately with u_k=abs(k)*m/d and u_h=h*m/d, whose sum is U.
Every value is nonzero, every domain is valid, and monomial unit signs do not affect these absolute bounds.
Equations(3)--(5) give

    1<=abs Norm_K(z*w)^(1/d)
      <=2R*exp(2U)*Ferr(u_k)*Ferr(u_h)
      <=(13/18)*exp(2U)*Ferr(U)^2<1,                 (12)

using(9)--(10).
This is a contradiction uniform in all four coefficient heights.

If h=0, both original binomials are constants times the same monomial.
Their full norm magnitudes are exact, so(6) and the delta estimate in(7) instead give

    1<=abs Norm_K(z*w)^(1/d)
       <=(1/2)*exp(2U)*Ferr(U)<1.                   (13)

This handles equal exponents for every L, without falsely applying a two-distinct-exponent energy formula to a collected constant.

It remains h>0,L2.
Then a=b=X=Y=1 and r=s=1.
The output pair has actual coefficient denominator q dividing2, exact complementary E1 at weights1/2, and actual common width T<=h+abs(k).
If T>0 the [C71 E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) and(9) force both outputs to be signed monomials: otherwise1<=q^8[epsilon(2Tm/d)+12Tm/d]<1.
If T0, actual order membership and division by the common monomial make both rational coefficients nonzero integers; their mean square1 forces signs.
After the coordinate sign conjugation, the output difference equals f-g.
At distinct input exponents the only monomial possibilities are the unchanged pair or(-g,-f).
The first forces(t^k-1)(f+g)=0, impossible.
The second forces{a0+k,b0+k}={a0,b0}, also impossible for k!=0 by the maximal exponent.
This is the elementary two-term classification, compatible with the separately developed D37 unit-direction proof but proved here without a pending premise.
All cases with z,w nonzero have been excluded, proving(11).

The new ingredient is simultaneous ORIGINAL-order integrality of z AND w, combined with the integer coefficient margin(5), not a bound on the raw direction height or global weight denominator.
The earlier coarse estimate and its failed weight-dependent escape remain in the initial candidate account as actual research history.

<a id="binary-height-arbitrary-legal-word-and-costs"></a>
## 5. Every finite legal binary word, with all original costs

Fix ANY finite number N>=2, ANY normalized positive rational indexed weights omega_i and their ACTUAL least denominator M, with positive primitive copies m_i=M*omega_i.
Start with TRUE Laurent polynomials epsilon_i*t^(a_i), epsilon_i in{+1,-1}, of common width A0.
At each of ANY finite J>=1 steps select a pair of distinct labels, use their reduced ratio r:s, choose ANY primitive two-nonzero-coordinate integer direction(x,y) and ANY nonzero signed integer delay k.
Retain the same weights throughout.
Require EVERY intermediate coordinate, including every unchanged one, to have a NONZERO value in the SAME O0.
Set

    B_word=A0+sum_(j=1)^J abs(k_j), U_word=B_word*m/d.

**Theorem 2.**
At U_word<=K0 EVERY TRUE intermediate polynomial remains a signed monomial with its original sign.
Each factor either fixes its selected pair or shifts two direction-aligned matching monomials together.
In particular

    actual q_final=1, E=1, Lambda=surplus=0.           (14)

The SAME K0 works for arbitrary N,J,M, initial multiplicities, weight ratios and primitive direction heights.
The proof is induction: each projection delay enlarges the actual common support interval by at most abs(k_j), so the next pair's exponent spread plus delay is at most B_word.
Theorem1 applies to the actual current monomials and the required nonzero integral outputs.
It proves the next TRUE polynomial stage, without inserting clean replacements modulo P.
Signed monomials have absolute original norm1 and every factor preserves exact weighted covariance E1.

Consequently, for any fixed B0>0, any positive-income word in THIS class satisfies

    U_word>K0;
    B_word<=B0*d and Lambda>0 imply m>K0/B0.          (15)

These are construction-class obstructions on a hypothetical near-one sequence, not proof that such a sequence exists or a uniform gap for arbitrary polynomials.
One-coordinate primitive projection delays, if additionally allowed, merely shift that one monomial and do not change the induction; rational constant rotations and factors with three or more active coordinates are not included.

For an arbitrary word before the threshold is assumed, let its actual matrix denominators be L_j from(1).
Then

    q_final divides product_j L_j,
    T_final<=B_word,
    FINAL indexed M and every copy m_i remain unchanged. (16)

All labels are retained, without an artificial equal-copy expansion.
After one common t^b normalization, define D_i=Norm_K(alpha^b F_i(alpha)) and integer polynomial H_i=q_final*t^b F_i.
The full original signed identities are

    Res(P,H_i)=q_final^d D_i,
    product_i Res(P,H_i)^(m_i)=q_final^(dM)*product_i D_i^(m_i),
    sum_i omega_i ||H_i||_2^2=q_final^2,
    I_int=log q_final+Lambda.                         (17)

Under(14), pre-normalization raw norms are epsilon_i^d*nu^(a_i'), and the full copied exponent sum changes only by(m_i+m_j)*k when a selected pair is actually shifted.
An allowed single-coordinate delay adds m_i*k.
A common normalization multiplies each raw norm by nu^b and the copied product by nu^(bM).
Contents, negative signs and original degree d are never removed.
The Laurent matrix determinant is not substituted for the product of coordinate norms.
The old C10 direct covariance bound gives the additional generic expense Lambda<=T_final*m/d, at its existing source scope, without constructing a packet.

<a id="binary-height-controls-and-scope"></a>
## 6. Exact controls, attribution and unproved classes

The accepted [C71 PartF positive quadratic control](Yin_C_G0071_v1.md#statement), also credited in D37, belongs to this wider class: P=t^2-4t+1, weights1/2, seed(1,t), direction(1,-1), k1.
It produces((1+2t-t^2)/2,(1+t^2)/2), actual values1-alpha and2alpha, signed norms-2 and4, q2/M2/E1/T2, numerator resultants-8 and16 and full surplus3log2/4.
Its U=m=log(2+sqrt3)>K0.
This is prior exact positive arithmetic, not a new example or near-one sequence.

A genuinely unequal-height unchanged branch is necessary: direction(2,1), weights1/3,2/3 and seed(1,-1) has r1,s2,S6,c2,A=B=1,L3 and A*f+B*g=0.
Its output is identically the original pair for every nonzero k.
Actual q1, FINAL M3 and zero income remain, although the actual matrix denominator is3.
More generally r=Y,s=X and opposite direction-aligned equal-exponent signed seeds give this cancellation for every coprime X,Y.
Thus the theorem does NOT force bounded direction heights; it forces the actual operation to be income-free at small cumulative expense.

L380/C53 credit the weighted projection and particular-vector arithmetic interface.
The new second integral value, height-independent coefficient margin, complete local cases and all-height word induction are proved directly here.
L229 supplies only its already adopted original-resultant coefficient-energy estimate; C71 supplies only the small-denominator exceptional E1 dichotomy and the old positive control; C74 supplies its fixed numerical margins.
C10 supplies only the final optional expense inequality.
The parallel D37/C82 unit-direction result is comparison and motivation, not a logical input or an independent finding for this author extension.
Existing Pri11/Dim19/AJL source-inspection limits remain; no new source theorem or acquisition is asserted.

The theorem leaves factors with at least three active coordinates, rational constant rotations, nonmonomial seeds, changed metrics or weights, final-only integral products, zero intermediate coordinates and small final width obtained from large cumulative cancellation outside.
It does not say every rational weighted paraunitary matrix admits a LEGAL factorization in the permitted class.
No construction of actual same-exponent income A(n)>=eta*d at n<=C*d, no uniform positive-surplus packet and no unrestricted G0001 gap has been produced.

The root author has checked the above algebra by hand, including both integer Bezout steps, the four-positive-integer inequality, the collected constant case, both nonvanishing exceptions, all original signs and widths and the strict inherited margins.
This is still AUTHOR work pending a complete final reread/freeze and separate whole review.
No mathematical native program or trial was run.


<a id="binary-height-entire-author-freeze"></a>
## 7. Entire author freeze and exact direct inputs

Date: 2026-10-12T16:44.
Freeze the COMPLETE initial unequal-height candidate, failed coarse estimates and subfamily check, followed by Sections1--7/Theorems1--2/equations1--17.
The author hand-checked both Bezout implications in the actual O0, primitive matrix-denominator leastness, positive-integer coefficient margin, both equal-exponent sign alternatives, all nonzero rational-power exceptions, the three separate local cases and every original norm/degree/unit-sign factor.
The strict comparison to the inherited K0 margin, C71 exceptional q2 branch, true-polynomial induction, arbitrary weights/heights/counts, actual-versus-cumulative support, copied signed costs and both credited/unchanged controls were also checked.
This is author checking, not independent review or a native calculation.

The direct analytic input is [L229 Theorem(7)](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound), applied only to nonvanishing integer binomials with effective support at most2 and valid positive width parameters.
[C74's explicit numerical section](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) supplies precisely the three retained margins.
[C71's accepted E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) handles only the L2 exceptional pair, and [its statement PartF](Yin_C_G0071_v1.md#statement) supplies the prior quadratic positive control.
The optional final expense uses [C10's direct covariance proof](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality).
Weighted factor/projection attribution is the existing [L380](../ledger/Yin_L_G0380_v1.md#rational-weighted-delay-factorization) and [C53 particular-vector gate](Yin_C_G0053_v1.md#statement); all required elementary identities for this new argument are proved above.
D37/C82 is a comparison and initial lead, not an unadopted premise.

A bounded local phrase screen for a second integral auxiliary and binary height refinements found the current parallel unit-direction work and older differently scoped binary/probability materials; the actual closest arithmetic interfaces above were read.
This is no exhaustive novelty or literature claim.
No new external source acceptance or proof audit is asserted.
Existing original-root angular source boundaries remain attached to their adopted input.

The scoped check of D40 and its four direct analytic/expense Claim or ledger inputs returned checked5.
The pre-freeze saved proof was21132 characters/219 lines/six explicit anchors and ASCII.
A separately organized noncontributor must review this ENTIRE proof and exact interfaces before adoption.
Root is its sole new proof author and cannot provide that independent finding.
This freeze neither fixes a new Claim nor retires the draft, changes the unrestricted contract or supplies the missing positive main-gate income.
