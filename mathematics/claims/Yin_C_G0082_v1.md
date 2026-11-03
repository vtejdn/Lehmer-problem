---
author: Yin
---
# Uniform true-polynomial rigidity for legal binary delays at arbitrary fixed rational weights

Date: 2026-10-12T16:36.
Human author Yin.
Fixed internal extraction under the continuing G0001 instruction.
Rounding-recovery supplied all new reduced-weight congruence, original-norm restriction, binary classification and word induction in the complete original D37.
g0001_matrix_recovery authors this new exact statement and extraction wrapper and is therefore a contributor to this artifact.
Root independently WHOLE-reviewed the actual00:27 original in R308, with its C71/C74 ancestor roles and old-control reuse pointer disclosed.
That finding supports the original proof only; it does not prospectively review this new wrapper.
Initial status is proof draft / under review pending separate actual extraction review.

## Statement

Fix an ACTUAL monic irreducible minimal polynomial P of a nontorsion algebraic integer unit alpha, original degree d>=2, K=Q(alpha), O0=Z[alpha], nu=Norm_K(alpha) in{+1,-1}, and total logarithmic Mahler measure m=m(P)>0.
Reciprocity is not required.
Every norm below retains ALL d original embeddings.
For rational Laurent polynomials star reverses t; for matrices it also transposes.

Fix ANY finite N>=2 and ANY positive normalized rational weights omega_1,...,omega_N.
Let M be their ACTUAL least indexed denominator and m_i=M omega_i positive integers, with sum m_i=M and gcd_i m_i=1.
All labels and weights remain fixed.
The atom count N, final indexed denominator M and finite word length are otherwise unrestricted.

Use the already adopted numerical constants and function

    c=log2/4, h0=c exp(-20),
    b_ang(x)=max{x,sqrt(x/c)log(sqrt(c/x))},
    epsilon(x)=min{1,15sqrt(b_ang(x))+4x}, 0<x<=h0,
    K0=c/[2*36^8*5^64]>0.

The function epsilon is increasing on that domain, and the accepted strict margins are

    K0<h0/2,
    5^8[epsilon(2K0)+12K0]<1.

Only these numerical margins of C74 and C71's actual all-positive-weight E1 selector are imported; no multiplicity-dependent word theorem is used to infer the new uniform conclusion.

**A. Exact permitted binary factor and reduced-weight order gate.**
Choose two distinct labels i,j.
Write their weight ratio in lowest positive terms r/s, so

    r=m_i/gcd(m_i,m_j), s=m_j/gcd(m_i,m_j), L=r+s.

For sigma in{+1,-1} and a NONZERO integer delay k, put

    D=diag(r,s), v=(1,sigma)^T,
    Pi=v(v^T D)/(v^T D v)
       =(1/L)[[r,sigma*s],[sigma*r,s]],
    U_k=I-Pi+t^k Pi.

Apply this block to the selected coordinates and fix every other coordinate.
It has Pi^2=Pi, Pi^T D=D Pi, U_k^star D U_k=D and determinant t^k.
Its ACTUAL matrix coefficient denominator is L, since r/L is reduced; the output packet's coefficient denominator may be smaller.
These are precisely binary directions whose two nonzero entries have equal absolute value, normalized to1,sigma.
Arbitrary unequal relative heights or additional active coordinates are excluded.

For any current f_i(alpha),f_j(alpha) in the ACTUAL O0, align a=f_i and b=sigma*f_j and write

    delta=(t^k-1)(r*a+s*b)/L,
    g_i=f_i+delta, g_j=f_j+sigma*delta.

Then BOTH output values lie in O0 if and only if

    delta(alpha) in O0
      iff (alpha^k-1)(a(alpha)-b(alpha)) in L O0.

This is an exact whole-order equivalence, using gcd(r,L)=1 and integer Bezout.
Norm integrality, reduction at one root or membership in a larger maximal order is not substituted.
Nonvanishing of the output values is a SEPARATE hypothesis.

If the aligned inputs are CLEAN signed monomials a=epsilon*t^A,b=eta*t^B with epsilon,eta in{+1,-1}, the identical-polynomial case a=b gives the pure common shift g_i=t^k f_i,g_j=t^k f_j for ANY L.
Otherwise the actual difference and alpha^k-1 are nonzero.
Defining

    u=(abs(A-B)+abs(k))*m/d,

legality forces the exact full-norm price

    L<=4exp(u).

Indeed z=(alpha^k-1)(a(alpha)-b(alpha))=Lh with nonzero h in O0 has signed norm Norm_K(z)=L^d Norm_K(h), and its absolute norm is at most4^d exp((abs(A-B)+abs(k))*m).
Negative delays, opposite equal-exponent signs, all monomial unit factors and original degree-d signs are retained.
The bound concerns this REDUCED pair denominator in the distinct branch; it is not a bound on global M or a claim that the output coefficient denominator equals L.

**B. Absolute local rigidity at the true polynomial level.**
Suppose the selected inputs are signed monomials, both actual output values are NONZERO in O0, and u<=K0.
Then EXACTLY one of these two alternatives holds:

    a=b: both selected original coordinates are multiplied by t^k;
    a=-b and r=s=1: both selected coordinates remain unchanged.

Both alternatives conversely give legal nonzero outputs for every actual input and delay.
No legal small-u step mixes distinct exponents, changes an original coordinate sign or creates a nonmonomial Laurent representative.

In the distinct branch,4exp(K0)<5 forces the integer L<=4.
The clean output pair at normalized weights r/L,s/L has E1, actual q_pair dividing L, and actual common width T<=abs(A-B)+abs(k).
If T>0, a nonmonomial pair would contradict C71 because

    1<=q_pair^8[epsilon(2Tm/d)+12Tm/d]
       <=4^8[epsilon(2K0)+12K0]<1,
    0<2Tm/d<=2K0<h0.

