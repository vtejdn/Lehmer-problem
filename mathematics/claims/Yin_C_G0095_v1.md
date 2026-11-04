---
author: Yin
---
# Eight-power coefficient quotient types and the quarter-class energy boundary

Date: 2026-10-13T03:45.
Human author Yin.
Root authored the ENTIRE D50 proof and its 11:34 freeze.
The separately assigned eight-power reviewer independently whole-reviewed that original in R327 and NOW authors this exact statement/extraction wrapper, becoming a contributor to this new artifact.
R327 remains original whole-proof evidence only.
A different noncontributor must inspect this ACTUAL statement, retained body and interfaces before adoption.
Initial assessment is proof draft / under review.
The entire original question, reuse/candidate text, Sections 1--7, equations (A)--(B), source/control boundaries, author checking and freeze are retained below without mathematical changes.

## Statement

Fix an ACTUAL nontorsion algebraic integer unit alpha with monic irreducible minimal polynomial P, ORIGINAL degree d>=2, K=Q(alpha), O0=Z[alpha], total logarithmic Mahler measure m=log M(P)>0 and nu=Norm_(K/Q)(alpha) in {+1,-1}.
All norms and radial sums use ALL d original embeddings.
Negative powers belong to the SAME O0.
Reciprocity, coefficient flatness and a maximal-order replacement are not assumed.

Retain the accepted quantities

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log(sqrt(c0/u))},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0,
    K0=c0/[2*36^8*5^64].

The functions are used only in their positive increasing domain.
The exact numerical margins are

    K0<h0/2, K0<1/10000,
    epsilon(K0)<5^-8<1/100000,
    5^8[epsilon(2K0)+12K0]<1.

Zero width is treated directly, without epsilon(0).
L229's accepted actual powered-degree and Pri11/Dim19 source limits are retained.

**A. Automatic independence and strict intermediate coefficient floor.**
Let 1<=r<=8 and let a_1,...,a_r be DISTINCT integers, with span A=max a_i-min a_i and U=A*m/d<=K0.
Then alpha^(a_1),...,alpha^(a_r) are Q-linearly independent, without an extra r<=d premise.
Define

    L={x in Q^r: sum_i x_i alpha^(a_i) belongs to O0},
    Z^r subset L, H=L/Z^r.

Every nonzero x in L satisfies ||x||_2^2>99/100, including after subtraction of any integer vector.

The independence argument compares a rational zero relation's lower phase Gram energy with its squared radial error and would force 1<=7epsilon(U)+16U<1.
It does not apply a nonzero-resultant norm floor at zero.
For a NONZERO value of a rational Laurent f on this dictionary, after its actual coefficient denominator is cleared and canceled in L229, positive true width gives

    1<=abs Norm_K(f(alpha))^(2/d)
      <=||f||_2^2 exp(2U)[1+7epsilon(U)+32U].

The multiplier is strictly less than100327/99980 and its product with99/100 is below one.
At width zero the rational coefficient belongs to O0 intersect Q=Z.
Common monomial normalization uses an O0 unit and retains its signed full norm.

**B. Exhaustive NECESSARY quotient types and exact supports.**
The ENTIRE H is finite and is one of

    0, Z/2, (Z/2)^2, Z/4.

These are necessary possibilities, not a realization theorem.

- For H=Z/2 its sole nonzero class has w half coordinates with 5<=w<=r<=8.
- For H=(Z/2)^2, necessarily r=8 and all positions are active.
  Its three nonzero binary support weights are5,5,6.
  For the two weight-five generators the coordinate types10,01,11 occur respectively3,3,2 times, up to coordinate permutation and choice of those generators.
- For H=Z/4, necessarily r=8.
  Each generator has five exact quarter coordinates, with nearest residues+/-1/4, and three half coordinates.
  Both order-four cosets have nearest squared norm17/16.
  Their common double has five half coordinates and nearest squared norm5/4.
  No additional independent half direction occurs.

Individual rational classes have finite order without prior finiteness of H.
For an order-p class, p odd prime, with s active coordinates, the average nearest squared norm over its p-1 NONZERO multiples is s(p+1)/(12p)<=8/9.
A weight-four half class supplies ALL sixteen sign polynomials with four coefficients+/-1/2 and weights1/16: every value is nonzero in O0, actual q2, FINAL M16, exact Laurent covariance1 and the actual common width.
C71 at q2 contradicts C74's strict doubled-parameter margin.
Thus every nonzero half class has weight at least five.

An order-eight class would double to the displayed quarter type and have nearest squared norm at most57/64, contradicting A.
Excluding higher powers of two and odd factors gives 4H=0 and embeds H into finite (Z/4)^r before kernel/image counting.
An order-four generator permits only its own double as a nonzero half class, forcing cyclicity.
Otherwise H is a binary space of dimension at most two with the displayed support pattern.
For r<=7 the necessary types reduce to0 or Z/2; this is a consequence of the present proof, without using D48 as a premise.

