---
author: Yin
---
# Fixed-rank coefficient-index bounds and legal rational constant-word rigidity

Date: 2026-10-12T18:01.
Human author Yin.
Fixed extraction under continuing G0001 authorization.
Root authored the ENTIRE D46 proof and implemented its actual01:54:22 corrections.
The g0001_matrix_recovery AI independently whole-reviewed the original revision in R320, identified its two bounded defects, then independently whole-reviewed the ENTIRE actual corrected revision in R321.
That agent NOW authors this statement, decision and extraction wrapper and is a contributor to the present artifact; it cannot independently review its own extraction.
Another noncontributor must inspect this actual registered Claim before adoption.
The complete original candidate, proof, controls, original freeze, negative-review history, old erroneous phrases, dated author correction and corrected freeze are retained below.

## Statement

Let alpha be an ACTUAL nontorsion algebraic integer unit with monic irreducible minimal polynomial P, original degree d>=2, K=Q(alpha), O0=Z[alpha], nu=Norm_(K/Q)(alpha) in{+1,-1} and TOTAL logarithmic measure m=log M(P)>0.
All norms retain ALL d original embeddings; negative powers belong to O0.
Fix r>=1 distinct integer exponents a_1,...,a_r whose powers are Q-linearly independent, so r<=d, and put A=max a_i-min a_i.
Independence remains an EXPLICIT general-rank premise.

Retain the accepted increasing functions and constants at positive arguments only:

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0,
    K0=c0/[2*36^8*5^64], eta_R=K0 R^-64, R in Z_(>=1),
    eta_R<h0/2,
    exp(2eta_R)[4/5+8R epsilon(eta_R)+32R eta_R]<1,
    (5R)^8[epsilon(2eta_R)+12eta_R]<1.

Define H_r to be the LEAST positive integer with H_r^2>=2r, and set

    Q_r=H_r^r,
    R_r=max{r,ceil(Q_r/5)},
    kappa_r=eta_(R_r)>0.

These explicit constants depend only on r.
They are coarse fixed-rank bounds, not the stronger same-K0 three/four-power saturation constants.
Zero-width cases are handled directly without epsilon(0).

**A. ENTIRE coefficient quotient and one simultaneous denominator.**
Define the ADDITIVE subgroup

    L={x in Q^r : sum_i x_i alpha^(a_i) belongs to O0},
    Z^r subset L.

If A*m/d<=kappa_r, then L/Z^r is finite, with integer group order I satisfying

    1<=I<=Q_r,
    I*x belongs to Z^r for EVERY x in L.

Consequently the least common coefficient denominator of ANY finite collection of vectors in L divides the SAME I.
This is not an unbounded least common multiple of separately bounded denominators, and I need not equal the group exponent or a particular packet's denominator.
For r1, L=Z and I1 without a width hypothesis.

No discreteness, lattice determinant, chosen integer basis or prior finiteness is assumed.
The full original norm estimate implies every nonzero O0-valued polynomial on the dictionary has coefficient squared energy>1/2 when0<A*m/d<=kappa_r.
A one-term coefficient is an ordinary nonzero integer.
Unique coset representatives in[0,1)^r placed into H_r^r half-open boxes would, if there were too many, yield a nonzero coefficient difference of squared norm<r/H_r^2<=1/2.
Q-independence makes its actual value nonzero and gives a contradiction.
Translation in the finite quotient then shows that its order I kills every class at once.

The rational analytic estimate is L229 after clearing and CANCELING the SAME coefficient denominator q:

    abs Norm_(K/Q)(f(alpha))^(2/d)
      <=S exp(2u)[1+(rho-1)epsilon(u)+4rho*u],
    u=t*m/d, 0<u<=h0,
    S=||f||_2^2, rho=||f||_1^2/S,

for nonzero actual value and positive actual width t.
The integer floor uses actual O0 membership.
All original norms, scalar factors, coefficient contents and radial expense are retained; no norm-only substitute for membership is used.

**B. ALL supplied finite rational packets on this independent dictionary.**
Let f_b be ANY finite indexed family of rational Laurent polynomials supported in the SAME set{a_1,...,a_r}, with every actual value NONZERO in O0.
Give them positive normalized RATIONAL weights omega_b.
Let q be the ACTUAL least common coefficient denominator, M the FINAL least indexed weight denominator, and T their ACTUAL common union width after one common monomial shift.
Then under A*m/d<=kappa_r,

    q divides I, q<=I<=Q_r<=5R_r, T<=A.

The following two conclusions have different hypotheses:

1. No such family has weighted coefficient squared energy E=sum_b omega_b||f_b||_2^2<1, even WITHOUT lag cancellation.
2. If it has the EXACT Laurent identity sum_b omega_b f_b(t)f_b(t^-1)=1, every TRUE f_b is a signed monomial.
   Actual q1 and full norm income/surplus0 follow.