If T=0, divide by its common monomial unit: its rational coefficients are nonzero integers in O0 intersection Q=Z, and positive weighted squared average1 forces both to be signed units.
The remaining two-term polynomial classification is retained completely in the proof.
The conclusion concerns ACTUAL polynomials, not only their values modulo P.

**C. All finite weighted words with one uniform cumulative threshold.**
Start with the TRUE Laurent vector

    F_i^(0)=epsilon_i t^(a_i), epsilon_i in{+1,-1},
    A0=max_i a_i-min_i a_i.

For ANY finite J>=1 choose a permitted binary factor at each step, with its selected labels, sign sigma_j and nonzero signed delay k_j.
Form F^(j)=U_j F^(j-1) using the TRUE polynomials.
Require EVERY coordinate at EVERY stage0,...,J to have a NONZERO value in the SAME original O0.
The global weights and indexed labels remain fixed.
Define

    B_word=A0+sum_(j=1)^J abs(k_j),
    U_word=B_word*m/d.

If U_word<=K0, then EVERY true coordinate at EVERY stage is a signed monomial with its ORIGINAL sign.
Each factor acts by exactly one of B's two cases.
In particular every stage has actual coefficient denominator1, the final complete absolute coordinate norms are1, and

    E=1,
    Lambda=(1/d)sum_i omega_i log abs Norm_K(F_i^(J)(alpha))=0,
    full surplus=Lambda-(1/2)log E=0.

The SAME K0 works for ALL finite N,J,M, arbitrary positive rational weights and arbitrary initial exponent multiplicity.
There is no cloning into M equal labels or dimension/word-length loss.
The induction charges the actual pre-step support by A0+sum_(h<j)abs(k_h), then applies B to the TRUE current monomials.
No clean representative is substituted into another vector's covariance identity.

Consequently EVERY legal positive-income word in this class satisfies the STRICT necessary price U_word>K0.
For any fixed B>0,

    B_word<=B*d and Lambda>0 imply m>K0/B.

Along a hypothetical m(P_l)->0 sequence with B_word,l<=B*d_l, such positive-income words therefore do not exist eventually, even if N,J,M and the reduced pair denominators grow.
This is a uniform obstruction to the specified recipe, not a proof that the hypothetical sequence exists or a gap theorem for arbitrary inputs.
Small FINAL width alone is not the cumulative-budget hypothesis.

**D. All original denominators, copied signs and physical costs.**
For an arbitrary legal word of the stated class, before imposing the small-cost hypothesis, let L_j be its j-th reduced pair denominator.
Then

    q_final divides product_(j=1)^J L_j,
    T_final<=B_word,
    FINAL indexed M is unchanged, copies m_i=M omega_i.

Divisibility of the actual output q is not equality.
Pair normalization in B is an auxiliary two-atom packet and does not change the original global weights.
No label merging, splitting or deletion is part of the word.

Choose ONE common monomial t^b making every final coordinate ordinary.
Let D_i=Norm_K(alpha^b F_i^(J)(alpha)) be the complete normalized SIGNED integer norm, and H_i=q_final*t^b F_i^(J) in Z[t].
Then

    Res(P,H_i)=q_final^d D_i,
    product_i Res(P,H_i)^(m_i)=q_final^(dM)product_i D_i^(m_i),
    sum_i omega_i ||H_i||_2^2=q_final^2,
    I_int=log q_final+Lambda,
    I_int-(1/2)log(q_final^2)=Lambda.

Every coefficient content and original norm remains.
The separately reused C10 direct covariance expense is Lambda<=T_final*m/d at the ACTUAL final width; it does not construct income.

