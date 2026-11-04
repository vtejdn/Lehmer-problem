---
author: Yin
---
# Isolated-support rigidity for universally integral paraunitary matrices in wider row windows

Date: 2026-10-12T12:23.
Human author Yin.
Root authored the complete original D23 mathematics and its dated literal correction.
g0001_review_recovery independently reviewed the original20:11 whole scope in R287 and actual20:20 corrected whole scope in R288, and NOW authors this new fixed statement/wrapper.
The extractor is a contributor to this new material and cannot supply its independent actual-extraction review.
Its earlier C65-wrapper contribution remains disclosed in the original review accounts.
The ENTIRE corrected proof, original history/freeze, literal defects and dated correction are retained below.
Initial status is proof draft / under review, pending another noncontributor's actual statement/preservation/interface review.

## Statement

Let P(t)=sum_(i=0)^d p_i t^i be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, p_0 in{+1,-1},p_d=1,p_i in{0,+1,-1}.
Use actual O0=Z[alpha] and original field Q(alpha).
Reciprocity is NOT assumed.
Fix a NONNEGATIVE INTEGER k and put r=k+1,T=d+k.
An original support position i is k-isolated if

    |i-i'|>k for EVERY other i' with p_(i')!=0.

Let n be the total number of nonzero coefficients of P, let h count ALL these actual original isolated positions, and assume

    h>=16r.

Then k<d follows from16(k+1)<=h<=d+1.
Put kappa=sqrt(r/h)<=1/4.
No altered polynomial, support-degree surrogate, overorder or2k-isolation condition is substituted.

**A. Exact universal matrix theorem and converse.**
For ANY positive integer M let U(t) be an M-by-M rational Laurent matrix satisfying

    U(t) U(t^-1)^T=I_M,
    EVERY U_ij(alpha) belongs to O0,
    EVERY ROW's ACTUAL union support width is at most T.

The first condition is an identity in Q[t,t^-1] with ordinary Euclidean weights.
Each row is nonzero; its row-union width is the maximum exponent minus the minimum exponent across ALL nonzero entries of THAT row.
No global span bound across different rows is assumed.

The entry condition, including zero actual values, is equivalent to universal FORWARD preservation U(alpha)O0^M contained in O0^M, by standard basis testing and the ring property.
It is not a condition on one selected packet, and inverse integrality is not separately assumed.

Then there exist a permutation pi of{1,...,M}, signs epsilon_i in{+1,-1} and integer exponents a_i such that

    U_(i,pi(i))(t)=epsilon_i t^(a_i),
    U_(i,j)(t)=0 for j!=pi(i).

This is equality of the ACTUAL Laurent matrix, not just its field evaluation.
It includes M1 and row spans strictly smaller than T; the matrix's actual coefficient denominator is1.
Conversely every such signed monomial permutation satisfies the matrix hypotheses, with row widths0 and universal original-order preservation.
Thus genuinely mixing universally integral matrices must fail the declared isolation or final-row-width condition.
No all-width or tailored-vector impossibility is asserted.

**B. Complete local fractional reduction and strict two-shell bounds.**
Let B be the(T+1)-by-r integer matrix with coefficient columns t^jP,0<=j<=k.
EVERY rational f of degree<=T with nonzero actual f(alpha) in O0 admits

    f=z+B theta, z in Z^(T+1), theta in Q^r,
    |theta_j|<=1/2, z(alpha)=f(alpha)!=0.

This uses the actual degree<d integer power-basis representative and nearest-integer reduction of EVERY quotient coefficient.
For e=||f||_2^2,

    e>=h||theta||_2^2,
    |(B theta)_ell|<=sqrt(r)||theta||_2
                         <=kappa sqrt(e) for EVERY ell,
    e>=a=(1+kappa)^(-2)>=16/25>1/2.

If the ACTUAL value is not one of+/-alpha^ell,0<=ell<=T, then

    e>=b=2/(1+sqrt2*kappa)^2>=128/121>1.

The retained proof checks all h*r DISTINCT rows i+j, each containing only p_i in its respective column, including closed half-integer endpoints.
A nonzero integer z gives the first shell; a nonmonomial value excludes a signed coordinate z and gives either two nonzero coordinates or one of modulus>=2.
No fractional class, scalar denominator, small-energy cutoff or chosen residue inventory is imposed.
These estimates are proved LOCALLY at h>=16r, not imported from C63's separate h>=1024r full-surplus theorem.

**C. All zero-value corrections and both original-polynomial branches.**
Normalize each ENTIRE row by its own common unit monomial.
Paraunitarity and original-order membership survive, and all entries lie in[0,T].
Each row's total coefficient energy is1.
The shells in B force exactly one nonzero integral value, and that value equals epsilon alpha^j for0<=j<=T.
The case of no nonzero value contradicts evaluation of the entire row identity at alpha.

Write the active entry as epsilon t^j+P Q_0 and EVERY other entry as P Q_l, with all deg Q_l<=k.
Including Q_0, set

    A(t)=sum_l Q_l(t)Q_l(t^-1),
    A_0=sum_l||Q_l||_2^2,
    support(A) contained in[-k,k].

The complete row identity, with no zero-valued polynomial dropped, is

    epsilon[t^jP*Q_0*+t^-jP Q_0]+P P* A=0,
    P*(t)=P(t^-1), Q_0*(t)=Q_0(t^-1).

If Q_0=0, the identity and A_0 force every Q_l=0.
Otherwise evaluation at alpha gives P*(alpha)Q_0*(alpha)=0.
Since k<d, a nonzero t^kQ_0(t^-1) cannot vanish at alpha, so reciprocity is forced.
The possibility t^dP(t^-1)=-P(t) would imply P(1)=0, violating irreducibility; hence p_0=1 and P*=t^-dP.
Division then gives

    epsilon[t^jQ_0*+t^(d-j)Q_0]+P A=0.

The bracket has at most2r nonzero positions.
But at EVERY original k-isolated position i, coefficient_i(P A)=p_i A_0, nonzero because Q_0!=0 implies A_0>0.
These h>=16r>2r distinct positions contradict the identity.
The count covers overlap, endpoint and negative Laurent shifts and uses k-isolation exactly.
Hence every correction vanishes.
Row orthogonality forces distinct columns and proves A for the ACTUAL matrix.

**D. Arbitrary final composites and precise applicability.**
Any finite product of rational Laurent paraunitary factors is paraunitary.
The theorem applies to its FINAL matrix when that matrix has the actual universal-entry and row-width properties, independently of intermediate integrality, factor denominators or cancellations.
No factorization theorem or classification of individual factors is presumed.
C53's old single-factor gate is not silently promoted to a composite result.

A matrix may instead map one tailored packet to integral values by cancellation while some of its own entries at alpha are nonintegral.
That does not satisfy universal order preservation.
This theorem does not exclude such vectors, failed isolation, longer final row windows, nonflat inputs, changed orders or different energy conventions.

For k0 the present sufficient condition is h=n>=16 and is weaker than C65's separately accepted first-window n>=5 theorem.
For integer k>=1, dense flat support has h0 and is excluded, consistently with the old dense d+1 dyadic escape.
No degree-proportional-extra-window impossibility follows from this isolation condition.

**E. Complete original packet arithmetic and actual width.**
Before acting on a genuine finite rational complementary packet, expand its ACTUAL FINAL positive normalized rational weights into M equal-weight indexed copies at1/M, all with nonzero actual O0 values.
Only this convention gives the ordinary Euclidean M-by-M action.
The surviving matrix sends

    g_i(t)=epsilon_i t^(a_i) f_(pi(i))(t).

Every output remains nonzero and integral, coefficient energy E and complete circle covariance are unchanged, and the ACTUAL common coefficient denominator q is unchanged EXACTLY.
The unmerged indexed equal weights have least denominator M; any later merging requires its own true final denominator recomputation.

With ALL original d conjugates, put

    nu=Norm_(Q(alpha)/Q)(alpha)=(-1)^d p_0 in{+1,-1},
    D_j=Norm_(Q(alpha)/Q)(f_j(alpha)),
    D'_i=Norm_(Q(alpha)/Q)(g_i(alpha)).

Then the FULL signed norms and their copied product satisfy

    D'_i=epsilon_i^d nu^(a_i)D_(pi(i)),
    product_i D'_i=[product_i epsilon_i^d]
                         nu^(sum_i a_i)product_j D_j.

Integer Laurent numerators F_j=qf_j and G_i=qg_i retain their contents.
The full original-root product of each G_i is q^dD'_i; the complete indexed product carries q^(dM)product_i D'_i.
Negative exponents are evaluated at nonzero original conjugates.
An ordinary-polynomial resultant is used only after ACTUAL common polynomial normalization, with its signed unit-norm factor also charged.

The absolute income Lambda=(1/(dM))sum_j log|D_j| is exactly preserved.
Thus S_int=q^2E, I_income=logq+Lambda and the FULL surplus Lambda-(1/2)logE are unchanged with the SAME actual q and final copies.
No numerator content, negative sign, original root or copy factor is removed.

Each individual coordinate width is preserved, but different row monomials can change the packet's COMMON physical union width.
That actual new width must be measured before applying C10.
Neither a cheap width bound nor invariance of common union width is asserted.
The theorem prohibits genuine universal mixing under its explicit conditions without prohibiting coordinate alignment, providing a full-profile optimum or resolving unrestricted G0001.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:23 |
| status | open |
| reason | Register the complete corrected isolated-support universal matrix theorem at h>=16(k+1), including explicit integer k, full local shells, all zero-value corrections, reciprocal/nonreciprocal support proof, final composites and actual q/M/norm/width costs. R288 covers the corrected original whole body only; its reviewer now authors this new wrapper, requiring another noncontributor's actual extraction review. R287 original literal negative scope and the complete dated correction remain. No all-width/tailored-packet impossibility or Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual flat original unit/order, integer k, h>=16(k+1), every universally integral final Laurent matrix with row widths<=d+k, exact classification, local proof interfaces and complete copied-packet/width limits. |
| argument | [Complete retained proof](#argument) | ENTIRE actual20:20 corrected D23, allocation/reuse/candidate history, Sections1--6/equations1--9, original20:11 freeze and dated type/encoding correction with retained original evidence. |
| support | [C63 exact isolated-support antecedent](Yin_C_G0063_v1.md#statement) | Existing h>=1024(k+1) full-surplus scope only; present16 threshold and all shell steps are locally proved. |
| support | [C63 original solo-row mechanism](Yin_C_G0063_v1.md#isolated-extra-window-row-floor) | Credited actual fractional-cube/distinct-row mechanism, reproduced locally at the exact present hypotheses. |
| support | [C65 short-row matrix antecedent](Yin_C_G0065_v1.md#statement) | Existing first-window n>=5 result and complete cost boundaries; no wider theorem follows by citation alone. |
| support | [C53 universal single-factor boundary](Yin_C_G0053_v1.md#universal-order-preserving-projection-boundary) | Earlier SINGLE-factor scope and universal-versus-particular distinction only, not a premise classifying arbitrary products. |
| dependency | [C10 original common-window price](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only the actual-packet expense interface after common normalization and measurement of NEW union width, retaining all original roots and final copies; not a premise of matrix rigidity. |
| support | [Original literal whole objection](../audits/reviews/Yin_R_G0287_v1.md#isolated-universal-original-literal-finding) | Entire original20:11 mathematical reconstruction and fixed negative type/encoding scope, retained rather than overwritten. |
| support | [Corrected complete whole finding](../audits/reviews/Yin_R_G0288_v1.md#isolated-universal-corrected-whole-finding) | ENTIRE actual20:20 corrected original proof and interfaces only; this reviewer now contributes the new wrapper and cannot provide its independent actual-extraction verdict. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:43 |
| status | proved |
| reason | Adopt original corrected whole R288 and separate actual extraction R290 after retaining original negative R287 and the dated literal/integer-domain correction. Universal original-order-integral final matrices with the declared isolation and row-width hypotheses are exactly signed monomial permutations; tailored packets and unrestricted gap remain outside this theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual flat original unit/order, integer k, h>=16(k+1), every universally integral final Laurent matrix with row widths<=d+k, exact classification, local proof interfaces and complete copied-packet/width limits. |
| argument | [Complete retained proof](#argument) | ENTIRE actual20:20 corrected D23, allocation/reuse/candidate history, Sections1--6/equations1--9, original20:11 freeze and dated type/encoding correction with retained original evidence. |
| support | [C63 exact isolated-support antecedent](Yin_C_G0063_v1.md#statement) | Existing h>=1024(k+1) full-surplus scope only; present16 threshold and all shell steps are locally proved. |
| support | [C63 original solo-row mechanism](Yin_C_G0063_v1.md#isolated-extra-window-row-floor) | Credited actual fractional-cube/distinct-row mechanism, reproduced locally at the exact present hypotheses. |
| support | [C65 short-row matrix antecedent](Yin_C_G0065_v1.md#statement) | Existing first-window n>=5 result and complete cost boundaries; no wider theorem follows by citation alone. |
| support | [C53 universal single-factor boundary](Yin_C_G0053_v1.md#universal-order-preserving-projection-boundary) | Earlier SINGLE-factor scope and universal-versus-particular distinction only, not a premise classifying arbitrary products. |
| dependency | [C10 original common-window price](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only the actual-packet expense interface after common normalization and measurement of NEW union width, retaining all original roots and final copies; not a premise of matrix rigidity. |
| support | [Original literal whole objection](../audits/reviews/Yin_R_G0287_v1.md#isolated-universal-original-literal-finding) | Entire original20:11 mathematical reconstruction and fixed negative type/encoding scope, retained rather than overwritten. |
| support | [Corrected complete whole finding](../audits/reviews/Yin_R_G0288_v1.md#isolated-universal-corrected-whole-finding) | ENTIRE actual20:20 corrected original proof and interfaces only; this reviewer now contributes the new wrapper and cannot provide its independent actual-extraction verdict. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0290_v1.md#isolated-universal-actual-extraction-finding) | Entire actual statement, complete retained original body and precise direct interfaces separately inspected after allocation, preserving earlier review scopes and corrections. Finding relationship: self-reviewed. |

## Registration and complete preservation

Date: 2026-10-12T12:23.
The corrected original D23 body below is retained in full, with only repeated author front matter removed, its first title demoted once and terminal whitespace normalized.
Valid existing relative links are preserved.
Every mathematical proof, original role/reuse/source account, exact scalar/copy/width limitation, original freeze, two original literal defects and dated correction remains.
No new result is inferred from the older candidate or then-pending ancestry descriptions.

R287 and R288 keep their completed original scopes.
This new statement is an AUTHOR extraction and requires a different noncontributor to inspect its actual A--E, retained body and current interfaces.
Initial status stays proof draft / under review.
No target proof modification, original finding rewrite, source acquisition, native mathematical run, adoption or draft retirement accompanies registration.

## Argument

## Isolated coefficients force universal paraunitary rigidity beyond the first window

Date: 2026-10-12T12:07.
Human author Yin.
Root AUTHOR continuation under unchanged G0001.
Root owns this new isolated-row/composite-matrix candidate and cannot independently review it.
No mathematical program or source acquisition is planned.

## Exact reused interfaces and new question

Adopted [C63](Yin_C_G0063_v1.md#statement) proves isolated coefficient rows control every rational quotient fraction, giving all-residue shell/income bounds in a fixed extra window under h>=1024(k+1).
The complete C63 proof and [C65](Yin_C_G0065_v1.md#statement) short-row universal matrix argument have been read.
C65 has now passed actual extraction R284 v1 and awaits root's mechanical adoption; it is credited as the author antecedent, while all steps needed here will be reproved locally.
A bounded current screen at C53/C63/C65 found no universal matrix classification in a wider row window with a quantitative isolated-support hypothesis.
This is not a novelty assertion.

## Candidate theorem and planned complete proof

Let P be the ACTUAL flat monic irreducible nontorsion integer-unit minimal polynomial of degree d.
Fix a nonnegative INTEGER k, r=k+1, and let h count original nonzero coefficient positions isolated from every other nonzero position by MORE THAN k.
Suppose h>=16r.
For ANY rational Laurent square matrix U with U(t)U(t^-1)^T=I, ALL entriesU(alpha) in actual O0 and every ROW-union width<=d+k, the candidate conclusion is that the ACTUAL matrix is a signed monomial permutation.

Each row may be normalized together by its own unit monomial.
Represent each entry as integer z plus P times a rational degree<=k quotient and reduce those r fractions into[-1/2,1/2].
The h*r disjoint solo rows give e>=h||theta||^2 and pointwise perturbation<=kappa*sqrt(e),kappa=sqrt(r/h)<=1/4.
Thus every nonzero integral residue costs at least (1+kappa)^-2>=16/25, while every value not among +/-alpha^j,0<=j<=d+k, costs at least2/(1+sqrt2*kappa)^2>=128/121>1.
These exact inequalities must be locally proved; the lower16 threshold is not silently imported from C63's1024 statement.

Row energy1 then forces one nonzero monomial-valued entry f=epsilon t^j+P Q0 and all other entries P Q_l,deg Q_l<=k.
The FULL row identity has correction A=sum_l Q_l Q_l*, whose constant coefficient is positive if any Q_l is nonzero.
For nonreciprocal P, evaluation at alpha forces Q0*(alpha)=0, hence Q00 because k<d (which follows from h>=16r and h<=d+1); all other Q_l vanish by circle positivity.
If P becomes reciprocal, division by P gives epsilon(t^jQ0*+t^(d-j)Q0)+P A=0.
The left correction has at most2r support positions, but at EACH of the h k-isolated coefficient positions of P, the coefficient of P A is p_i A_0 nonzero.
Since h>2r this is impossible.
Include the antiself p0=-1/irreducibility case.
Then row orthogonality gives the full signed monomial permutation.

All zero residue/monomial residue cases, quotient degree, Laurent supports, actual row shifts, complete original order and arbitrary FINAL composite scope require proof below.
Preserve actual q/FINAL equalweight copies, original signed norms/content and potentially changed unionwidth when the surviving matrix acts on a genuine packet.
This will not rule out sparse-isolation failure, longer row windows, nonflat inputs or a matrix tailored to one packet rather than universally integral.
Developing unadopted author material; independent whole and actual extraction reviews remain separate.


<a id="isolated-universal-matrix-theorem"></a>
## 1. Actual input, threshold and universal final matrix theorem

Let P(t)=sum_(i=0)^d p_i t^i be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, d>=2,p_0=+/-1,p_d=1,p_i in{0,+/-1}.
Use original O0=Z[alpha] and original degree d.
Fix a nonnegative INTEGER k, r=k+1,T=d+k.
Let h be the number of support positions i of P for which every different nonzero support position i' has |i-i'|>k.
Assume

    h>=16r.                                        (1)

In particular h<=d+1 gives16(k+1)<=d+1 and hence k<d.
This needed quotient-degree fact is proved by the actual count, not an additional hidden hypothesis.
Put kappa=sqrt(r/h)<=1/4.

Let U(t) be ANY M-by-M rational Laurent matrix, M>=1, such that

    U(t)U(t^-1)^T=I_M,
    every U_ij(alpha) belongs to O0,
    every ROW's actual union support width<=T.      (2)

All entries are tested, including zero actual values.
Actual entry integrality is equivalent to U(alpha) mapping ALL O0^M forward into O0^M; testing standard basis vectors proves necessity.
No inverse-integrality, particular-packet, factorization, individual-factor or fixed denominator hypothesis is assumed.

**Theorem.**
Under(1)--(2), the ACTUAL Laurent matrix U is a signed monomial permutation: one entry epsilon_i t^(a_i) in each row and a distinct column, all others zero, with epsilon_i=+/-1 and a_i integer.
Conversely every such matrix satisfies(2), with row widths0 and actual order preservation.
Thus a genuinely mixing universally integral rational paraunitary FINAL matrix for this input must violate at least one of the named isolation/width assumptions; no theorem excludes tailored packets or all widths.

The new quantitative threshold16r is proved below.
It is not imported from C63's stronger hypothesis1024r, whose different goal was a small full-surplus bound.
All local shell and correction arguments are supplied here, with C63/C65 credited as author antecedents rather than expanded beyond their selected statements.

<a id="isolated-universal-matrix-local-shells"></a>
## 2. Complete local fractional reduction and two shells at the lower threshold

For any rational f of degree at most T with nonzero f(alpha) in O0, subtract its unique degree<d integer power-basis representative.
Division by the actual monic P yields a rational quotient of degree<=k.
Reduce EACH of its r coefficients modulo integers to theta_j in[-1/2,1/2], absorbing those integer P-multiples into an integer polynomial z.
With B the(T+1)-by-r matrix of columns t^jP,

    f=z+B theta, z in Z^(T+1), theta in Q^r,
    |theta_j|<=1/2, z(alpha)=f(alpha)!=0.            (3)

For every k-isolated i and each0<=j<=k, row i+j of B contains only p_i in column j: another column would use a distinct support index within distance k.
These h*r rows are pairwise DISTINCT, because i+j=i'+j' with i!=i' would also contradict isolation.
Each corresponding coefficient of f is an integer plus p_i theta_j, hence has magnitude at least |theta_j|.
For e=||f||^2 this gives

    e>=h||theta||^2,
    |(B theta)_ell|<=sqrt(r)||theta||
                         <=kappa sqrt(e) for EVERY ell.      (4)

No small-energy assumption or rounding of actual field values occurs here.
Closed half-integer endpoints obey the same inequality.

The integer z is nonzero.
Some coefficient has absolute value at least1, so1<=|f_ell|+kappa sqrt(e)<=(1+kappa)sqrt(e).
Therefore every such f satisfies

    e>=a=(1+kappa)^(-2)>=16/25>1/2.                (5)

Call an actual value monomial in the allowed window if it equals+/-alpha^ell for some0<=ell<=T.
If f(alpha) is not such a value, z is not a signed coordinate vector.
If it has at least two nonzero coefficients, choose two; their absolute sum is at least2 and by(4),

    2<=|f_i|+|f_j|+2kappa sqrt(e)
         <=(sqrt2+2kappa)sqrt(e).

If it has just one coefficient, that magnitude is at least2 and the resulting bound4/(1+kappa)^2 is stronger.
Consequently every nonmonomial value obeys

    e>=b=2/(1+sqrt2 kappa)^2
            >=2/(1+3/8)^2=128/121>1.              (6)

We used kappa<=1/4 and sqrt2<=3/2.
These strict two-shell properties are what the matrix proof requires.
They are locally derived for16r, without presuming the small-pi estimates or full income theorem at C63's1024r domain.

<a id="isolated-universal-matrix-row-values"></a>
## 3. Whole-row normalization and the full polynomial correction identity

Multiply each entire row of U by the inverse of its least exponent monomial to obtain V.
Its entries are ordinary rational polynomials of degree<=T, its rows still satisfy VV*=I, and its values remain in O0 because alpha is an actual unit.
This uses one shift PER ROW, not independent entry shifts.
The constant coefficient of each row norm identity gives total row coefficient energy1.

By(5), at most one entry in any row has a nonzero integral value, since2a>1.
A row cannot have none: if every value vanishes at alpha, every entry is P Q_l with deg Q_l<=k, and the full row identity P P* sum Q_lQ_l*=1 contradicts evaluation at the nonzero alpha.
Thus there is exactly one nonzero value.
Its coefficient energy is at most1, so(6) makes it epsilon alpha^j with0<=j<=T.
Write its polynomial and the other entries as

    f=epsilon t^j+P Q_0,
    f_l=P Q_l, deg Q_l<=k.

The degree bound for Q_0 also holds because both f and epsilon t^j have degree<=T.
Let star mean t->t^-1 and put

    A(t)=sum_l Q_l(t)Q_l(t^-1),
    A_0=sum_l ||Q_l||^2>=0,
    support(A) contained in[-k,k].

The index l includes the active correction Q_0.
In particular A_0>0 if ANY Q_l is nonzero; zero-valued entries have NOT been removed.
Expanding the FULL row identity gives

    epsilon[t^j P* Q_0*+t^-j P Q_0]+P P* A=0.      (7)

If Q_0 is zero, (7) implies A is identically zero, and A_0=0 forces every Q_l to vanish.
The row is then already a single signed monomial.
We show that a nonzero Q_0 is impossible as well.

<a id="isolated-universal-matrix-nonreciprocal-branch"></a>
## 4. Nonreciprocal minimality and the genuine reciprocal branch

Suppose Q_0 is nonzero.
Evaluating(7) at alpha gives

    P*(alpha)Q_0*(alpha)=0.

If P*(alpha)!=0, then Q_0*(alpha)=0.
Multiplying by alpha^k shows that the nonzero rational polynomial t^k Q_0(t^-1), of degree at most k<d, vanishes at alpha.
This contradicts ACTUAL degree-d minimality.
It follows that P*(alpha)=0 instead.

The reversed polynomial t^dP(t^-1) has degree d, leading coefficient p0, and the same root alpha.
Irreducibility and monicity give t^dP(t^-1)=p0 P(t).
The case p0=-1 would force P(1)=0 and is excluded at degree>=2.
Thus p0=1 and P*=t^-dP.
Substitute this into(7) and divide the nonzero Laurent factor t^-dP:

    epsilon[t^j Q_0*+t^(d-j)Q_0]+P A=0.            (8)

The first bracket has at most2r nonzero coefficient positions, since each Q_0 and Q_0* has at most r.
Overlap or cancellation can only lower that count; j endpoints and j beyond d merely move the two Laurent intervals.
No positivity assumption on these coefficients is needed.

On the other hand, for EVERY k-isolated support position i of the ORIGINAL P,

    coefficient_i(P A)=p_i A_0.

Indeed any other convolution term would use a P coefficient at i-l with0<|l|<=k, impossible by isolation, while A has support[-k,k].
Since Q_0 is nonzero, A_0>0, and p_i=+/-1, all these h distinct coefficients of P A are nonzero.
Therefore P A has at least h>=16r>2r support positions.
This contradicts(8).
Notice that k-isolation is sufficient: it is the POSITIVE constant coefficient A_0 sampled at the original positions that prevents cancellation; a stronger2k-isolation hypothesis is unnecessary.

Hence Q_0 must be zero and then every Q_l is zero.
Every row of V has precisely one signed monomial entry.
Row orthogonality prevents two rows from choosing the same column, and the square matrix uses every column.
Undoing the whole-row monomials proves the stated exact classification of U itself.

<a id="isolated-universal-matrix-composite-and-costs"></a>
## 5. Final composites, all original costs and limitations

Every finite product of rational Laurent paraunitary factors remains paraunitary.
The theorem therefore covers ANY such FINAL product when its final entries are all in O0 at alpha and each FINAL row span is at most d+k, without requiring intermediate factors to preserve the order.
Factor cancellations and temporary denominators cannot evade the final row identity.
C53's separate single-factor gate is not being used as an unjustified classification of products.

Conversely, a matrix tailored to a PARTICULAR actual packet can have nonintegral entries while its chosen output vector is integral; then standard-basis testing fails and the universal hypothesis is absent.
The theorem excludes no such tailored construction, higher row width, failure of the coefficient isolation count, nonflat polynomial, changed order or energy convention.
It does not require a global span bound across different rows.

For a genuine packet first expand FINAL rational weights into M equal-weight indexed copies before using the ordinary Euclidean M-by-M convention.
Under the surviving signed monomial permutation, each output is epsilon_i t^(a_i) times one input.
All nonzero O0 values remain nonzero, coefficient energy and circle covariance remain the same, and the ACTUAL common coefficient denominator q is unchanged.
The indexed equal weights still have least denominator M; any later merging requires its own true denominator recomputation.

With nu=Norm_(Q(alpha)/Q)(alpha)=(-1)^d p0, original full signed input norms D_j and original degree d, output norms are

    D'_i=epsilon_i^d nu^(a_i)D_(pi(i)),
    product_i D'_i=[product_i epsilon_i^d]
                       nu^(sum_i a_i)product_j D_j.           (9)

Thus all absolute logarithmic norm income and the full surplus Lambda-(1/2)logE are preserved.
Every original sign remains in(9).
Integer Laurent numerators obtained with actual q retain their contents; their full root products are q^d D'_i and the indexed product has q^(dM).
Negative Laurent exponents are legitimate at nonzero alpha, and an ordinary-polynomial resultant is asserted only after an actual common normalization, whose signed unit norm is also charged.
No primitive-content deletion or q=M identification is made.

The common physical union width of an acted-on packet can change under different row monomials, and must be measured anew before the original C10 expense inequality.
Its maximum individual-coordinate width is unchanged.
Universal rigidity therefore prohibits genuine mixing under(1)--(2), without claiming that useful coordinate alignment is impossible or supplying a cheap width bound for an arbitrary packet.

For k0 this theorem's h=n>=16 requirement is sufficient but weaker than C65's n>=5 first-window theorem, which uses a sharper local shell.
For k>=1, dense flat inputs have h0 and are outside the present isolation hypothesis, consistent with the existing dyadic d+1 escape.
Even for sparse inputs, a degree-proportional extra k may violate h>=16(k+1); no all-C*d impossibility is inferred.
The original uniform arithmetic-income/width problem remains unresolved.

<a id="isolated-universal-matrix-complete-freeze"></a>
## 6. Complete author self-check and frozen handoff

Root checked every actual field/order and flat/minimal input condition, h<=d+1 implying k<d, forward universal versus particular-vector testing, and M1; complete fractional quotient reduction, all h*r distinct solo rows, half-integer endpoints and lower16 threshold; value versus polynomial monomials, zero-residue row impossibility and all nonzero/zero correction costs; quotient support, original-degree nonreciprocal minimality, p0=-1 exclusion and reciprocal Laurent division; the h independently nonzero p_i A_0 coefficients versus at most2r bracket positions, including overlapping/negative-exponent blocks; row orthogonality and EXACT matrix classification; final composites, true q/FINAL equal-weight M, contents/signed Laurent norm products and measured union width; and every stated comparison/uncovered domain.
No native program, external source, pending theorem or formal assistant is a premise.
This is author checking only.

Freeze the ENTIRE original allocation/reuse/candidate history and Sections1--6/equations1--9 at 2026-10-12T12:11.
Root is the sole new mathematical contributor and cannot independently review it.
Separately organized whole review and any later actual Claim extraction review remain required before adoption.
No new execution allowance or unrestricted Task conclusion is asserted.


<a id="isolated-universal-literal-correction"></a>
## Dated literal correction and complete corrected freeze

2026-10-12T12:20.
The actual [R287 original whole finding](../audits/reviews/Yin_R_G0287_v1.md#isolated-universal-original-literal-finding) required two explicit P3 corrections.
The original phrase `Fix k>=0` omitted the INTEGER type required for shift indices and matrix column count; both candidate and formal input now say `Fix a nonnegative INTEGER k`.
The original candidate also contained one U+864F after the theta norm where squared notation belonged, and four U+9B4F occurrences where the kappa variable belonged.
These exact erroneous code points and counts are preserved here as the rejected original literal content; the active candidate now uses ASCII `||theta||^2`, `kappa` and explicit multiplication.
The complete formal squared-norm/kappa proof was already correctly written.
No mathematical threshold, norm or argument changes, beyond making the required integer type explicit.

The original allocation/complete freeze and R287 negative finding retain their own original scope; no original finding is silently relabeled a pass.
Root corrected these literal issues using explicit UTF-8 stdin and ASCII mathematical notation.
Freeze the ENTIRE actual corrected document, including original allocation, Sections1--6/equations1--9, original complete freeze and this exact dated correction.
A separate corrected-whole finding is required before adoption.
No native computation, source change or new execution allowance accompanies this repair.