For the first, the old C50 PartD inequality q^4[epsilon(Tm/d)+6Tm/d]>=1 contradicts the displayed bound q<=5R_r and C74's doubled-parameter margin.
For the second, the old C71 E1 alternative q^8[epsilon(2Tm/d)+12Tm/d]>=1 gives the same contradiction unless all atoms are signed monomials.
T0 is handled by positive weighted integer squares.
Neither argument assumes a fixed below-one deficit, a minimum positive weight, a bounded label count or a bounded FINAL M.

Coefficient energy1 alone, WITHOUT the full lag identity, is not asserted to force monomial polynomials.
E>1 and dependent dictionaries remain outside.
No short independent dictionary or such packet is constructed for an unrestricted target.
The fixed group order I, actual coefficient denominator q and weight denominator M remain distinct.

**C. Positive RATIONAL constant metrics and arbitrary finite legal words.**
Let B be ANY rational CONSTANT isometry of a finite positive RATIONAL diagonal metric D, so B^T D B=D.
Apply it to TRUE signed monomial inputs whose selected block uses at most r distinct Q-independent powers at common span A.
Require every actual output NONZERO in O0.
If A*m/d<=kappa_r, every TRUE output is a signed monomial on an exponent already present in that block.
Repeated input exponents do not force the entire matrix integral.
Signs may change.

The weights normalized by their positive rational sum and the unchanged support satisfy B.
This proves an actual polynomial assertion; a value-equivalent different representative is not inserted into its covariance.
For s<=r distinct powers, H_s^s<=H_r^r and R_s<=R_r give kappa_s>=kappa_r, so the stated rank bound applies without assuming unspecified monotonicity or inventing extra independent powers.

Fix any finite number of labels, fixed positive normalized rational weights and TRUE signed monomial seeds of initial common span A_init.
Allow ANY finite interleaving of these constant blocks with the ACTUALLY ADOPTED C84 primitive weighted binary delays, either nonzero signed delay k, and optional one-coordinate monomial shifts.
Every constant block must use at most r DISTINCT CURRENT exponents whose powers are Q-independent.
The permitted binary delay is the C84 factor at the selected reduced positive ratio r_pair:s_pair and primitive integer direction v=(x,y)^T, xy nonzero:

    U_k(t)=Id+(t^k-1)v(v^T D)/(v^T D v).

Keep all labels and weights fixed and require EVERY intermediate actual coordinate NONZERO in the SAME O0.
Charge

    B_word=A_init+sum_(ALL delayed factors)abs(k),
    B_word*m/d<=kappa_r,

including the absolute delay of every one-coordinate shift.
Then EVERY TRUE intermediate polynomial remains a signed monomial, actual final q1, E1 and full income/surplus0.
Constants introduce no new exponent, and each C84 step increases common width by at most abs(k).
Since kappa_r<=K0, its exact adopted local interface applies at every stage.

The result is uniform in word length, labels, fixed rational weights/FINAL M, actual constant-matrix denominators and primitive delay heights, at each FIXED r.
The local general-rank independence gate stays explicit.
The earlier three/four-power results are not used to remove it for arbitrary r.
No general rational paraunitary matrix is asserted to have a factorization preserving that gate and all intermediate order membership.
Small final width after large cumulative cancellation does not replace the charged budget.

**D. Every original norm, scalar, indexed copy and sign.**
For a supplied packet after ONE common shift, let F_b=qf_b in Z[t], m_b=M omega_b be its positive primitive copies and D_b=Norm_(K/Q)(f_b(alpha)) its nonzero signed ORIGINAL norms.
Then

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(m_b)=q^(dM)product_b D_b^(m_b),
    S_int=q^2 E,
    Lambda=(1/d)sum_b omega_b log abs(D_b),
    I_int=log q+Lambda,
    surplus=Lambda-(1/2)log E.

If norms are recorded before a common shift t^b, include its precise copied factor nu^(bM).
Contents remain inside every integer numerator and all indexed copies are retained.
Quotient order I is neither M nor I_int.
The same log q cancels only after both norm and energy costs are charged.

For general words before rigidity, actual output denominator divides the product of actual constant-matrix entry denominators and exact C84 delay denominators; it may be much smaller.
Actual final union width is at most B_word and FINAL M/copies remain fixed.
Under C, q1 and actual final signed norms(epsilon'_b)^d nu^(a'_b) have absolute value1, so E=S_int1 and Lambda=I_int=surplus0.
No matrix determinant or initial copied exponent sum replaces the coordinate norm product.
The original field is retained even if powers have smaller minimal degree.