Under C write the PRE-normalization final polynomials as F_i^(J)=epsilon_i t^(a_i').
The full signs and copied exponent sum are

    D_i^raw=epsilon_i^d nu^(a_i'),
    product_i (D_i^raw)^(m_i)
       =(product_i epsilon_i^(d*m_i))nu^(sum_i m_i*a_i'),
    sum_i m_i*a_i'=sum_i m_i*a_i
       +sum_(changing steps j)(m_(i_j)+m_(h_j))*k_j.

Here i_j,h_j are the selected labels, and only the common-shift branch contributes to the final sum.
The common normalization gives D_i=nu^b D_i^raw and multiplies the copied product by nu^(bM).
The determinant t^(sum_j k_j) of the full matrix word is NOT asserted to preserve the copied coordinate-norm product.

**E. Both exact controls and their scope.**
The architecture can give positive income outside the small-cost domain.
Reuse C71's EXISTING control at

    P=t^2-4t+1, d=2, alpha=2+sqrt3,
    weights1/2,1/2, seed(1,t), direction(1,-1), k=1.

The TRUE output and complete costs are

    g1=(1+2t-t^2)/2, g2=(1+t^2)/2,
    g1(alpha)=1-alpha, g2(alpha)=2alpha,
    signed norms(-2,4), numerator resultants(-8,16),
    copied signed numerator product=-128,
    q_final=2, FINAL M=2, E=1, T_final=B_word=2,
    Lambda=surplus=(3/4)log2>0.

All intermediate values in this one-step word are nonzero in O0.
Its fixed U_word=m=log(2+sqrt3)>K0, so it does not contradict C or supply a near-one construction.
The example and numerical identities are old C71 mathematics; only their placement in the stated class is used here.

The identical-aligned exception admits arbitrary pair denominators.
For EVERY integer L>=2, weights1/L,(L-1)/L, seed(1,1), sigma=1 and any nonzero k give EXACTLY(t^k,t^k).
This has actual q1, unchanged FINAL M=L, E1, zero absolute norm income and actual union width0, while B_word=abs(k).
Thus the distinct-branch bound on L cannot be asserted when a=b, and an arbitrarily large matrix or weight denominator alone creates no income.

**F. Exact excluded cases and remaining main gate.**
The result does not assert that an arbitrary weighted paraunitary matrix admits a factorization into these binary unit-direction steps with every intermediate original-order value nonzero.
Unequal primitive direction heights(x,y), whose weighted denominator is r*x^2+s*y^2, do not have the reduced r+s cancellation used above.
More active coordinates, changing weights/metrics, nonmonomial seeds, rational constant rotations, final-only integrality, zero intermediate atoms and small final width with large cumulative delay remain outside.

L380's classical weighted delay factorization and C53's particular-vector order gate are credited antecedents; their needed metric and congruence identities are calculated locally.
C74/C77 fixed-dimension conclusions and C78's scalar/content closure are comparisons rather than hidden premises for C.
The inherited C71/C74/C10 source limits remain.
No uniform positive same-exponent A(n)>=eta*d at n<=C*d, uniform positive packet surplus, all-architecture exclusion or unrestricted G0001 result is supplied.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T16:36 |
| status | open |
| reason | Register the exact reduced-weight gate and original norm price, true-polynomial local rigidity and zero-income word theorem uniform in all N/J/M, complete signed costs and both actual controls. The ENTIRE original00:27 D37 remains. R308 whole-reviewed that original only; this new authored statement/wrapper requires a separate actual extraction review before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, actual original unit/order/degree, fixed arbitrary positive rational weights, exact binary unit directions, all-stage legality, cumulative budget, constants, costs and restrictions. |
| argument | [Entire retained original body](#argument) | COMPLETE allocation/question/reuse/candidate/safe checkpoint and Sections1--8/Theorems1--2/equations1--15, both controls, all source/contributor limits and actual00:27 freeze. |
| dependency | [C71 all-positive-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Supplied pair's exact E1, nonzero O0 atoms, true q/common width and the stated monotone epsilon/domain. No E>1 or unsigned-norm substitute. |
| dependency | [C74 explicit numerical margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY the defined K0, K0<h0/2 and5^8[epsilon(2K0)+12K0]<1; no dimension/multiplicity word theorem supplies the new uniform conclusion. |
| dependency | [C10 direct full-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Additional Lambda<=T_final*m/d for the supplied final legal E1 packet at its actual common width; no profile/lifting existence theorem. |
| dependency | [C71 exact positive control](Yin_C_G0071_v1.md#statement) | ONLY PartF's adopted quadratic one-step values, signed resultants and positive surplus, retained as a credited outside-threshold control. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0308_v1.md#binary-weighted-whole-independent-finding) | Root's actual NONCONTRIBUTOR review of the new complete00:27 D37 deduction, with C71/C74 ancestor contributions disclosed and reused at their accepted scope; no prospective review of this extraction. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T16:49 |
| status | proved |
| reason | Adopt original whole R308 and separate actual extraction R310. Fix the uniform true-polynomial zero-income obstruction for all finite N/J/M within the exact fixed-positive-weight binary unit-direction class, retaining every intermediate nonzero order condition and cumulative support cost. Unequal-height extension remains separate author work. No positive main-gate construction or unrestricted gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, actual original unit/order/degree, fixed arbitrary positive rational weights, exact binary unit directions, all-stage legality, cumulative budget, constants, costs and restrictions. |
| argument | [Entire retained original body](#argument) | COMPLETE allocation/question/reuse/candidate/safe checkpoint and Sections1--8/Theorems1--2/equations1--15, both controls, all source/contributor limits and actual00:27 freeze. |
| dependency | [C71 all-positive-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Supplied pair's exact E1, nonzero O0 atoms, true q/common width and the stated monotone epsilon/domain. No E>1 or unsigned-norm substitute. |
| dependency | [C74 explicit numerical margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY the defined K0, K0<h0/2 and5^8[epsilon(2K0)+12K0]<1; no dimension/multiplicity word theorem supplies the new uniform conclusion. |
| dependency | [C10 direct full-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Additional Lambda<=T_final*m/d for the supplied final legal E1 packet at its actual common width; no profile/lifting existence theorem. |
| dependency | [C71 exact positive control](Yin_C_G0071_v1.md#statement) | ONLY PartF's adopted quadratic one-step values, signed resultants and positive surplus, retained as a credited outside-threshold control. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0308_v1.md#binary-weighted-whole-independent-finding) | Root's actual NONCONTRIBUTOR review of the new complete00:27 D37 deduction, with C71/C74 ancestor contributions disclosed and reused at their accepted scope; no prospective review of this extraction. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0310_v1.md#c82-weighted-binary-actual-extraction-finding) | Entire ACTUAL A--F, complete original and exact adopted interfaces; original whole R308 retains its own scope and disclosed ancestor roles. |

## Registration and complete preservation

The [original entire D37 freeze](#binary-weighted-entire-author-freeze) is extraction ancestry, not another proof dependency.
The full saved original has29785 characters,227 lines and8 explicit anchors.
Its ENTIRE body follows with only duplicate author/framework front matter removed and the original first title demoted by one hash.
Ordinary line-ending and separating/terminal blank-line normalization is allowed.
All original paragraphs, candidate obligations, priority-review/checkpoint history, formulas,15 numbered equations, eight anchors, reuse/contribution/source limits and actual freeze remain.
Every original ../claims/ and ../ledger/ link remains valid from this directory; no rebasing is needed and no proof passage is replaced by a summary.

Rounding-recovery remains the sole new-proof author.
Root supplied the broad question and an existing-control reuse/presentation pointer; R308 discloses those facts and its accepted C71/C74 ancestor contributions.
g0001_matrix_recovery contributes the present statement/wrapper only and cannot independently certify it.
R308's original whole scope does not automatically cover this new artifact.
Historical pending-review prose and the safe checkpoint remain at their original dates; the present decision states this extraction's actual pending review.

The source role remains narrow: the actual adopted C71/C74 numerical/analytic interfaces and the separate C10 final expense carry their existing source-acceptance limits.
L380/C53 are credited mechanisms rechecked locally, C77/C78 are comparison scopes, and no unadopted extension or finite computation is needed.
Structural checks and complete preservation do not constitute mathematical acceptance.
This extraction performs no adoption, draft retirement or native mathematical execution.

## Argument

## Reduced weight denominators in legal binary delay mixing

Date: 2026-10-12T16:12.
Human author Yin.
New AUTHOR inquiry by rounding-recovery under the continuing original G0001 weekly authorization.
Root supplied the broad arbitrary-weight/main arithmetic-gate question, not the formulas or proposed obstruction below.
This author contributed C71's original two-label account and other antecedents; an independent reviewer must inspect any new theorem.
No mathematical native program, source acquisition or new allowance is proposed.
This is a safe author checkpoint before a separately assigned C80 extraction review, not a completed proof or Claim.

## Responsible question and bounded reuse

The current S1/S3/S4/S8 gate remains actual same-exponent income A(n)>=eta*d at n<=C*d, or a fully paid degree-linear complementary packet with uniform surplus.
Adopted C71 allows ALL positive rational weights at E1 but forces only actual coefficient-denominator growth.
C74/C77 exclude legal equal-index-weight rank-one words at thresholds depending on dimension/multiplicity, and require every intermediate original-order value plus cumulative absolute-delay cost.
C78 excludes a different scalar/tensor/full-mixture content-ideal closure, expressly leaving weight-dependent coordinate mixing outside.
None by itself supplies a uniform main gate.

A targeted local screen for weighted rank-one/projection/paraunitary delays and two-coordinate mixing located C71's dyadic two-factor congruence and L377/L380.
The latter already gives rational weighted delay factorization for diag(1,2), with exact original interpolation and prime restrictions; it does not supply intermediate integrality or arbitrary-weight short-cost coverage.
Thus weighted paraunitary algebra is credited reuse, not a new construction.
The proposed new arithmetic step is cancellation of the reduced binary weight numerator in a TAILORED original-order integrality condition, followed by a full ORIGINAL norm bound on the resulting modulus.
This differs from cloning rational weights into M equal labels and merely invoking C77 with dimension M.
This bounded screen is not an exhaustive novelty claim.

## Precise candidate, not yet whole-author frozen

Fix an actual monic irreducible nontorsion integer unit alpha, degree d>=2, O0=Z[alpha], original total measure m>0.
At one step select TWO coordinates of an arbitrary finite positive rational-weight packet.
Write their relative weights as r/(r+s),s/(r+s), with coprime positive integers r,s, and L=r+s.
For sigma in{+1,-1} use the weighted rank-one direction v=(1,sigma) and a NONZERO integer delay k.
On selected coordinates f1,f2 put

    a=f1, b=sigma*f2,
    delta(t)=(t^k-1)(r*a+s*b)/L,
    g1=f1+delta, g2=f2+sigma*delta.

This is the usual projection delay for the diagonal metric diag(r,s); all other coordinates are fixed.
It preserves the selected weighted norm and hence the complete original weighted covariance.
Arbitrary rational direction heights or rational orthogonal constants are NOT included in this proposed class.

At a clean signed-monomial input a=epsilon*t^A,b=eta*t^B, actual output integrality is equivalent to delta(alpha) in O0.
Since gcd(r,L)=1, it is in turn equivalent to

    (alpha^k-1)(a(alpha)-b(alpha)) in L O0.             (candidate1)

Indeed modulo L the weighted numerator equals r(a-b), and the invertibility of r follows from the reduced positive weights.
If a=b as Laurent polynomials, both coordinates are simply shifted by k for every L, and no income is created.
Otherwise a(alpha)-b(alpha) is nonzero by nontorsion, so the complete integer norm floor and elementary full-root binomial estimate should give

    L<=4 exp(((abs(A-B)+abs(k))*m)/d).                (candidate2)

This claims a bound on the REDUCED pair denominator; it does not bound the entire FINAL indexed M or discard original denominator/content costs.
The sign and k<0 branches must retain their unit norm factors explicitly.

The proposed local conclusion uses adopted C74's already explicit K0= (log2/4)/[2*36^8*5^64], whose accepted inequalities give K0<h0/2 and5^8[epsilon(2K0)+12K0]<1.
If u=(abs(A-B)+abs(k))*m/d<=K0, candidate2 would give L<=4 unless the two aligned monomials coincide.
The clean two-coordinate packet at its reduced relative weights has E1, actual q dividing L and actual union width at most abs(A-B)+abs(k).
C71 should then force both output polynomials to be signed monomials.
The zero-width case needs a separate elementary integer-constant check.
A weighted two-coordinate monomial classification, to be written and checked, should show that the only changing case shifts two matching aligned signed monomials; a balanced cancelling case is unchanged.

If these steps hold, induction would exclude positive full norm income for EVERY finite sequence of these binary unit-direction weighted delays at small CUMULATIVE width-times-measure, without a bound on atom count, word length or the positive rational weight denominator.
This is the substantive proposed improvement over the equal-weight dimension/multiplicity price, but is restricted to the stated unit-direction binary factors and complete nonzero original-order legality at EVERY stage.
It would not exclude general high-height weighted directions, final-only integral composites, nonmonomial seeds, arbitrary changes of metric or short final width with large cumulative expense.

## Remaining proof and cost obligations

Complete and check the weighted metric identity, both directions of candidate1 in the actual order, the full signed norm argument for candidate2, the strict constant bound4exp(K0)<5, the exact C71 hypotheses at the clean actual support and zero-width edge case, and the exact weighted monomial classification.
Then state the entire finite word with fixed positive rational weights, all actual intermediary nonzero values, true versus clean polynomials, actual q dividing the product of the pair denominators, unchanged ACTUAL FINAL M/copies, full signed norm products and real physical support versus cumulative budget.
Label splitting or weight changes must not be silently included without a separate exact statement.
A uniform zero-income obstruction in this restricted mixing class would not produce the requested positive same-exponent income or an unrestricted Mahler gap.

The conjectured formulas above are AUTHOR candidate material awaiting complete derivation and review.
No finite arithmetic scan or program has been run.
This checkpoint preserves the actual candidate before priority C80 review; it is not an adopted result.

<a id="binary-weighted-resolved-inputs"></a>
## 1. Resolved inputs and the fixed mixing class

Date: 2026-10-12T16:19.
The priority C80 review is complete and the present author inquiry resumes.

The proof below resolves the stated candidate for FIXED positive rational weights and binary unit directions; it makes no claim about arbitrary direction heights or changing metrics.

The exact [C71 all-weight E1 theorem](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) is used only as its accepted dichotomy: either all nonzero actual integral-valued atoms of a complementary E1 packet are signed monomials, or q^8[epsilon(2Tm/d)+12Tm/d]>=1 in the stated domain.
[C74's explicit threshold](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) supplies ONLY the constant and numerical estimates

    c=log2/4, h0=c exp(-20), K0=c/[2*36^8*5^64]>0,
    K0<h0/2,
    5^8[epsilon(2K0)+12K0]<1.                         (1)

Explicitly the SAME accepted function, writing b_ang to distinguish it from the aligned polynomial b below, is b_ang(x)=max{x,sqrt(x/c)log(sqrt(c/x))} and epsilon(x)=min{1,15sqrt(b_ang(x))+4x} for0<x<=h0.
It is increasing on that domain.
No C74 or C77 fixed-dimension word theorem is invoked as the new proof.
Their equal-copy/multiplicity conclusions are comparison only.
[L380's weighted projection factor](../ledger/Yin_L_G0380_v1.md#rational-weighted-delay-factorization) and [C53's particular-vector arithmetic gate](Yin_C_G0053_v1.md#statement) credit the old rational delay mechanism.
L380's factorization supplies neither binary unit directions nor nonzero integral intermediate states.
[C78](Yin_C_G0078_v1.md#statement) concerns common scalar/content operations, a different class.

Fix an ACTUAL monic irreducible minimal polynomial P of a nontorsion algebraic integer unit alpha, original degree d>=2, K=Q(alpha), O0=Z[alpha], nu=Norm_K(alpha) in{+1,-1}, and total m=m(P)>0.
Reciprocity is not required.
Fix ANY finite number N>=2 and ANY positive normalized rational weights omega_1,...,omega_N.
Their ACTUAL indexed denominator is M and m_i=M omega_i are positive integers with sum m_i=M and gcd_i m_i=1.
The weights and labels remain fixed through a word, but N,M and the number of factors may be arbitrarily large.

For two distinct selected labels i,j, reduce their ratio to coprime positive integers r,s, so omega_i/omega_j=r/s.
Equivalently r=m_i/gcd(m_i,m_j), s=m_j/gcd(m_i,m_j).
Put L=r+s, choose sigma in{+1,-1} and a NONZERO integer delay k.
On those two coordinates use

    D=diag(r,s), v=(1,sigma)^T,
    Pi=v(v^T D)/(v^T D v)
       =(1/L)[[r,sigma*s],[sigma*r,s]],
    U_k=I-Pi+t^k Pi.                                 (2)

Other coordinates are fixed.
This covers precisely primitive binary directions whose two nonzero entries have equal absolute value, normalized to1,sigma.
Arbitrary rational relative heights, more than two active coordinates, rational orthogonal constant factors and changes of weights are outside the stated word theorem.

Directly Pi^2=Pi, Pi^T D=D Pi and v^T D v=L.
Since star sends t to t^-1, expanding the orthogonal projection decomposition gives U_k^star D U_k=D.
The block determinant is t^k.
All entries lie in Q[t,t^-1], and the ACTUAL matrix coefficient denominator is L: the off-zero coefficient r/L is reduced because gcd(r,L)=1.
This does not mean the output packet denominator equals L, since cancellation can reduce it.
These elementary metric identities are a specialization of the credited old factor algebra, not a new factorization theorem.

<a id="binary-reduced-weight-congruence"></a>
## 2. Exact reduced-weight congruence and original norm price

Take any current original-order values f_i(alpha),f_j(alpha) in O0, and align the second coordinate by setting a=f_i, b=sigma*f_j.
The two outputs of(2) are

    delta(t)=(t^k-1)(r*a(t)+s*b(t))/L,
    g_i=f_i+delta, g_j=f_j+sigma*delta.                 (3)

They BOTH have actual values in O0 if and only if delta(alpha) is in O0; one output already supplies necessity by subtraction, and sufficiency is immediate.
Nonvanishing of both outputs is a separate condition throughout.

Because r*a+s*b=r(a-b)+L*b, integer Bezout for gcd(r,L)=1 gives the EXACT equivalence

    delta(alpha) in O0
      iff (alpha^k-1)(a(alpha)-b(alpha)) in L O0.       (4)

For detail, the difference between the two numerator expressions is L(alpha^k-1)b(alpha) in L O0, since alpha is a unit.
If integers x,y satisfy xr+yL=1, membership of r z in L O0 implies z=x r z+yL z in L O0.
No division in a maximal order, residue-field simplification, squarefree assumption or selected-root test is used.
This is the new useful elimination of the REDUCED weight numerator; it is valid in the entire monogenic order.

Now assume the input is CLEAN signed monomials a=epsilon*t^A, b=eta*t^B, with epsilon,eta in{+1,-1}.
If a=b as polynomials, delta=(t^k-1)a and both original coordinates simply acquire t^k.
This case permits arbitrarily large L, with no output denominator or norm income.

Otherwise a(alpha)-b(alpha) is nonzero.
Equality would give alpha^(A-B)=epsilon*eta, which forces alpha to be torsion unless A=B and epsilon=eta, the excluded identical case.
Also alpha^k-1!=0.
Thus z=(alpha^k-1)(a(alpha)-b(alpha)) is a NONZERO original algebraic integer.
If(4) holds, write z=L h with h in O0 minus{0}; the full signed norm identity is

    Norm_K(z)=L^d Norm_K(h), abs(Norm_K(h))>=1.         (5)

Put h_ab=abs(A-B).
Factoring monomial units and, when k<0, the factor alpha^k, changes full signed norms only by powers of nu and a possible degree-d sign.
At ALL d original embeddings, the elementary estimate1+abs(alpha_l)^h<=2max(1,abs(alpha_l)^h) gives

    abs Norm_K(a(alpha)-b(alpha))<=2^d exp(h_ab*m),
    abs Norm_K(alpha^k-1)<=2^d exp(abs(k)*m).

The first estimate includes h_ab=0 and opposite signs, when the first norm is exactly2^d.
Original degree d and every powered-conjugate multiplicity are retained.
Combining with(5) proves

    L<=4 exp(u), u=(h_ab+abs(k))*m/d.                  (6)

This is a strict arithmetic restriction on a tailored legal binary step with distinct aligned monomials.
It is not a bound on global FINAL M and does not identify L with the packet's actual q.
It uses no coefficient-energy approximation or native arithmetic.

<a id="binary-local-uniform-rigidity"></a>
## 3. An absolute local rigidity threshold

**Theorem 1.**
Suppose the input coordinates are signed monomials, both outputs in(3) are NONZERO in O0, and u=(abs(A-B)+abs(k))*m/d<=K0.
Then precisely one of the following applies:

    a=b: g_i=t^k f_i and g_j=t^k f_j;
    a=-b and r=s=1: g_i=f_i and g_j=f_j.               (7)

Both alternatives conversely give legal nonzero signed monomial outputs for every actual input and every k.
In particular no legal step satisfying this threshold mixes two distinct exponents, changes an individual coordinate sign, or creates a nonmonomial Laurent representative.

**Proof.**
The identical case is already exact without a threshold.
In the other case, (6) gives L<=4exp(K0)<5, so the integer L is at most4.
The strict numerical comparison follows without approximations: K0<h0/2<c/2<1/8<1/5<log(5/4), the last inequality following by integrating1/x from1 to5/4.
Thus the clean output pair has actual coefficient denominator q_pair dividing L and q_pair<=4.

The pair, taken ALONE with normalized weights r/L,s/L, has E1 by(2), since its two original atoms are signed monomials.
Its ACTUAL common support width T is at most abs(A-B)+abs(k), whether k is positive or negative.
The weights are positive rational with their actual reduced denominator L, not a lower-bounded probability assumption.
Both values are nonzero integral by hypothesis.
If T>0, C71 and monotonicity imply that any nontrivial pair would satisfy

    1<=q_pair^8[epsilon(2Tm/d)+12Tm/d]
       <=4^8[epsilon(2K0)+12K0]<1,                   (8)

contradicting(1).
The domain is valid because0<2Tm/d<=2K0<h0.
If T=0, both rational polynomials are rational multiples of the SAME monomial.
Their nonzero actual O0 values imply their rational coefficients are nonzero integers: divide by the monomial unit, and use O0 intersect Q=Z.
Their positive weighted squared coefficients average1, so both coefficients are+/-1.
Thus in every case the two output polynomials themselves are signed monomials, not merely monomial values at alpha.

It remains to classify this polynomial possibility; a generic norm-one value conclusion would be weaker.
Let h1=g_i and h2=sigma*g_j.
Then h1=a+delta, h2=b+delta, so h1-h2=a-b.
If A=B but a!=b, one has b=-a.
Two signed monomials whose difference is2a must be h1=a,h2=b; hence delta=0.
Since t^k-1 is a nonzero Laurent polynomial, (3) then forces r=s, and coprimality gives r=s=1.

If A!=B, the two exponents in h1-h2 force precisely one of two arrangements.
Either h1=a,h2=b, so delta=0, impossible because r*a+s*b is a nonzero two-term polynomial.
Or h1=-b,h2=-a, giving delta=-a-b.
Equation(3) then becomes

    t^k(r*a+s*b)=-s*a-r*b.

Both sides have two nonzero terms.
Their exponent supports would give {A+k,B+k}={A,B}, impossible for k!=0 by comparing the largest elements.
This excludes every distinct-exponent case.
The original signs in the identical aligned case are retained when translating back from h2=sigma*g_j.
This proves(7).
The algebraic classification is related to C77's equal-weight block classification, but the uniform arithmetic reduction(4)--(8) does not follow by duplicating weights into its dimension-dependent theorem.

<a id="binary-words-uniform-zero-income"></a>
## 4. Arbitrary-length weighted binary words at cumulative degree-linear cost

Let the TRUE starting vector be

    F_i^(0)=epsilon_i t^(a_i), epsilon_i in{+1,-1},
    A0=max_i a_i-min_i a_i.

Choose ANY finite number J>=1 of factors of(2), selecting any pair of labels, sign sigma_j and nonzero signed delay k_j at each step.
The same positive normalized rational weights omega_i are fixed, but are otherwise arbitrary.
Put F^(j)=U_j F^(j-1), retaining the TRUE Laurent polynomials.
Require EVERY coordinate at EVERY stage0,...,J to have a NONZERO actual value in the SAME O0.
Define the paid cumulative budget

    B_word=A0+sum_(j=1)^J abs(k_j),
    U_word=B_word*m/d.                                (9)

**Theorem 2.**
If U_word<=K0, then EVERY TRUE coordinate at every stage is a signed monomial with its ORIGINAL sign.
Each factor either shifts BOTH selected matching aligned monomials by its delay or fixes both in the balanced opposite case(7).
Consequently the FINAL actual coefficient denominator is1, all full coordinate norms have absolute value1 and

    Lambda=(1/d)sum_i omega_i log abs Norm_K(F_i^(J)(alpha))=0,
    E=1, full surplus=0.                             (10)

The same numerical K0 works for ALL finite N,J and ALL rational positive weights/FINAL M.
No bound on their growth or on initial exponent multiplicity is required.

**Proof.**
Each weighted factor preserves the same exact global covariance, hence E1 holds for every TRUE vector even before the small-cost hypothesis is applied.
Inductively suppose stage j-1 is signed monomials.
Its actual union width is at most A0+sum_(h<j)abs(k_h): multiplication by I-Pi+t^k Pi enlarges any common support interval by at most abs(k), regardless of cancellations.
The gap between the two selected exponents is at most that width.
Therefore their local u is at most U_word<=K0.
Every output has the required nonzero O0 value by the word's legality hypothesis, so Theorem1 applies to the ACTUAL current polynomials and proves the next monomial stage.
This closes the induction from j1 through J.

Unlike a general many-coordinate direction, a selected weighted sum of TWO aligned monomials cannot vanish at alpha without vanishing as a polynomial: a rational signed relation between powers of the integer unit would force a rational unit power, hence torsion unless the exponents coincide.
The explicit local proof above handles the only cancellation that survives.
There is thus no invisible nonzero P correction in this theorem's TRUE polynomials, and no substitution of clean representatives into an old covariance identity.
This stronger polynomial conclusion is specific to the stated binary unit-direction class.

Every legal positive-income word in this class must therefore satisfy the STRICT necessary price U_word>K0.
In particular for any fixed B>0,

    B_word<=B*d and Lambda>0 imply m>K0/B.             (11)

Thus on ANY hypothetical actual sequence m(P_l)->0 with cumulative budgets B_word,l<=B*d_l, no such positive-income words exist eventually, EVEN IF their atom counts, factor counts, weight denominators and reduced pair ratios are unbounded.
This is an obstruction to this specific proposed construction class, not a proof of a gap for arbitrary inputs or an assertion that a near-one sequence exists.
It does not merely replace one multiplicity constant in C77: there is NO dimension/word-length/multiplicity loss in(11), at the price of the explicit restriction on active directions.

<a id="binary-word-full-signed-costs"></a>
## 5. Actual denominators, indexed weights, signs and physical width

For an arbitrary legal word of this class, before assuming U_word<=K0, let L_j be the reduced pair denominator in its j-th factor.
The actual coefficient denominator q_final satisfies

    q_final divides product_(j=1)^J L_j,
    T_final<=B_word,
    FINAL indexed M unchanged, copies m_i=M omega_i.   (12)

The first assertion is divisibility only, since each rational Laurent matrix has denominator L_j and the initial vector is integral.
All N labels and their positive weights remain; no equal-copy expansion is used in the proof and no output atom is discarded.
Actual rational-weight reduction gives gcd_i m_i=1, making M the least indexed denominator throughout.
Individual pair weights normalized by their sum are an auxiliary two-atom packet for Theorem1, not a change of the original global weights.

After ONE common monomial normalization t^b makes every final F_i ordinary, let D_i be its complete original SIGNED value norm and H_i=q_final*t^b F_i in Z[t].
Exact algebra gives

    Res(P,H_i)=q_final^d D_i,
    product_i Res(P,H_i)^(m_i)=q_final^(dM) product_i D_i^(m_i),
    sum_i omega_i ||H_i||_2^2=q_final^2,
    I_int=log q_final+Lambda,
    I_int-(1/2)log(q_final^2)=Lambda.                  (13)

All coefficient contents and all actual integer norms remain in these expressions.
The original degree stays d; no minimal polynomial of a powered unit or selected conjugate is substituted.
The original C10 covariance inequality additionally gives Lambda<=T_final*m/d for such a supplied legal E1 packet, but it is an old expense bound rather than the new obstruction.

Under Theorem2, BEFORE the common shift, write F_i^(J)=epsilon_i t^(a_i').
The full signed norms are epsilon_i^d nu^(a_i'), and the copied product is

    D_i^raw=epsilon_i^d nu^(a_i'),
    product_i (D_i^raw)^(m_i)=(product_i epsilon_i^(d*m_i))
                               nu^(sum_i m_i*a_i'),
    sum_i m_i*a_i'=sum_i m_i*a_i
       +sum_(changing steps j)(m_(i_j)+m_(h_j))*k_j.   (14)

Here i_j,h_j are the two selected labels.
A common normalization t^b gives D_i=nu^b D_i^raw and multiplies the copied product by nu^(bM).
Formula(14) refers expressly to pre-normalization values; formula(13) uses the chosen normalized ones.
The matrix determinant t^(sum_j k_j) is NOT asserted to preserve the copied coordinate norm product.
In the threshold domain q_final=1, E1, all absolute norm income vanishes and actual true polynomials themselves are monomials, regardless of how large the final indexed M is.

<a id="binary-old-positive-control-and-exception"></a>
## 6. A credited positive control outside the threshold and the unbounded-L exception

The architecture is NOT excluded at all parameters.
Reuse EXACTLY the adopted [C71 PartF quadratic control](Yin_C_G0071_v1.md#statement), rather than claiming a newly discovered packet.
For P=t^2-4t+1, d2, alpha=2+sqrt3, take weights1/2,1/2, seed(1,t), direction(1,-1) and k1.
The true output is

    g1=(1+2t-t^2)/2, g2=(1+t^2)/2,
    g1(alpha)=1-alpha, g2(alpha)=2alpha,
    Norm(g1(alpha))=-2, Norm(g2(alpha))=4,
    q_final=2, FINAL M=2, E1, T_final=B_word=2,
    numerator resultants(-8,16), copied product-128,
    Lambda=surplus=(3/4)log2>0.                       (15)

There is only one step, and its initial and final values are nonzero in the same O0.
The fixed actual measure is m=log(2+sqrt3), so U_word=B_word*m/d=m>K0.
Every datum is the old exact control, now placed in this stated binary class.
It supplies no near-one sequence or uniform construction and does not contradict Theorem2.
Root suggested crediting an already retained outside-domain control after reading the developing proof; that is a reuse/presentation pointer, not a contribution to the new reduced-weight congruence or uniform obstruction.

The exceptional identical-aligned branch is also necessary.
For ANY integer L>=2 take weights1/L,(L-1)/L, seed(1,1), sigma1 and any nonzero k.
Formula(3) gives the exact output(t^k,t^k), legal for every original input, with actual coefficient q1, unchanged FINAL M=L, energy1 and zero absolute norm income.
Its actual union width is0 although its cumulative budget isabs(k).
Thus no bound on L can be asserted in(6) when a=b, and a large matrix/weight denominator is not itself arithmetic gain.
This direct identity is a control for the stated exception, not a new positive construction or a uniform-degree estimate.

<a id="binary-obstruction-boundaries-and-source"></a>
## 7. What this excludes and what it leaves open

The new conclusion excludes growing FINAL weight denominators as an escape mechanism for LEGAL finite compositions of the specified binary unit-direction weighted delays from monomial seeds at uniformly small cumulative U_word.
It is not a statement that every weighted paraunitary matrix factors into these permitted pieces with all intermediary O0 values nonzero.
L380 factors an existing rational weighted Laurent column using arbitrary rational directions and constant columns; neither those directions nor their intermediate values meet this theorem automatically.
Replicating weights into M equal coordinates would only recover the already dimension-dependent C74/C77 result and misses the reduced denominator argument(4).

An arbitrary two-coordinate primitive direction(x,y) has weighted denominator r*x^2+s*y^2.
Its numerator cannot be replaced by r(a-b) modulo r+s as in(4); unequal direction heights are a precise remaining case.
More active coordinates, weight changes, nonmonomial seeds, rational constant rotations, final-only integrality, zero intermediate atoms, and small ACTUAL final width with large CUMULATIVE delay remain outside.
C78's content-ideal closure likewise contains no permission to add the excluded mixing operations or normalize these words freely.
No theorem here rules out a different actual positive-income packet architecture.

The same-exponent arithmetic gate is not achieved: no construction of A(n)>=eta*d at n<=C*d, uniform E<1 packet or positive uniform surplus is supplied.
Instead(11) is a uniform obstruction to this fully specified weighted mixing recipe.
The full-word legality and cumulative support charge are essential.
The main G0001 objective remains unresolved.

The source role is narrow and explicit.
L380 already records checked AJL17/AJL16 attribution for the classical delay factor form, with its complex/rational-field and proof-inspection limits; the metric calculation here is a direct specialization.
C53 credits the particular-vector order gate.
C71 and C74 supply their actual adopted theorem/numerical interfaces with the inherited L229/Pri11 source limits, not a new source-proof acceptance.
The elementary integer congruence, full binomial norm bound and two-term polynomial classification are proved completely above.
No external search, mathematical program, J or adoption is part of this new author proof.

<a id="binary-weighted-entire-author-freeze"></a>
## 8. Entire author proof and actual checking boundary

Date: 2026-10-12T16:27.
Freeze the COMPLETE original question/reuse/candidate/safe-checkpoint history and Sections1--8/Theorems1--2/equations1--15.
The author checked the exact weighted projection identity, both actual-order implications in(4), the reduced ratio and coprimality, every full signed norm/unit factor in the denominator bound, the identical-polynomial exception, both signs of delay and monomials, the zero-width rational-integer case, both two-term monomial arrangements, exact C71 domain/monotonicity and strict C74 margins, all local-to-global induction indices, true polynomial rather than value rigidity, actual q versus matrix L versus FINAL M, original copies, common-normalization signs, physical versus cumulative width, and the credited positive and unbounded-denominator controls.
These are AUTHOR checks; a separate whole noncontributor review remains necessary.

The direct accepted proof inputs are [C71's all-positive-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem), [C74's explicit K0/epsilon margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold), and ONLY for the additional generic final expense [C10's direct full-root covariance inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality).
[C71 statement PartF](Yin_C_G0071_v1.md#statement) supplies the already adopted exact quadratic control.
L380/C53 are credited mechanism antecedents whose needed identities are calculated directly here; C77/C78 are comparisons, not additional premise chains.
No unadopted draft, finite experiment or new source theorem is needed.

The scoped check of this draft and actual C71/C74/C53/L380/C10 interfaces returned checked6; all saved author text is ASCII.
Structural checks do not independently prove the mathematics.
Root's broad question and later old-control reuse pointer supplied no new congruence, norm inequality or word-induction step.
This author supplied the new proof and cannot independently review it.
Root may separately review the new deduction with its own C71/C74 ancestor roles disclosed; that does not re-certify those accepted ancestors.
The actual result is a uniform small-cumulative-cost zero-income obstruction for the PRECISE binary unit-direction fixed-weight class.
The main same-exponent arithmetic-income construction and unrestricted G0001 remain unresolved.
No native mathematical execution, Claim adoption or draft retirement was performed.