**C. True denominators, energy and positive weights without lag cancellation.**
Every vector in L has collected coefficient denominator dividing four; it divides two in the elementary binary cases.
Therefore the ACTUAL common coefficient denominator q of any finite family on this dictionary divides four.
This does not bound raw matrix-entry denominators or the FINAL indexed weight denominator M, and does not identify q with the group order or exponent for every family.

Every rational Laurent f on the dictionary with NONZERO value in O0 satisfies

    ||f||_2^2>=1,
    equality holds exactly for a TRUE signed monomial,
    every TRUE nonmonomial has ||f||_2^2>=17/16.

The zero coset has nonzero integer energy at least1 and nonmonomial integer energy at least2.
Nonzero half cosets have nearest energy at least5/4; quarter cosets have nearest energy17/16.
Other representatives cannot improve the nearest-residue norm.
For r<=7 the nonmonomial floor is5/4.
No actual attainment of a nontrivial quotient or of17/16 is asserted.

For any finite indexed family f_i with union dictionary as in A, every value nonzero in O0, and positive rational weights omega_i summing1, put

    E=sum_i omega_i ||f_i||_2^2,
    theta=sum_(i: f_i is a TRUE nonmonomial) omega_i.

Then E>=1+theta/16 and theta<=16(E-1).
Thus E<1 is impossible and E=1 forces EVERY atom to be a TRUE signed monomial, WITHOUT a Laurent lag-cancellation hypothesis, minimum positive weight or bound on the number of indexed labels.

**D. Exact constant blocks and permitted binary delays.**
Fix any finite labels with positive rational weights omega_i summing1 and their ACTUAL least indexed denominator M, starting at TRUE signed monomials epsilon_i t^(a_i).
A permitted rational CONSTANT block B preserves the SAME selected diagonal weight metric,

    B^T diag(omega_i in the block) B=diag(omega_i in the block),

and its CURRENT true monomial inputs use at most eight distinct exponents.
Block weights may be normalized by their positive total when applying C.
If their span times m/d is at most K0 and every output value is nonzero in O0, every TRUE output is a signed monomial on that SAME exponent dictionary.
Constants may change signs.
Repeated exponents do not force the whole constant matrix to have integer entries.

Interleave such blocks with exactly C84's adopted binary factors.
At a selected pair's coprime positive integer relative weight ratio u:v and primitive integer direction(x,y), xy nonzero, set

    S=u*x^2+v*y^2, c_g=gcd(abs(u*x),abs(v*y)),
    A1=u*x/c_g, B1=v*y/c_g, L0=S/c_g,
    Pi=(1/L0)[[x*A1,x*B1],[y*A1,y*B1]],
    B_delay(t)=Id-Pi+t^k Pi, k in Z minus{0}.

Optional one-coordinate signed monomial shifts are allowed.
Labels and weights stay fixed.
These are specified factors, not arbitrary rational nonconstant matrices or an assertion that every paraunitary matrix has a legal factorization.

**E. Entire finite words at cumulative cost.**
Require EVERY actual coordinate at EVERY stage, including unchanged coordinates, to belong to the SAME O0 minus{0}.
Let

    B_word=initial global exponent span
           +sum abs(k) over EVERY binary delay and optional coordinate shift.

If B_word*m/d<=K0, EVERY TRUE intermediate polynomial is a signed monomial, actual final q1, E1 and T_final<=B_word.
This holds for any finite label count, word length, exponent multiplicities, fixed positive weight ratios/FINAL M and rational constant or primitive binary heights, with at most eight CURRENT distinct exponents in each selected constant block.
This is a local block restriction; the global dictionary need not have at most eight powers.

Constants introduce no new exponent; binary delays and optional shifts enlarge the common interval by at most their absolute shift.
Pair span plus the next abs(k) is charged before applying C84.
Induction acts on TRUE monomial polynomials and never inserts a value-equivalent representative into an old covariance identity.
Width-zero constant steps use rational O0 integers and positive weights.