**E. Exact index-five control and corrected full norm.**
On the adopted golden input P=t^2-t-1, alpha=(1+sqrt5)/2, d2, nu=-1 and alpha^5=3+5alpha, the powers1,alpha^5 are independent and

    x+y alpha^5 belongs to Z[alpha]
      iff x+3y belongs to Z and5y belongs to Z.

Thus L/Z^2 has EXACTLY5 classes, generated by(-3/5,1/5).
At r2, H2=2 and Q2=4, so this actual I5 exceeds the small-cost bound outside its domain.
The representative(2/5,1/5) has

    (2+alpha^5)/5=1+alpha=alpha^2,
    actual denominator5, coefficient energy1/5,
    full signed Norm(1+alpha)=+1,
    Res(P,2+t^5)=+25.

The positive signs are the ACTUAL corrected values.
The original norm-1 phrase is retained only as a quoted historical error in the dated correction.
Its width5 gives U=(5/2)log alpha>K0>=kappa_2, so it does not contradict the theorem or supply a near-one family.

The old accepted rotation B=(1/5)[[3,4],[-4,3]] on(1,t^5), weights1/2, has actual values3+4alpha and1+3alpha of norms5,-5; actual q5/M2/E1/T5, signed numerator resultants125,-125, copied product-15625 and full surplus(1/2)log5>0.
These old controls remain credited to C87.
The new coefficient-quotient calculation identifies exactly why the fixed input is outside the bounded-index conclusion; it is not a new uniform positive-income construction.

**F. Source, correction history and exact remaining scope.**
The finite quotient proof is a local classical box-pigeonhole argument.
The old C57/C59 mechanisms and EPF26 selected Dirichlet attribution retain credit, but no external lattice/Minkowski theorem is a proof premise.
EPF26's ordinary attribution account is not promoted into a canonical source theorem or full proof audit.
L229's accepted source limits, C74's numerical margins, C50/C71's old packet consequences, C84's actual delay class and C87's fixed control retain their precise scopes.

R320 found the original control sign error and the missing local RATIONAL metric qualifier.
Root corrected those exact points at01:54:22 and retained the original phrases and earlier freeze.
R321 then actually whole-reviewed the COMPLETE corrected draft.
Neither record automatically reviews this new extraction, and R320's old negative finding is not rewritten or backdated.