For final outputs epsilon_i' t^(b_i),

    Norm_K(f_i(alpha))=(epsilon_i')^d nu^(b_i),
    Lambda=(1/d)sum_i omega_i log abs Norm_K(f_i(alpha))=0,
    full surplus=Lambda-(1/2)log E=0.

Any positive final income in this specified word class requires the STRICT price B_word*m/d>K0.
If B_word<=C*d for a fixed C>0, it requires m>K0/C.
The paid cumulative budget can exceed the physical final width; this is a construction-class price, not a final-width-only theorem or an unrestricted Mahler gap.

**F. Complete original signed costs and fixed control.**
Keep m_i=M omega_i as positive indexed integer copies and every label.
In E let b=min_i b_i.
After the ONE common normalization t^(-b),

    Res(P,epsilon_i' t^(b_i-b))=(epsilon_i')^d nu^(b_i-b),
    full copied product=product_i[(epsilon_i')^d nu^(b_i-b)]^(m_i),
    abs(full copied product)=1.

FINAL M and all copies remain unchanged.
Constants may change the final signs; no determinant is substituted for the product of coordinate norms.

For a general family in C, first normalize all Laurent supports by ONE common monomial, then use f_i and D_i=Norm_K(f_i(alpha)) in THAT same normalization.
With actual common q dividing4,

    Res(P,qf_i)=q^d D_i,
    product_i Res(P,qf_i)^(m_i)=q^(dM)product_i D_i^(m_i).

All contents, full signed degree-d norms and physical width remain.
A common shift t^c contributes nu^c per raw norm and nu^(cM) to the copied product.
A general nonmonomial atom is not asserted to have unit norm.

The accepted C87 golden-unit control remains: P=t^2-t-1, alpha=(1+sqrt5)/2, d2, weights1/2,1/2, seed(1,t^5) and B=(1/5)[[3,4],[-4,3]] have actual q5, FINAL M2, E1, signed norms5,-5, width5 and surplus(log5)/2.
Its fixed paid U=(5/2)log alpha>K0, so it is outside the theorem.
This is an existing control, not a new near-one family.

**G. Source and unresolved scope.**
L229 supplies its actual finite phase and nonzero-resultant coefficient-energy inputs with retained Pri11/Dim19 statement/applicability limits and powered multiplicities.
C74 supplies the numerical margin, C71 the complete sign-packet E1 contradiction, C84 exactly the binary local interface and C87 the stated control.
No new external theorem or native computation is a premise.

Classical binary averaging is attributed through [Que08's selected source record](../audits/literature/Que08/readme.md#plotkin-selected-attribution).
The Queen Mary Spring2008 HTML lecture-log statements were read online; the detailed source proof and original Plotkin1960 paper were not inspected.
Bounded registration retrieval failed DNS and supplies no local artifact.
This is attribution for the complete local counting proof, not an additional external proof premise or source-wide acceptance.
No individual source author is inferred from its URL.

D48 motivates the inquiry and retains its separate review; it is not a proof input.
Adopted C90/C92 give fixed-rank results at rank-dependent thresholds and remain comparisons.
There is no nine-power result, realization classification, actual quarter extremizer, growing-rank uniformity, general all-overorder extension, same-exponent positive-income construction, all-input near-one coverage or unrestricted G0001 completion.
Changing labels/weights, nonmonomial seeds, zero or nonintegral intermediate values, maximal-order-only legality, arbitrary other nonconstant factors and small final width after large cumulative expense remain outside the word statement.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T03:45 |
| status | open |
| reason | Register the exact same-K0 at-most-eight-power necessary quotient classification, energy/positive-weight bounds, specified legal cumulative-word obstruction and signed costs, retaining the ENTIRE original D50. R327 independently whole-reviewed only the original11:34 freeze. Its reviewer authors this new wrapper and is now a contributor; a distinct noncontributor must inspect the ACTUAL extraction before adoption. No realization, stronger rank or unrestricted result is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--G, actual O0/unit/degree domain, r<=8 and same K0, necessary types/supports, intermediate/final floors, positive weights, exact legal words, costs/control/source and exclusions. |
| argument | [Entire retained original](#argument) | COMPLETE original D50 question/reuse/candidate, Sections1--7/(A)--(B), all eight original explicit anchors, source/control/contributor boundaries and11:34 freeze. |
| dependency | [L229 angular coherence](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Finite ORIGINAL phase moments, exact positive-domain epsilon and actual powered degree/d/N repetitions; used before any nonzero-resultant condition. |
| dependency | [L229 coefficient-energy bound](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Only nonzero values after actual denominator clearing and common monomial normalization, full degree-d norm, actual S/rho/width and radial expense. |
| dependency | [C74 numerical margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | R=1 exact K0/h0 and doubled-parameter strict bound, plus the elementary epsilon estimate; no older word theorem is used. |
| dependency | [C71 all-weight E1 statement](Yin_C_G0071_v1.md#statement) | Only PartA for the COMPLETE sixteen-sign half-weight-four packet, actual q2, FINAL M16, nonzero O0 values, common width and q^8 contradiction. |
| dependency | [C84 local binary classification](Yin_C_G0084_v1.md#statement) | Primitive weighted two-coordinate delays, arbitrary nonzero signed k, true monomial local action, original-order nonzero legality and paid pair span plus abs(k). |
| dependency | [C87 golden-unit control](Yin_C_G0087_v1.md#statement) | Only PartE's matrix, seed, q5/M2/E1/width5, signed norms5,-5 and fixed outside-domain surplus. |
| dependency | [Pri11 accepted statement](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Through L229 ONLY: retained integer/simple-zero/actual N>=55, real compact Lipschitz test and original statement/applicability limits. |
| dependency | [Retained house source unit](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Through L209/L229 ONLY: this unit's house subsection and retained Dim19 v1 actual-powered-degree house-to-height consequence; no new proof or later-version adoption. |
| support | [Original entire finding](../audits/reviews/Yin_R_G0327_v1.md#eight-power-entire-independent-finding) | ENTIRE original11:34 D50 reviewed before this wrapper existed; not an actual extraction finding for this new statement. Finding relationship: self-reviewed. |
| support | [C90 fixed-rank comparison](Yin_C_G0090_v1.md#statement) | Existing independent-dictionary result with rank-dependent threshold; comparison only. |
| support | [C92 automatic fixed-rank comparison](Yin_C_G0092_v1.md#statement) | Existing automatic-independence assembly at rank-dependent thresholds; no growing-rank consequence is borrowed. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:00 |
| status | proved |
| reason | Adopt original entire D50 finding R327 and distinct actual C95 extraction finding R331. The same-K0 at-most-eight-power necessary quotient types and exact support restrictions, coefficient energy17/16, positive-weight estimate, actual q/M/signed costs and specified legal cumulative-word theorem are fixed at their original-order scopes. Root authored the original proof and relies on separately organized noncontributor findings. No nontrivial quotient realization, sharp realized energy, nine-power/growing-rank uniformity or unrestricted positive-income/gap conclusion is inferred. All original history and source limits remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--G, actual O0/unit/degree domain, r<=8 and same K0, necessary types/supports, intermediate/final floors, positive weights, exact legal words, costs/control/source and exclusions. |
| argument | [Entire retained original](#argument) | COMPLETE original D50 question/reuse/candidate, Sections1--7/(A)--(B), all eight original explicit anchors, source/control/contributor boundaries and11:34 freeze. |
| dependency | [L229 angular coherence](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Finite ORIGINAL phase moments, exact positive-domain epsilon and actual powered degree/d/N repetitions; used before any nonzero-resultant condition. |
| dependency | [L229 coefficient-energy bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Only nonzero values after actual denominator clearing and common monomial normalization, full degree-d norm, actual S/rho/width and radial expense. |
| dependency | [C74 numerical margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | R=1 exact K0/h0 and doubled-parameter strict bound, plus the elementary epsilon estimate; no older word theorem is used. |
| dependency | [C71 all-weight E1 statement](Yin_C_G0071_v1.md#statement) | Only PartA for the COMPLETE sixteen-sign half-weight-four packet, actual q2, FINAL M16, nonzero O0 values, common width and q^8 contradiction. |
| dependency | [C84 local binary classification](Yin_C_G0084_v1.md#statement) | Primitive weighted two-coordinate delays, arbitrary nonzero signed k, true monomial local action, original-order nonzero legality and paid pair span plus abs(k). |
| dependency | [C87 golden-unit control](Yin_C_G0087_v1.md#statement) | Only PartE's matrix, seed, q5/M2/E1/width5, signed norms5,-5 and fixed outside-domain surplus. |
| dependency | [Pri11 accepted statement](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Through L229 ONLY: retained integer/simple-zero/actual N>=55, real compact Lipschitz test and original statement/applicability limits. |
| dependency | [Retained house source unit](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Through L209/L229 ONLY: this unit's house subsection and retained Dim19 v1 actual-powered-degree house-to-height consequence; no new proof or later-version adoption. |
| support | [Original entire finding](../audits/reviews/Yin_R_G0327_v1.md#eight-power-entire-independent-finding) | ENTIRE original11:34 D50 reviewed before this wrapper existed; not an actual extraction finding for this new statement. Finding relationship: self-reviewed. |
| support | [C90 fixed-rank comparison](Yin_C_G0090_v1.md#statement) | Existing independent-dictionary result with rank-dependent threshold; comparison only. |
| support | [C92 automatic fixed-rank comparison](Yin_C_G0092_v1.md#statement) | Existing automatic-independence assembly at rank-dependent thresholds; no growing-rank consequence is borrowed. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0331_v1.md#c95-eight-power-actual-extraction-finding) | Entire actual statement, complete retained original and all precise coefficient/group/weight/word/norm/source interfaces and preservation; distinct noncontributor actual review. |

## Registration and complete preservation

This extraction organizes the already complete [original D50 freeze](#eight-power-entire-author-freeze) for fixed reuse, with no mathematical extension or adoption.
Root owns the original proof.
The R327 reviewer writes this wrapper and cannot independently certify this artifact.
A distinct actual extraction review remains necessary.

The ENTIRE original body follows.
Only duplicate front matter is represented once, the first original title is demoted by one hash, and newline/boundary whitespace is normalized.
Existing ../claims/ and ../ledger/ links resolve here without rebasing.
Every candidate assertion, historical pending-review sentence, scope distinction, derivation, source note, control and author freeze survives.
Historical sentences retain their dated meaning; the selected assessment above governs this new artifact.

The wrapper's Que08 locator identifies the same inspected HTML attribution and adds no proof premise.
R327 is preserved at its original scope.
This registration edits no original D or earlier C/R and performs no retirement.
Root retains later actual review/adoption/shared-navigation/consumer-relocation coordination.

## Argument

## Eight-power coefficient quotients and the quarter-class energy boundary

Date: 2026-10-13T03:32.
Human author Yin.
Root is the author of this new inquiry under the explicitly resumed G0001 Task.
The preserved seven-power D48 remains under separate whole review; it motivates this inquiry but is not an accepted proof premise.
Root owns this draft; the independent D48 reviewer does not contribute to its proof.

## Question, reuse and candidate scope

At the SAME accepted K0 and actual original-order domain, determine what changes for a dictionary of at most EIGHT distinct powers.
The local search of current C/L/D materials for eight-power, order-four quotient and binary-code bounds found the unreviewed D48 boundary, adopted C90/C92 fixed-rank bounds (with rank-dependent threshold), and the existing C71/C74/C84 interfaces.
Those provide sufficient tools for a direct extension attempt, without reopening their proofs or claiming novelty of elementary finite residue/linear-code counting.

The candidate group L/Z^r may now allow cyclic order4 and a binary group of rank2.
Proposed exact necessary types are 0, Z/2, (Z/2)^2 and Z/4; a cyclic order4 generator must have five quarter coordinates and three half coordinates.
Proposed nonmonomial energy floor is17/16, giving nonmonomial positive-weight mass at most16(E-1) and energy-one rigidity without lag cancellation.
These are UNREVIEWED candidate assertions until the complete proof and independent review below are supplied.
No actual realization of a nontrivial quotient is asserted.
No all-input income, growing-rank uniformity or unrestricted gap follows.

The next proof obligations are the same-K0 strict99/100 coefficient floor for r<=8; correct nonzero cyclic averages excluding odd primes; half-weight4 exclusion using the exact complete C71 sign packet; classification/exclusion of orders4/8; and the actual positive-weight and cumulative-cost word interfaces.
No native computation or source acquisition is started.
All accepted-source scopes remain those of L229/C71/C74/C84.

<a id="eight-power-domain-and-floor"></a>
## 1. Exact original domain and local floor

Let P be an actual monic irreducible nontorsion integer-unit polynomial, alpha a root, K=Q(alpha), ORIGINAL degree d>=2, O0=Z[alpha], total logarithmic measure m>0, and nu=Norm_K(alpha) in {+1,-1}.
Fix r distinct integer exponents a_i, 1<=r<=8, of span A and U=A*m/d<=K0.
Put

    L={x in Q^r: sum_i x_i alpha^(a_i) belongs to O0},
    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log(sqrt(c0/u))},
    epsilon(u)=min{1,15sqrt(b(u))+4u},
    K0=c0/[2*36^8*5^64].

The actual accepted [L229 phase and nonzero-resultant bounds](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) and [C74 numerical margin](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) give K0<h0/2, K0<1/10000 and epsilon(K0)<5^-8<1/100000, together with 5^8[epsilon(2K0)+12K0]<1.
Monotonicity is used only on the original positive domain.
Write alpha_j=r_j z_j, abs(z_j)=1; ALL original embeddings satisfy sum_j abs(log r_j)=2m.

The powers are automatically Q-independent.
For a nonzero rational relation F(alpha)=0, normalize its actual support to width T<=A and put S=sum c_i^2, rho=(sum abs(c_i))^2/S<=8.
The lower phase Gram bound is

    d^-1 sum_j abs(F(z_j))^2 >= S[1-(rho-1)epsilon(U)].

Every F(alpha_j)=0.
Dividing it by max(1,r_j)^T and comparing each normalized radial coefficient with 1 bounds the same average by 2rho*S*T*m/d<=2rho*S*U: pointwise the squared error is at most (sum abs(c_i))^2 min(1,T abs(log r_j))^2, and min(1,v)^2<=v.
A relation would force 1<=7epsilon(U)+16U<7/100000+16/10000<1.
Width zero involves one nonzero monomial and is impossible directly.
This argument uses no norm floor at resultant zero and proves independence even when an a priori r<=d assumption is absent.

For nonzero x in L, independence ensures f(alpha)!=0 for f=sum x_i t^(a_i).
Normalize its actual support, let q be the true coefficient denominator, T the true width and S=||f||_2^2.
All negative powers are units in O0, so the normalization preserves membership and nonvanishing.
If T=0 then f(alpha)=c alpha^a in O0 forces c in O0 intersect Q=Z, hence S>=1.
Otherwise the integer auxiliary qf has Res(P,qf)=q^d Norm_K(f(alpha)), where the normalized f and its unit sign are used consistently.
Cancel q in L229 to obtain

    1<=abs Norm_K(f(alpha))^(2/d)
       <=S exp(2U)[1+7epsilon(U)+32U].

Set D8(U)=exp(2U)[1+7epsilon(U)+32U].
The elementary exp(v)<=1/(1-v) gives

    D8(U)<(5000/4999)*(100327/100000)=100327/99980,
    (99/100)*(100327/99980)=9932373/9998000<1.

Consequently EVERY nonzero x in L has ||x||_2^2>99/100.
This includes subtraction of arbitrary integer vectors: the resulting vector stays in L and its value cannot vanish unless the vector itself is zero.
The entire proof retains actual O0 and all d original norms; a maximal-order replacement is not made.

<a id="eight-power-odd-and-half-classes"></a>
## 2. Every odd order is excluded; half classes have weight at least five

Each class in H=L/Z^r has finite order because each representative is rational.
No initial finiteness of H is assumed.
An order divisible by an odd prime p would give an order-p class.
For its coordinatewise nearest representatives y_k, k=0,...,p-1, each of s<=8 nonzero coordinates has exact total squared residue sum (p^2-1)/(12p); this follows directly by summing 2 sum_{j=1}^{(p-1)/2}(j/p)^2.
Thus the average over the NONZERO k is

    (p-1)^-1 sum_{k=1}^{p-1} ||y_k||_2^2
       =s(p+1)/(12p)<=8/9<99/100.

All those representatives are nonzero in L, a contradiction.
Using the average over nonzero classes is essential: the coarser seven-coordinate comparison from D48 would not exclude p3 at r8.
Hence every class has power-of-two order.

A nonzero order-two class has nearest representative with w half coordinates, of energy w/4>99/100, so w>=4.
Exclude w4 by the exact sixteen-sign construction: for its four actual exponents J retain ALL g_sigma=(1/2)sum_{i in J}sigma_i t^(a_i), each weight1/16.
Sign changes alter coefficients by integers, so every value is in O0, and independence makes all sixteen nonzero.
Their exact Laurent covariance is 1, with actual q2, FINAL M16 and common width T_J<=A.
The full signed norms D_sigma are nonzero integers and the copied integer-resultant product is 2^(16d) product_sigma D_sigma after common normalization.
[C71 Part A](Yin_C_G0071_v1.md#statement) requires 2^8[epsilon(2T_J*m/d)+12T_J*m/d]>=1, contradicting the strict C74 margin at K0.
Thus every nonzero half class has Hamming weight at least five.
This uses O0 as required by C71 and claims no all-overorder extension.

<a id="eight-power-quarter-class-classification"></a>
## 3. Exact order-four and higher-order restrictions

For an order-four class choose a nearest representative y.
Let n4 count coordinates of exact denominator4 and n2 those of exact denominator2.
Its double is a nonzero half class, so n4>=5; also n4+n2<=8.
Its actual nearest squared norm is

    ||y||_2^2=n4/16+n2/4>99/100.

Thus n4+4n2>=16.
If n4>=6, the left side is at most n4+4(8-n4)=32-3n4<=14, impossible.
Hence n4=5, and n2 must equal3.
Necessarily r=8 with no integral coordinate.
The two order-four cosets have nearest norm17/16; their double has nearest norm5/4.
This classification does not claim actual algebraic realization.

There is NO order-eight class.
Its double would have the preceding order-four type, forcing five exact denominator8 coordinates and three exact denominator4 coordinates in a representative x.
In nearest residues the first five have abs<=3/8, and the last three have abs=1/4.
Therefore

    ||x||_2^2<=5*(3/8)^2+3*(1/4)^2=57/64<99/100,

a contradiction.
A class of any higher power-of-two order would have an order-eight multiple.
Combined with Section2, every class has order dividing4.
It follows, without any prior lattice compactness theorem, that H embeds in the finite group (Z/4)^r.

Suppose H contains an order-four class y with quarter-coordinate set Q of size5 and half-coordinate set B of size3.
For any order-two z, adding its half coordinates changes a quarter residue only between +/-1/4, while a half residue on B becomes integral.
If z has k supported coordinates in B, a nearest representative of y+z has norm

    5/16+(3-k)/4=17/16-k/4.

The class y+z has order4, so its representative is nonzero and the floor forces k=0.
Every nonzero z has weight>=5 and is then supported entirely on Q, hence equals2y.
The doubling map H->H[2] therefore has image {0,2y} and kernel H[2]={0,2y}.
Since H is finite, it has order4 and H=<y> is CYCLIC, not a larger group with an extra half direction.

<a id="eight-power-binary-alternative"></a>
## 4. Elementary binary alternatives and classical attribution

If there is no order-four class, H is a binary linear code in (F2)^r, with every nonzero word of weight>=5.
It cannot contain three independent words: in the resulting eight-word subcode every active coordinate occurs in exactly four words, giving total nonzero-word weight<=4r<=32, whereas seven nonzero words each have weight>=5, giving total>=35.
Thus its dimension is at most two.

In dimension two the three nonzero weights sum to twice the number of active coordinates.
They are at least5, their sum is even and is at most16, so the only possibility is weights5,5,6, with r=8 and all eight coordinates active.
For two weight-five generators, the column-type counts are three10 columns, three01 columns and two11 columns.
In dimension one the single nonzero weight may be5,6,7 or8.
The zero code is allowed.
These are exhaustive NECESSARY coefficient-quotient types, not an algebraic existence classification.

This finite averaging is the classical linear-code form of the Plotkin bound, not a new coding theorem.
A bounded primary-source check directly read the Queen Mary MAS309 Coding Theory Spring2008 [lecture log](https://webspace.maths.qmul.ac.uk/m.jerrum/MAS309/lectureLog.html), entries21January10:00--11:00 and4February10:00--11:00.
The former states A_2(n,d_min)<=2d_min/(2d_min-n) for2d_min>n and identifies row/column double counting; the latter identifies minimum distance with minimum nonzero weight for a linear code.
Here n<=8,d_min>=5, giving size<=5 and hence binary dimension<=2.
The entire needed counting proof is supplied above; the log's proof details and original Plotkin1960 paper were not inspected.
No priority claim or external proof dependency is asserted.
A Manchester full-notes PDF was opened as an alternative locator but no theorem or proof from it is used.
This source check introduces no artifact acquisition or source-wide acceptance.

<a id="eight-power-energy-and-weights"></a>
## 5. Energy gap, exact coefficient denominator and positive weights

We have proved that H is one of 0, Z/2, (Z/2)^2, Z/4, with the precise supports above.
Every coefficient vector has denominator dividing4; in the elementary binary cases it divides2.
This is a denominator statement for TRUE collected coefficients, not a claim about raw matrix entries or FINAL weight denominators.

For a nonzero vector in the zero coset, integer coefficients give energy>=1, with equality exactly a signed coordinate vector; a nonmonomial integer vector has energy>=2.
A nonzero half coset has nearest energy at least5/4.
In the cyclic-four case the order-four cosets have nearest energy17/16 and the half coset5/4.
Every other representative is a nearest residue plus integers, so cannot have smaller coordinatewise squared norm.
Therefore

    every nonzero integral-valued f has ||f||_2^2>=1,
    equality holds exactly for a TRUE signed monomial,
    every TRUE nonmonomial has ||f||_2^2>=17/16.              (A)

For a finite family of nonzero O0 values with positive normalized rational weights omega_i, set E=sum omega_i ||f_i||_2^2 and let theta be the total weight of nonmonomial TRUE polynomials.
Then

    E>=1+theta/16, so theta<=16(E-1).                        (B)

In particular E<1 is impossible and E=1 forces every atom to be a signed monomial, WITHOUT any lag-cancellation assumption.
This is stronger than merely saying a complementary packet has no income.
It applies only when the union dictionary has at most8 distinct powers and U<=K0.
The factor16 is a proved universal bound over the necessary types, not a claim that its quarter-type extremizer is realized by an actual near-one polynomial.

<a id="eight-power-legal-words-and-costs"></a>
## 6. Specified legal words and all original costs

Fix any finite labels with positive rational weights omega_i summing1 and actual least FINAL indexed denominator M, starting at TRUE signed monomials epsilon_i t^(a_i).
Permit constant rational isometries B of the SAME diagonal weight metric on any selected block whose current TRUE monomials use at most8 distinct exponents: B^T diag(omega)B=diag(omega).
The block weights need not sum1; normalize by their positive total when applying (B).
Their input weighted energy equals that total, so their output weighted coefficient energy does also.
If all output values are nonzero in O0, (A)--(B) force every TRUE output to be a signed monomial on the same exponent dictionary.
No rewriting of algebraic values is substituted into a polynomial covariance identity.

Interleave such constants with exactly the accepted [C84 binary factors](Yin_C_G0084_v1.md#statement): for coprime positive relative weights u:v and primitive integer direction(x,y) with xy!=0, put S=u*x^2+v*y^2, c_g=gcd(abs(ux),abs(vy)), A1=ux/c_g, B1=vy/c_g, L0=S/c_g, Pi=(1/L0)[[x*A1,x*B1],[y*A1,y*B1]], and Id-Pi+t^k Pi for any signed integer k!=0.
Optional one-coordinate signed monomial shifts are allowed.
REQUIRE every actual coordinate at EVERY stage, including unchanged coordinates, to be nonzero in the SAME O0.
Labels and weights remain fixed.

Let B_word be initial global exponent span plus the sum of abs(k) of EVERY binary delay and every optional coordinate shift.
Assume B_word*m/d<=K0.
At a constant step, the pre-step span is at most the paid cumulative bound; Section5 applies at the same K0.
At a binary step C84's exact local classification at pair span plus abs(k) applies, leaving true signed monomials and increasing the global interval by at most abs(k).
Shifts have the same interval bound.
Induction covers the ENTIRE finite word, arbitrarily many labels or factors, preserving E1 and actual final width<=B_word.
Width zero is the integer single-coordinate case and uses no epsilon(0).

Every final output is epsilon_i' t^(b_i), so actual coefficient q=1 and each full signed original norm is (epsilon_i')^d nu^(b_i).
After the common shift b=min b_i, integer resultants are (epsilon_i')^d nu^(b_i-b); with m_i=M omega_i the full copied product is product_i[(epsilon_i')^d nu^(b_i-b)]^(m_i), of absolute value1.
Thus Lambda=(1/d)sum omega_i log abs Norm(f_i(alpha))=0 and complementary surplus Lambda-(1/2)log E=0.
Constants may change signs; FINAL M and every label remain unchanged.
For a general family in Section5, retain Res(P,qf_i)=q^d D_i and product_i Res(P,qf_i)^(m_i)=q^(dM)product_i D_i^(m_i), with actual q dividing4, full signed D_i and physical width; no unit norm is asserted for its nonmonomial atoms.

Any positive final income in this specified word class therefore requires the STRICT price B_word*m/d>K0.
If B_word<=C*d, it requires m>K0/C.
This is a necessary construction-class price, not an existence theorem, a bound based only on final width, or an unrestricted Mahler gap.
Changing weights, nonmonomial seeds, zero or nonintegral intermediate values, maximal-order-only legality, general nonconstant multi-coordinate factors and arbitrary paraunitary factorization remain outside.

<a id="eight-power-controls-and-limits"></a>
## 7. Controls, limits and whole-review target

The accepted [C87 golden-unit control](Yin_C_G0087_v1.md#statement) remains a positive example outside the small domain: P=t^2-t-1, alpha=(1+sqrt5)/2, equal-weight seed(1,t^5) and B=(1/5)[[3,4],[-4,3]] have actual q5, FINAL M2, E1, signed norms5,-5 and width5, yielding surplus(log5)/2.
Its paid U=(5/2)log alpha>K0, so it contradicts neither (A) nor the word result.
No experiment or new near-one family is claimed.

The exact advance over D48 is that eight powers allow new NECESSARY quotient types, yet still have a uniform nonmonomial energy gap17/16 at the SAME K0.
The quarter class has been classified, not excluded or realized.
For r<=7 the present necessary types reduce to the earlier 0/Z2 boundary and floor5/4; D48's whole review is separate.
C92 remains the adopted all-fixed-rank theorem with rank-dependent thresholds.
No nine-power result or improvement of the unrestricted same-exponent coverage gate is established.

Root author checking covers the zero-resultant comparison, cancellation of actual q, all integer/rational width-zero cases, exact nonzero cyclic average, sixteen-sign copied norms, quarter and eighth residues, finiteness before group counting, binary weight accounting, arbitrary positive weights, true-polynomial constant operations, C84's original-order interface and cumulative-cost induction.
The selected L229 source scopes, including actual powered degree, remain inherited accepted interfaces.
No new native computation has run.
This is a complete AUTHOR proof candidate requiring a separately organized whole review by a noncontributor; it is not yet a proved Claim.

<a id="eight-power-entire-author-freeze"></a>
## Entire author freeze

Date: 2026-10-13T03:34.
Root has saved and reread the complete candidate, Sections1--7 and equations(A)--(B).
The original candidate/status history remains.
The author considers the stated necessary quotient classification, energy gap and specified legal-word conclusion complete at the exact hypotheses above; whole independent review is pending.
This freeze includes the directly checked classical Plotkin attribution and its limited statement-level source scope.
There is no native execution or mathematical acceptance at this checkpoint.