For each FIXED r and fixed C>0, the result excludes nontrivial E1 packets on actual independent r-power dictionaries of span<=Cd when m<=kappa_r/C.
It does not prove arbitrary-rank saturation, eliminate general-rank dependence, construct an independent dictionary for all inputs, classify E>1 packets or general rational factorization, provide uniformly positive same-exponent arithmetic income, or resolve the unrestricted Mahler-gap Task.
Dependence and growing dictionary size remain possible exits, not successful constructions.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T18:01 |
| status | open |
| reason | Register the fixed-rank ENTIRE coefficient quotient and simultaneous-denominator theorem, distinct below-one/exact-E1 packet consequences, rational-metric constant/mixed words and correctly signed exact control, retaining the ENTIRE actual01:54:22 corrected D46. R320's initial objections and the dated author corrections remain; R321 supports only the corrected original whole. Its reviewer now authors this wrapper, which requires another noncontributor's actual extraction review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F, explicit original-order/general-rank independence, exact constants/index/q/M separation, rational metrics, actual words/costs/control/source and all exclusions. |
| argument | [Entire corrected original body](#argument) | COMPLETE candidate, Sections1--6/Theorems1--2/equations1--9, ten anchors, old01:46:38 freeze, exact negative-finding/correction history and actual01:54:22 corrected freeze. |
| dependency | [L229 coefficient-energy bound](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Nonvanishing actual integer auxiliary and original full norm, S/rho/radial costs; local rational denominator cancellation and accepted positive parameter domain. |
| dependency | [C74 all-R numerical margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | EVERY integer R>=1 eta_R and both exact strict inequalities, applied at R_r=max(r,ceil(Q_r/5)); no old multiplicity word theorem supplies the new index result. |
| dependency | [C50 general-unit below-one theorem](Yin_C_G0050_v1.md#statement) | ONLY PartD actual nonzero O0 rational family, positive rational weights, coefficient E<1 WITHOUT lag equations, actual q/T and q^4 necessary price. |
| dependency | [C71 all-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Finite positive rational weights, EXACT covariance1, actual q/common width and nonzero O0 values, signed-monomial alternative or q^8 price. |
| dependency | [C84 actual adopted delays](Yin_C_G0084_v1.md#statement) | Specified primitive weighted binary signed delays and optional one-coordinate shifts, TRUE output at K0, fixed rational weights/all-stage nonzero O0 legality and cumulative/full-cost scope. |
| dependency | [C87 golden input/control](Yin_C_G0087_v1.md#statement) | ONLY PartE golden polynomial/power identity and old q5 rotation with exact values/norms/resultants; not a premise removing general-rank independence. |
| support | [Initial negative whole finding](../audits/reviews/Yin_R_G0320_v1.md#fixed-rank-whole-initial-finding) | Actual earlier01:46:38 D46, two exact bounded defects and its unchanged changes-required verdict; historical correction provenance, not an active unresolved objection to the corrected original. |
| support | [Corrected original whole finding](../audits/reviews/Yin_R_G0321_v1.md#fixed-rank-corrected-whole-independent-finding) | ENTIRE actual01:54:22 corrected D46 including both implemented repairs, unchanged proof/cost/source interfaces and preserved history. Its reviewer now authors this wrapper; no prospective extraction coverage. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T18:08 |
| status | proved |
| reason | Adopt corrected original whole R321 and separate actual extraction R323, retaining initial negative R320 and the exact dated author repairs. The finite coefficient-quotient index, simultaneous denominator bound, separate below-one/no-lag and E1/full-lag conclusions, and legal fixed-rank rational-metric word class are fixed at their explicit independence and cumulative-cost scopes. Root authored the proof and relies on distinct noncontributor findings; no E>1 or unrestricted gap conclusion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F, explicit original-order/general-rank independence, exact constants/index/q/M separation, rational metrics, actual words/costs/control/source and all exclusions. |
| argument | [Entire corrected original body](#argument) | COMPLETE candidate, Sections1--6/Theorems1--2/equations1--9, ten anchors, old01:46:38 freeze, exact negative-finding/correction history and actual01:54:22 corrected freeze. |
| dependency | [L229 coefficient-energy bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Nonvanishing actual integer auxiliary and original full norm, S/rho/radial costs; local rational denominator cancellation and accepted positive parameter domain. |
| dependency | [C74 all-R numerical margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | EVERY integer R>=1 eta_R and both exact strict inequalities, applied at R_r=max(r,ceil(Q_r/5)); no old multiplicity word theorem supplies the new index result. |
| dependency | [C50 general-unit below-one theorem](Yin_C_G0050_v1.md#statement) | ONLY PartD actual nonzero O0 rational family, positive rational weights, coefficient E<1 WITHOUT lag equations, actual q/T and q^4 necessary price. |
| dependency | [C71 all-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Finite positive rational weights, EXACT covariance1, actual q/common width and nonzero O0 values, signed-monomial alternative or q^8 price. |
| dependency | [C84 actual adopted delays](Yin_C_G0084_v1.md#statement) | Specified primitive weighted binary signed delays and optional one-coordinate shifts, TRUE output at K0, fixed rational weights/all-stage nonzero O0 legality and cumulative/full-cost scope. |
| dependency | [C87 golden input/control](Yin_C_G0087_v1.md#statement) | ONLY PartE golden polynomial/power identity and old q5 rotation with exact values/norms/resultants; not a premise removing general-rank independence. |
| support | [Initial negative whole finding](../audits/reviews/Yin_R_G0320_v1.md#fixed-rank-whole-initial-finding) | Actual earlier01:46:38 D46, two exact bounded defects and its unchanged changes-required verdict; historical correction provenance, not an active unresolved objection to the corrected original. |
| support | [Corrected original whole finding](../audits/reviews/Yin_R_G0321_v1.md#fixed-rank-corrected-whole-independent-finding) | ENTIRE actual01:54:22 corrected D46 including both implemented repairs, unchanged proof/cost/source interfaces and preserved history. Its reviewer now authors this wrapper; no prospective extraction coverage. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0323_v1.md#c90-fixed-rank-actual-extraction-finding) | Entire actual C90 A--F and complete corrected original, including both historical defects/repairs, every exact q/I/M/sign/word/source/control interface; distinct noncontributor. |

## Registration and complete preservation

The ENTIRE actual corrected D46 follows.
Only its36-character author/framework front matter is omitted and its first title demoted by one heading level.
Every original candidate, proof, numbered equation, ten explicit anchors, exact quotient/control calculation, source and author-role limit, original freeze, dated negative-finding/correction account and corrected freeze is retained verbatim.
The two original erroneous/unqualified phrases remain within their dated correction history, not as active final claims.
All relative links remain valid from this Claim directory and need no rebasing.

Original size is19349 characters.
Its19313-character body becomes19314 solely through title demotion, with162 body lines, ten anchors, all equations1--9 and nine links.
Full readback compares the complete body, not a summary.
These are truthful operational preservation facts, not a mathematical digest or a persistent byte-retention promise.
Historical pending statements remain at their actual dates; the current initial decision owns this new artifact's assessment.

Root remains the original proof/correction author.
The matrix-recovery AI is NOW the new wrapper contributor after its initial negative and corrected whole reviews, so another noncontributor must inspect this actual wrapper.
Older accepted-ancestor roles are disclosed in R321 and do not certify new mathematics.
No mathematical native run, external acquisition, original-draft retirement or adoption accompanies this allocation.

## Argument

## Fixed-rank order-lattice index and rational constant-factor rigidity

Date: 2026-10-12T17:43.
Human author Yin.
Root AUTHOR exploration under the continuing G0001 weekly instruction.
This new question follows the small fixed-power saturation work but does not assume arbitrary-rank saturation.
The original order is O0=Z[alpha].
No native program, adoption or independent finding is asserted.

<a id="fixed-rank-order-index-candidate"></a>
## Responsible candidate

For r Q-independent powers in a short measure-scaled window, consider ALL rational coefficient vectors whose actual values are order integers, as an additive group L containing Z^r.
Can exact small-box pigeonhole packing bound the finite index [L:Z^r] solely in r?
The actual nonzero norm floor and L229 coefficient-energy upper bound forbid two distinct coset representatives in one sufficiently small box.
If the index is finite, its group order clears EVERY coefficient denominator in L at once.
Combining this with the already accepted C71 E1 denominator obstruction may exclude every rational constant isometry on such a fixed-rank power dictionary at a threshold depending only on r, without bounding direction heights, labels, weights or number of constant factors.

The finite grid/pigeonhole mechanism is classical, with the repository's earlier Dirichlet attribution in C57/C59 and EPF26 retained.
This new use concerns the actual order coefficient quotient, not C57's fixed-degree first-window capacity, eigenvalue or C59's supplied-deficit finite dictionary.
Initial bounded literal searches found those old mechanisms; no claim of historical priority is made.
All new derivations, failed cases, exact constants and full costs will be written here before review.
Q-independence for arbitrary r remains an explicit gate; the earlier at-most-four-power work cannot automatically supply it for larger r.


<a id="fixed-rank-exact-inputs"></a>
## 1. Actual powers and the precise small-box threshold

Let alpha be an actual nontorsion algebraic integer unit, P its monic irreducible minimal polynomial of ORIGINAL degree d>=2, K=Q(alpha), O0=Z[alpha], nu=Norm_K(alpha) in{+1,-1}, and m=log M(P)>0 the TOTAL measure.
Fix r>=1 distinct integer exponents a_1,...,a_r whose powers are Q-linearly independent; in particular r<=d.
Put A=max a_i-min a_i.
For r1, the arguments with positive width are unnecessary and the coefficient group below is exactly Z; assume r>=2 unless stated otherwise.

The [L229 actual coefficient-energy input](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) applies to the same d original conjugates.
For a rational Laurent polynomial f with nonzero value, actual width t>0, squared coefficient norm S and rho=||f||_1^2/S, clearing and canceling its actual scalar denominator gives

    |Norm_K(f(alpha))|^(2/d)
      <= S exp(2u)[1+(rho-1)epsilon(u)+4rho*u], u=t*m/d<=h0.      (1)

The cancellation is exact: qf has squared coefficient norm q^2 S and original norm q^d Norm(f(alpha)), up to the common monomial unit sign.
No content, original root or norm-floor premise is suppressed.
Here c0=log2/4, h0=c0 exp(-20), epsilon(u)=min{1,15sqrt(b(u))+4u}, b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)}, at POSITIVE arguments in its accepted increasing domain.
If f has width0 and nonzero integer value, it is a rational multiple of a unit, hence that rational coefficient is an ordinary nonzero integer and S>=1.

The exact accepted [C74 margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) give, for every integer R>=1,

    K0=c0/[2*36^8*5^64], eta_R=K0 R^-64<h0/2,
    exp(2eta_R)[4/5+8R epsilon(eta_R)+32R eta_R]<1,
    (5R)^8[epsilon(2eta_R)+12eta_R]<1.                         (2)

Define H_r as the LEAST positive integer with H_r^2>=2r, and set

    Q_r=H_r^r,
    R_r=max{r,ceil(Q_r/5)}, kappa_r=eta_(R_r)>0.               (3)

All constants are explicit functions of r alone.
They are deliberately coarse and do not replace the much stronger same-K0 three/four-power results at their own scopes.
If0<U=A*m/d<=kappa_r, then EVERY nonzero actual O0-valued polynomial on this r-power dictionary has coefficient squared norm S>1/2.
For positive actual width, rho<=r and the product of exp(2U) with

    (1/2)[1+(r-1)epsilon(U)+4rU]

is strictly smaller than C74's4/5+8R_r epsilon(U)+32R_r U expression.
Equation(1) and the integer-norm floor would contradict S<=1/2.
The width-zero case was handled above.
The upper bound is not a lower norm estimate for arbitrary algebraic values; actual O0 membership supplies the floor.

<a id="fixed-rank-coefficient-quotient-index"></a>
## 2. Finite original-order coefficient quotient

Define the ADDITIVE subgroup

    L={x in Q^r : sum_i x_i alpha^(a_i) belongs to O0}.

It contains Z^r.
Q-independence makes the evaluation map injective on Q^r.
No discreteness, determinant lower bound, precomputed integer basis or finiteness of L/Z^r is assumed.

**Theorem 1.**
If A*m/d<=kappa_r, then the quotient L/Z^r is finite, its integer order I satisfies

    1<=I<=Q_r, and I*x belongs to Z^r for EVERY x in L.       (4)

For r1, I1 and the conclusion is unconditional in the exponent.

For r>=2 represent every coset uniquely in the half-open cube[0,1)^r by subtracting coordinatewise floors.
Subtraction preserves L membership.
Partition the cube into the Q_r=H_r^r half-open boxes of side1/H_r.
If there were more than Q_r cosets, choose Q_r+1 representatives; two belong to the same box.
Their difference y is nonzero, belongs to L and satisfies

    |y_i|<1/H_r for every i,
    S=sum_i y_i^2<r/H_r^2<=1/2.                              (5)

Independence makes its actual value nonzero.
If the difference has one surviving coefficient, its integer unit-normalized value makes S>=1.
Otherwise its actual positive width is at most A and Section1 excludes(5).
This contradiction proves finiteness and I<=Q_r, with no compactness or limiting-lattice premise.

For completeness, the finite group order clears every coefficient class: translation by any x in L/Z^r permutes its I elements.
Summing all group elements before and after translation gives I*x=0 in the quotient.
Thus I*x is in Z^r for every x in L.
In particular every individual coefficient denominator divides I, and the common denominator of ANY finite collection of these vectors also divides that SAME I.
This is stronger than bounding each denominator separately and then taking an unbounded least common multiple.
It does not identify I with the group's exponent or with a particular packet's actual denominator.

The partition proof is the classical box-pigeonhole idea, here applied to the actual coefficient quotient.
Earlier [C57's finite-grid argument](Yin_C_G0057_v1.md#effective-integer-floor-conditioning) and [EPF26's selected Dirichlet attribution](../audits/literature/EPF26/readme.md#dirichlet-simultaneous-selected-attribution) were read.
That source supplies attribution only; its handwritten Minkowski proof was not accepted and is not needed.
The present local proof uses no uninspected geometric theorem, algorithm or source-wide acceptance.
C57's Gram eigenvalue and C59's finite packet dictionary are different conclusions and remain credited at their old scopes.

<a id="fixed-rank-full-packet-rigidity"></a>
## 3. Any complementary packet on the independent dictionary

Fix ANY finite indexed family of rational Laurent polynomials f_b supported in the SAME set{a_1,...,a_r}, with every value f_b(alpha) NONZERO in O0 and positive normalized rational weights omega_b.
Let q be the actual least common coefficient denominator and M the FINAL indexed weight denominator.
Theorem1 gives q dividing I and hence

    q<=I<=Q_r<=5R_r.                                        (6)

Every common normalization shifts all exponents together and changes none of this quotient or absolute norm information.

**Theorem 2.**
At A*m/d<=kappa_r:

(a) No such family can have weighted coefficient squared energy E=sum_b omega_b||f_b||_2^2<1, even without lag equations.

(b) If it additionally satisfies the EXACT Laurent complementarity sum_b omega_b f_b(t)f_b(t^-1)=1, then every TRUE f_b is a signed monomial.
Its actual q is1 and its complete original norm income/surplus is0.

For(a), the accepted [C50 below-one coefficient-denominator theorem](Yin_C_G0050_v1.md#statement), PartD, applies to this actual O0 family after a common monomial normalization.
If actual union width T=0, each nonzero rational multiple of the shared unit is an integer coefficient of absolute value at least1, immediately excluding E<1.
Otherwise T<=A and C50 gives

    q^4[epsilon(T*m/d)+6T*m/d]>=1.                          (7)

But q<=5R_r, monotonicity and(2) give a STRICT upper bound less than1: (5R_r)^4 times the bracket at U is at most (5R_r)^8 times the bracket at2U, which is less than1.
Thus(a) follows.
The theorem does not assume a fixed below-one deficit or minimum atom weight.

For(b), the actual all-weight E1 conclusion of [C71](Yin_C_G0071_v1.md#statement) gives either the claimed signed-monomial alternative or

    q^8[epsilon(2T*m/d)+12T*m/d]>=1,

which contradicts the same(2)/(6) bound.
T0 is handled as above by positive weighted integer squares.
This is the old C71 selector applied AFTER the new coefficient-index bound, not a new selector theorem.
All independent-power and original-order hypotheses have been checked; no norm-only surrogate for membership is used.

The theorem concerns every supplied rational complementary packet on the dictionary, not only packets obtained by a matrix or any finite search.
It does not assert that E1 alone without lag cancellation forces monomial polynomials.
Part(a) uses only coefficient energy, while(b) uses the full covariance identity.
It says nothing about packets with E>1 or linearly dependent dictionaries, or the existence of a short independent dictionary for an unrestricted target.

<a id="fixed-rank-constant-word-corollary"></a>
## 4. Rational constant blocks and arbitrary legal word length

Let B be ANY rational CONSTANT isometry of a finite positive RATIONAL diagonal metric, B^T D B=D.
Apply it to signed monomial inputs whose selected block uses at most r DISTINCT Q-independent powers with common spread A.
All selected output values must be NONZERO in O0.
The outputs remain supported on that same dictionary; their positive normalized weighted covariance is1.
At A*m/d<=kappa_r, Theorem2 forces every TRUE output polynomial to be a signed monomial, so its exponent already occurred in the selected block.
Matrix entries need not be integral when input powers repeat.

The same conclusion is uniform over any finite length, number of labels N and fixed positive rational weights.
Permit arbitrary finite interleavings of these constant blocks with the adopted [C84 primitive weighted binary delays](Yin_C_G0084_v1.md#statement), including either signed delay k and optional single-coordinate shifts.
Each constant block must use at most r distinct CURRENT exponents, whose corresponding powers are Q-independent.
For a block of s<=r powers one may use the r-dimensional bound directly with empty coordinates, or note H_s^s<=H_r^r and R_s<=R_r; no favorable monotonicity of an unspecified constant is assumed.

Keep EVERY intermediate actual coordinate nonzero in O0, all labels and weights fixed, and set

    B_word=A_init+sum_(all delayed factors)|k|,
    B_word*m/d<=kappa_r.                                    (8)

Then every TRUE intermediate polynomial is a signed monomial.
Constants introduce no new exponents; each binary delay uses exactly its C84 formula and enlarges the common interval by at most|k|.
Since kappa_r<=K0, C84 applies at every stage.
The current local cost is bounded by B_word, proving induction without replacing true polynomials by arbitrary representatives.
Constant signs may change.
There is no bound on the actual constant-matrix denominator, direction height, label count, FINAL M or number of stages as an extra hypothesis.

This class still has an explicit local Q-independence gate at general r.
For r<=3 the adopted C87 can discharge it under the larger K0 threshold; the separate four-power author program has its own review status.
Neither is needed as an unadopted premise here.
A rational factorization of an arbitrary paraunitary matrix need not preserve the local independence or intermediate integrality requirements.
No all-matrix classification or unrestricted gap follows.

<a id="fixed-rank-costs-and-positive-control"></a>
## 5. Every original cost and the exact old-input index control

For a supplied general packet after ONE common shift to nonnegative support, put F_b=qf_b in Z[t], m_b=M omega_b positive integers and D_b=Norm_K(f_b(alpha)), all signed and nonzero.
Then

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(m_b)=q^(dM)product_b D_b^(m_b),
    S_int=q^2 E,
    Lambda=(1/d)sum_b omega_b log|D_b|,
    I_int=log q+Lambda,
    surplus=Lambda-(1/2)log E.                             (9)

If unshifted values were used for D_b, the right side also includes the precise common factor nu^(bM) for shift t^b.
Contents remain inside each integer F_b; no primitive-part norm replaces its full resultant.
Index I in(4) is an additive quotient order and is not the final weight denominator M, energy S_int or income I_int.
For E1 under Theorem2, actual q1 and true signed-monomial D_b have absolute value1, so Lambda=surplus=0.
All indexed copies stay present.

For a general word before rigidity is concluded, the actual output coefficient denominator divides the product of actual entry denominators of its constant matrices and the exact C84 delay denominators L.
It may be much smaller; under(8) it is1.
Actual final union width is at most B_word, FINAL M/copies remain fixed, and the final signed norms are (epsilon'_b)^d nu^(a'_b).
No determinant or initial copied exponent sum is substituted for those actual values.
The cumulative condition cannot be replaced by final width after large cancellations.

The small-cost hypothesis matters even at rank2.
Reuse the actually adopted [C87 golden-ratio control](Yin_C_G0087_v1.md#statement), P=t^2-t-1, alpha^5=3+5alpha, d2 and nu-1.
The two powers1,alpha^5 are independent, and

    x+y alpha^5 belongs to Z[alpha]
        iff x+3y belongs to Z and5y belongs to Z.

Thus the ACTUAL coefficient quotient has exactly5 cosets, generated by(-3/5,1/5).
Indeed y mod1 has precisely the five possibilities j/5 and x mod1 is then determined.
At r2, H_r2 and Q_r4, so I5 EXCEEDS the claimed small-cost bound outside its domain.
The representative(2/5,1/5) has value(2+alpha^5)/5=1+alpha, a unit with signed norm+1 and coefficient energy1/5.
Its width5 gives U=(5/2)log alpha>K0>=kappa_2.
This is an exact fixed-input countercontrol to dropping the small-U premise, not a near-one family.

The same accepted constant rotation B=(1/5)[[3,4],[-4,3]] on(1,t^5), weights1/2, has nonzero integer outputs3+4alpha and1+3alpha of norms5,-5; actual q5/M2/E1/T5, signed numerator resultants125,-125 and copied product-15625, income/surplus(1/2)log5>0.
These are the old C87 hand controls, credited rather than claimed new.
The new quotient computation explains exactly why this fixed input fails the bounded-index hypothesis.
No new native calculation or source theorem is involved.

<a id="fixed-rank-source-limits-and-freeze"></a>
## 6. Review target, reuse and remaining problem

The new contribution is the uniform bound on the ENTIRE actual coefficient quotient and the simultaneous denominator it supplies to arbitrary finite packets, followed by its fully charged use of OLD C50/C71.
The box argument is elementary classical pigeonhole reasoning and is proved in full here.
The already accepted C74 numerical derivation was authored by root and independently reviewed; using it does not independently certify this new argument.
Root also authored C87's control and other small-block proofs; these ancestor contributions are explicitly separate from the current proof authorship.

Author checking covers injectivity from the exact dictionary independence, half-open representatives and strict small-box difference, width0, all r-dependent inequalities, finiteness without assuming a lattice determinant, the finite-group summation proof that one I clears ALL coefficients, q versus M, actual T versus declared A, separate no-lag E<1 and full-lag E1 branches, every stage of true-polynomial induction, original signed/resultant scalars and the exact quotient/control calculation.
The existing EPF26 selected account was read only for the already recognized Dirichlet attribution; no new source acquisition, byline/date inference, source-proof adoption, native program or enumeration occurred.

For every FIXED r and fixed C, this supplies a positive threshold kappa_r/C below which no nontrivial E1 packet on an actual independent r-power dictionary of span<=Cd exists.
Dependence, growing dictionary size and E>1 remain possible exits, not constructed successes.
The exact same-exponent arithmetic-income gate and all-input near-one coverage remain unresolved.
This is AUTHOR self-check only, awaiting a separate noncontributor WHOLE review of the entire actual draft.


<a id="fixed-rank-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T17:46.
Freeze the ENTIRE actual draft including the original candidate, all six sections, both theorems, equations1--9, fixed-rank constants, exact inherited control and new quotient computation, classical attribution and all source/contributor/independence limits.
No Claim adoption or mathematical completion is asserted.


<a id="fixed-rank-dated-author-correction"></a>
## Dated author correction after the actual negative whole finding

2026-10-12T17:54.
Root has read the ENTIRE [R320 initial whole finding](../audits/reviews/Yin_R_G0320_v1.md#fixed-rank-whole-initial-finding), which remains changes required at its original01:46:38 target and is not rewritten.
Make exactly its two bounded author repairs.
F1: the original control sentence said "a unit with signed norm-1 and coefficient energy1/5"; the corrected signed norm is+1 because1+alpha=alpha^2 and Norm(alpha)=-1.
Its integer numerator2+t^5 has original degree-two resultant+25 if priced separately.
The actual value, quotient index5, coefficient vector, denominator5, energy1/5, old rotation norms5/-5 and outside-threshold conclusions are unchanged.
F2: the original standalone block sentence said "finite positive diagonal metric"; it now explicitly says "finite positive RATIONAL diagonal metric", matching Theorem2 and the already rational-weight word theorem.
No broader real-weight claim is added.
The original freeze is retained above as historical verification, not retroactively certified.
All formulas1--9, constants, proofs and other costs remain as in the inspected draft.

<a id="fixed-rank-corrected-entire-author-freeze"></a>
## Corrected entire author freeze

2026-10-12T17:54.
Freeze the ENTIRE corrected draft plus the exact original-text correction account above for actual independent recheck.
Root is its author, not its independent reviewer.
R320 remains the original negative finding; no automatic PASS, extraction, adoption or mathematical completion is inferred.
