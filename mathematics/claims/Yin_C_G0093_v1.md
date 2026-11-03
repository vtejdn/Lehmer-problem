---
author: Yin
---
# Seven-power coefficient quotient, positive-weight energy gap and legal-word rigidity

Date: 2026-10-13T03:38.
Human author Yin.
Fixed internal extraction under the resumed G0001 authorization.
Root supplied the substantive D48 candidate and all central proof steps; rounding-recovery completed the original argument.
The separately assigned d48_whole_review AI independently reviewed the ENTIRE preserved 2026-10-12T18:28 D48 freeze in R326 and NOW authors this exact statement/extraction wrapper.
It is therefore a contributor to this NEW artifact and cannot independently review its actual extraction.
A different noncontributor must inspect the actual registered Claim before adoption.
R326 remains original whole-proof support only.
The entire original candidate, provenance, development history, proof and pause freeze are retained below.

## Statement

Fix an ACTUAL nontorsion algebraic integer unit alpha, its monic irreducible minimal polynomial P of ORIGINAL degree d>=2, K=Q(alpha), the SAME original order O0=Z[alpha], nu=Norm_K(alpha) in {+1,-1}, and TOTAL logarithmic Mahler measure m=m(P)>0.
Every norm below uses all d ORIGINAL embeddings.
For a rational Laurent polynomial f, let f*(t)=f(t^-1) and let ||f||_2^2 denote the sum of squares of its TRUE collected rational coefficients.
No replacement by a value-equivalent polynomial is allowed in these coefficient statements.

Use the exact accepted increasing functions and numerical constant

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log(sqrt(c0/u))},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0,
    K0=c0/[2*36^8*5^64]>0.

The adopted C74 R=1 margin gives K0<h0/2 and 5^8[epsilon(2K0)+12K0]<1.
All zero-width cases are treated exactly, without evaluating epsilon at zero.
The same K0 applies throughout; it does not depend on the number of labels, positive weights, matrix denominators, finite word length or primitive binary heights.
Existing L229/C71/C74/C84 source-acceptance and proof-inspection limits remain unchanged.

**A. Automatic independence and the COMPLETE seven-power coefficient quotient.**
Let 1<=r<=7 and let a_1,...,a_r be DISTINCT integers with actual span A=max_i a_i-min_i a_i satisfying A*m/d<=K0.
Define the full additive group

    L={x in Q^r: sum_i x_i alpha^(a_i) belongs to O0}.

Then the r actual powers are Q-linearly independent.
The ENTIRE quotient L/Z^r is either trivial or isomorphic to Z/2Z.
In the latter case there is one zero-one vector v of weight w in {5,6,7} such that

    L=Z^r+Z*(v/2),

that is, the union of Z^r and Z^r+v/2.
Every nonzero half class has support weight 5--7.
In particular L=Z^r for r<=4.
The conclusion does NOT assert that a proper half class is realized, or that full saturation holds for r=5,6,7.
It requires no A<d hypothesis and places no separate bound on absolute exponent sizes.

The local proof first establishes actual independence by comparing a lower phase Gram estimate with the radial error of a hypothetical zero relation, without applying a norm floor at zero.
For every nonzero x in L it then establishes the strict intermediate bound ||x||_2^2>99/100, using the full original rational-norm estimate and the SAME cleared denominator.
Finite-order residue averages, the complete sixteen-label C71 sign packet and a binary-code weight identity give the sharper quotient classification above.
Pending C92 acceptance is not a premise: the needed independence argument is completely reproduced in the retained proof.

**B. Exact energy gap for TRUE polynomials and ANY positive-weight family.**
Let f be any rational Laurent polynomial with at most seven distinct collected exponents, actual span A satisfying A*m/d<=K0, and NONZERO value f(alpha) in O0.
Then

    ||f||_2^2>=1,
    ||f||_2^2=1 if and only if f=+/-t^a for some integer a,
    f not a signed monomial implies ||f||_2^2>=5/4.

Here the phrase not a signed monomial includes a one-term polynomial whose coefficient is not +1 or -1.
Its actual coefficient denominator divides two.

For ANY finite indexed family f_1,...,f_N satisfying these conditions INDIVIDUALLY, with positive rational weights omega_i summing to one, put

    E=sum_i omega_i ||f_i||_2^2,
    mu=sum_(i: f_i is not a signed monomial) omega_i.

Each polynomial may use its OWN at-most-seven-exponent dictionary and OWN actual span; the union of all dictionaries is not required to have at most seven elements.
Then

    E>=1+mu/4,   0<=mu<=4(E-1).

Thus E>=1, and E=1 forces EVERY indexed polynomial to be a signed monomial.
This assertion needs NO off-diagonal lag cancellation and NO complementary covariance identity.
For E>1 it is an energy/mass bound only, not a positive norm-income bound.
All labels, including duplicates and opposite signs, remain indexed.

**C. Actual denominators, arbitrary indexed weights and full ORIGINAL signed costs.**
In B, let q be the ACTUAL least common coefficient denominator and M the ACTUAL least indexed weight denominator.
Then q is 1 or 2, with q=2 exactly when some coefficient is nonintegral.
This gives no bound on M.
Write m_i=M omega_i in positive integers, so sum_i m_i=M.
Let b be the minimum exponent in the UNION of the actual supports, and set

    ftilde_i=t^(-b) f_i, F_i=q ftilde_i in Z[t],
    D_i=Norm_K(f_i(alpha)), Dtilde_i=nu^(-b)D_i.

All D_i and Dtilde_i are nonzero signed integers.
Define

    Lambda=(1/d)sum_i omega_i log abs(D_i),
    I_int=(1/d)sum_i omega_i log abs Res(P,F_i),
    S_int=sum_i omega_i ||F_i||_2^2.

Then the exact arithmetic is

    Res(P,F_i)=q^d Dtilde_i,
    product_i Res(P,F_i)^(m_i)
        =q^(dM) nu^(-bM) product_i D_i^(m_i),
    S_int=q^2 E, I_int=log q+Lambda,
    I_int-(1/2)log S_int=Lambda-(1/2)log E.

No primitive content, normalization sign, original norm or indexed copy is discarded.
The COMMON union width used for this accounting can exceed every individual width; B asserts no common-width bound from its separate individual hypotheses.
At E=1, every D_i has absolute value one, actual q=1 and Lambda=full surplus=0, irrespective of that union width and M.

**D. Exact rational constant-block action.**
Take ANY finite selected block of labels with positive rational weights omega_i, TRUE signed-monomial inputs f_i=epsilon_i t^(a_i), epsilon_i in {+1,-1}, and at most SEVEN DISTINCT current exponents of actual span A with A*m/d<=K0.
Repeated exponents and arbitrarily many labels are allowed.
Let B be any rational constant square matrix on this block with

    B^T diag(omega_i) B=diag(omega_i).

Require EVERY actual output value g_i(alpha), where g=Bf is the TRUE polynomial action, to be NONZERO in the SAME O0.
Then EVERY output g_i is a signed monomial with exponent in the original block dictionary.
The proof preserves the full positive weighted coefficient energy and applies the Part B energy bound to each output, so the common support interval cannot enlarge.

This places no bound on block size, the raw matrix denominator or the weight denominators.
It does not require the block weights to sum to one.
The matrix itself need not be integral when input exponents repeat, and its entry denominator must not be identified with the actual output coefficient denominator, which is one.
Individual signs, exponent multiplicities and copied-exponent totals need not be preserved.

**E. ANY finite legal mixed word, with cumulative expense and every intermediate value.**
Fix ANY finite N>=1 indexed labels and positive rational weights omega_i summing to one, with ACTUAL least denominator M and copies m_i=M omega_i.
Start from TRUE signed monomials f_i^(0)=epsilon_i t^(a_i), and let A0=max_i a_i-min_i a_i.
Keep every label and weight fixed.
Permit ANY finite word consisting of:

1. Rational constant blocks as in D, each using at most seven DISTINCT current input exponents.
2. The exact adopted C84 binary delays.
   On two selected labels, use their ACTUAL coprime positive integer relative weights u:v, any primitive integer direction (x,y) with xy!=0, and any nonzero signed integer k.
   Put

       S=u*x^2+v*y^2, c_g=gcd(abs(u*x),abs(v*y)),
       A=u*x/c_g, B=v*y/c_g, L=S/c_g,
       Pi=(1/L)[[x*A,x*B],[y*A,y*B]],
       U_k=Id-Pi+t^k Pi.

3. Optional one-coordinate signed monomial shifts, with every absolute exponent shift charged below.

REQUIRE every coordinate value at EVERY stage, including unchanged coordinates, to be NONZERO in the SAME original O0.
Let

    B_word=A0+sum abs(k),
    U_word=B_word*m/d,

where the sum charges EVERY binary delay and EVERY optional coordinate shift, of either sign; constant factors add no charge.
If U_word<=K0, then EVERY TRUE intermediate polynomial and EVERY final polynomial is a signed monomial.
At every stage and finally,

    actual q=1, SAME actual indexed M,
    E=1, Lambda=0, full surplus=0,
    T_final<=B_word.

The PRE-step global spread is bounded by A0 plus all prior absolute charges.
A constant step uses D at its current dictionary; a binary step uses C84 at the ACTUAL pair spread plus abs(k), bounded by the updated cumulative expense.
C84's allowed action leaves that pair unchanged or applies a common t^k.
No value-equivalent representative is substituted inside a covariance identity.
If B_word=0, every seed exponent coincides and the exact one-power argument applies without epsilon(0).

Every permitted factor preserves the fixed weighted Laurent covariance, whose seed value is one.
If final polynomials are epsilon_i' t^(b_i), their FULL original signed norms are

    D_i=(epsilon_i')^d nu^(b_i).

After the common normalization b=min_i b_i, their integer resultants are (epsilon_i')^d nu^(b_i-b); their copied signed product is

    product_i [(epsilon_i')^d nu^(b_i-b)]^(m_i),

of absolute value one.
Constants may change individual signs, so no original-sign invariance or copied-exponent conservation is asserted for the mixed word.
Arbitrarily large raw matrix or fixed weight denominators do not alter these actual output facts.

For the SAME specified legal class without the small-cost assumption, any positive FINAL norm income, or positive final complementary surplus since covariance still gives E=1, necessarily has the STRICT price

    B_word*m/d>K0.

Consequently, for any fixed B0>0, B_word<=B0*d together with positive income implies m>K0/B0.
The charged quantity is CUMULATIVE expense, not a smaller final width obtained by cancellation.
No finite-dimensional, word-length, positive-weight-lower-bound or primitive-height restriction is substituted for these hypotheses.

**F. Retained exact positive control and limits.**
The existing C87 Part E control has P=t^2-t-1, alpha=(1+sqrt5)/2, d=2, nu=-1, weights 1/2,1/2, seed (1,t^5), and constant matrix

    B=(1/5)[[3,4],[-4,3]].

The TRUE outputs (3+4t^5)/5 and (-4+3t^5)/5 evaluate to 3+4alpha and 1+3alpha, with full signed norms 5,-5.
Actual q=5, FINAL M=2, E=1 and width 5 give numerator resultants 125,-125, copied product -15625=5^4*(-25), and Lambda=surplus=(1/2)log5>0.
Its fixed U=(5/2)log alpha>K0, so it lies outside the theorem.
It is not a realization of a proper small-cost half class or a near-one sequence.

The result does not prove full saturation for five to seven powers or existence of a nontrivial half class, and does not cover eight distinct powers, changing weights/metrics, nonmonomial seeds, zero intermediate values, final-only integrality, arbitrary multicoordinate nonconstant factors, or an arbitrary paraunitary factorization.
The SAME O0 restriction is retained because the four-half-class exclusion invokes C71; C87's full-order statement is not enlarged.
L229 supplies its exact accepted angular and original-resultant bounds, C74 only the numerical margin, C71 only the complete sixteen-label E1 selector, and C84 only the specified legal binary interface.
C87 is retained control/comparison; C92 is disclosed ancestry, not a premise.
Existing Pri11/Dim19 and ancestor source-proof limits remain.
No uniform same-exponent arithmetic lower income, positive universal packet surplus or unrestricted Mahler gap is established.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T03:38 |
| status | open |
| reason | Register the exact seven-power quotient, energy gap, individual-dictionary positive-weight family and specified legal mixed-word result while retaining the ENTIRE original D48 freeze. Original whole R326 supports D48 only; its reviewer now authors this new wrapper and cannot independently inspect its own extraction. A distinct reviewer must inspect the actual allocated statement, retained argument and every interface before adoption. No unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F: original integer-unit/O0/full-degree domain, SAME K0, complete quotient and energy gap, individual-dictionary families, positive weights without lag assumptions, exact q/M/norms, constant blocks, all-stage cumulative-cost words, retained control and limits. |
| argument | [Entire preserved original argument](#argument) | ENTIRE 2026-10-12T18:28 D48 freeze, initial candidate/provenance/history, Sections 1--9, equations (1)--(17), every original anchor, source/contributor boundaries and human-pause checkpoint. |
| dependency | [L229 angular input](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact finite-frequency estimate, c0/h0/b/epsilon, monotonicity, actual powered degree and original multiplicities; retained accepted source-proof limits. |
| dependency | [L229 full coefficient-energy estimate](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Nonzero INTEGER auxiliary with full content, Euclidean coefficient norm, rho and original degree/radial expense; SAME rational denominator cleared/canceled after local independence. |
| dependency | [C74 numerical margin](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY R=1, exact K0, K0<h0/2 and 5^8[epsilon(2K0)+12K0]<1; no multiplicity-dependent word theorem is used. |
| dependency | [C71 all-positive-weight E1 selector](Yin_C_G0071_v1.md#statement) | ONLY Part A applied to the COMPLETE sixteen-label nonzero O0 sign packet, actual q2/FINAL M16/E1 and actual common width; source/domain limits retained. |
| dependency | [C84 exact binary delay interface](Yin_C_G0084_v1.md#statement) | Exact primitive weighted binary signed factors and TRUE-polynomial local unchanged/common-shift classification at K0, fixed metric, every-stage nonzero SAME O0, actual local spread plus absolute delay and optional one-coordinate shifts. |
| support | [Existing golden-unit control](Yin_C_G0087_v1.md#statement) | ONLY Part E's exact constant rotation, original signed norms and q5/M2/E1/width5 surplus outside K0; its full-order saturation theorem is not a proof premise. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0326_v1.md#seven-power-entire-independent-finding) | ENTIRE actual frozen D48 and direct interfaces independently checked before this wrapper was authored. R326 remains original WHOLE support only; it does not prospectively cover the actual Claim extraction or adopt it. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-13T03:48 |
| status | proved |
| reason | Adopt original entire D48 finding R326 and distinct actual C93 extraction finding R329. Preserve complete source and historical pause freeze. The same-K0 seven-power quotient, energy5/4 and positive-weight/no-lag consequence, actual costs and specified cumulative legal-word rigidity are fixed at their precise original-order scope. No nontrivial quotient realization, unrestricted positive-income coverage or G0001 completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F: original integer-unit/O0/full-degree domain, SAME K0, complete quotient and energy gap, individual-dictionary families, positive weights without lag assumptions, exact q/M/norms, constant blocks, all-stage cumulative-cost words, retained control and limits. |
| argument | [Entire preserved original argument](#argument) | ENTIRE 2026-10-12T18:28 D48 freeze, initial candidate/provenance/history, Sections 1--9, equations (1)--(17), every original anchor, source/contributor boundaries and human-pause checkpoint. |
| dependency | [L229 angular input](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact finite-frequency estimate, c0/h0/b/epsilon, monotonicity, actual powered degree and original multiplicities; retained accepted source-proof limits. |
| dependency | [L229 full coefficient-energy estimate](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Nonzero INTEGER auxiliary with full content, Euclidean coefficient norm, rho and original degree/radial expense; SAME rational denominator cleared/canceled after local independence. |
| dependency | [C74 numerical margin](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY R=1, exact K0, K0<h0/2 and 5^8[epsilon(2K0)+12K0]<1; no multiplicity-dependent word theorem is used. |
| dependency | [C71 all-positive-weight E1 selector](Yin_C_G0071_v1.md#statement) | ONLY Part A applied to the COMPLETE sixteen-label nonzero O0 sign packet, actual q2/FINAL M16/E1 and actual common width; source/domain limits retained. |
| dependency | [C84 exact binary delay interface](Yin_C_G0084_v1.md#statement) | Exact primitive weighted binary signed factors and TRUE-polynomial local unchanged/common-shift classification at K0, fixed metric, every-stage nonzero SAME O0, actual local spread plus absolute delay and optional one-coordinate shifts. |
| support | [Existing golden-unit control](Yin_C_G0087_v1.md#statement) | ONLY Part E's exact constant rotation, original signed norms and q5/M2/E1/width5 surplus outside K0; its full-order saturation theorem is not a proof premise. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0326_v1.md#seven-power-entire-independent-finding) | ENTIRE actual frozen D48 and direct interfaces independently checked before this wrapper was authored. R326 remains original WHOLE support only; it does not prospectively cover the actual Claim extraction or adopt it. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0329_v1.md#c93-seven-power-actual-extraction-finding) | Entire actual statement and retained argument, all direct interfaces, individual-versus-union-width distinction and complete preservation; noncontributor actual review distinct from proof and wrapper authors. |

## Registration and complete preservation

The [original D48](#seven-power-entire-author-freeze) is now retained here after complete preservation and locator repair.
Its redundant draft path is retired.
Its ENTIRE body follows: remove only the duplicate author/framework front matter and demote the first title by one heading level.
The allocator normalizes newline encoding and final separating newlines; no substantive text, formula, anchor, history, earlier incomplete label, author-role disclosure, actual pause account or limitation is removed.
Existing relative links resolve from this Claim directory without rebasing.
A direct complete-body readback comparison verifies preservation with exactly these stated transformations; a structural check is not mathematical review.

The original author-complete checkpoint resolved the initial candidate's historical incompleteness, and R326 subsequently supplied an actual whole-proof finding.
Neither fact is rewritten into the retained history.
This initial Claim decision instead records the PRESENT proof-draft/under-review extraction status.
Root and rounding-recovery retain original contribution attribution.
The d48_whole_review AI now contributes only this new wrapper and cannot supply its independent extraction finding.
No adoption, D48 retirement, native mathematical program or new source acquisition accompanies this allocation.

## Argument

## Seven-power coefficient quotient and unconditional energy-one rigidity

Date: 2026-10-12T18:20.
Human author Yin.
Responsible late-window AUTHOR candidate.
Root supplied the substantive seven-power quotient, cyclic-average, binary-code and word candidate, including its proposed constants and all central proof steps.
Rounding-recovery completes and checks the argument.
BOTH are contributors and cannot independently WHOLE-review this material.
The current root C92 extraction is under actual review; its original annihilator argument is a credited candidate antecedent and will be completely restated here where needed, not assumed adopted.
No native computation or external source search is proposed.

<a id="seven-power-responsible-candidate"></a>
## Candidate and exact remaining checks

The proposed domain is an actual nontorsion integer unit alpha, original minimal degree d and total m, SAME O0=Z[alpha], and at most seven distinct integer exponents of actual span A with A*m/d<=the accepted K0.
The candidate first proves independence directly by comparing the lower phase Gram energy with the squared radial error for a hypothetical rational annihilator.
It then uses the nonzero L229 rational-norm bound to show every nonzero integral-valued coefficient vector has squared energy>99/100.

For the full group L={x in Q^r:sum x_i alpha^(a_i) in O0}, the intended classification is L/Z^r trivial or of order2; any nonzero half-coefficient class has support weight5--7.
The proposed proof excludes odd prime orders by exact cyclic nearest-residue averages, excludes weight4 half classes by the old q2/E1 sign packet, excludes order4 by its four-cycle average, and uses the length-seven binary code weight identity to exclude two independent order2 classes.
It does not assert that a proper half class is actually realized in the small-window domain.

If valid, every nonzero TRUE polynomial on this dictionary has coefficient energy>=1, equality only for a signed monomial, and every nonmonomial has energy>=5/4.
Positive weighted families would then have nonmonomial mass at most4(E-1), with E1 rigidity requiring no lag cancellation.
The candidate further considers legal words of rational constant metric isometries on blocks using at most seven distinct current powers, interleaved only with accepted C84 binary delays and charged shifts, all intermediates nonzero in O0 and cumulative width budget<=K0.

The exact K0 margins, rational finite-order issue, all cyclic averages and class nonvanishing, complete sign packet, actual quotient, full original norm signs, actual q/FINAL M, and cumulative true-polynomial word induction still require the explicit author check below.
Until a complete freeze is appended, this is an INCOMPLETE proof draft.
At the actual100percent stop gate it must remain at its true saved state without further research.


<a id="seven-power-domain-and-inputs"></a>
## 1. Actual domain, accepted inputs and numerical margins

Fix an ACTUAL monic irreducible nontorsion integer-unit minimal polynomial P, a root alpha, the ORIGINAL field K=Q(alpha), degree d>=2, O0=Z[alpha], nu=Norm_K(alpha) in{+1,-1}, and TOTAL logarithmic Mahler measure m=m(P)>0.
All norms below use the d original embeddings.
Put

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log(sqrt(c0/u))},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0,
    K0=c0/[2*36^8*5^64].                                  (1)

These are exactly the accepted [L229 angular and coefficient-energy functions](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound), increasing on the stated domain.
The actual [C74 R1 numerical margin](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) gives

    K0<h0/2,
    5^8[epsilon(2K0)+12K0]<1.

In particular epsilon(K0)<5^(-8)<1/100000.
Also K0<1/10000 directly from(1): c0<1 and 2*5^64>10000.
No value epsilon(0) is required.
For 0<U<=K0 the elementary exponential-series bound exp(x)<=1/(1-x) gives

    D7(U):=exp(2U)[1+6epsilon(U)+28U]
          <(5000/4999)*(50143/50000)=50143/49990,
    (99/100)*(50143/49990)=4964157/4999000<1.                (2)

Indeed 6epsilon(U)+28U<6/100000+28/10000=286/100000.
These deliberately coarse rational margins are hand inequalities, not numerical experiments.

The other direct accepted inputs are [C71's all-positive-weight E1 selector](Yin_C_G0071_v1.md#statement), used ONLY for one complete sixteen-label q2 sign packet in Section4, and [C84's all-height binary-delay classification](Yin_C_G0084_v1.md#statement), used ONLY for the specified legal word factors in Section7.
The new zero-relation argument in Section2 was supplied by root in its C92 ancestor work and then explicitly supplied as part of this candidate.
C92 was under actual extraction review when this candidate was received.
This draft gives that entire argument locally; C92 acceptance is NOT a premise.
Existing L229 source acceptance limits, including its powered-field/angular inputs, are unchanged.
No new external source is introduced.

<a id="seven-power-independence-and-energy-floor"></a>
## 2. Local independence and a strict rational coefficient-energy floor

Let a_1,...,a_r be DISTINCT integers, 1<=r<=7, with span A=max a_i-min a_i and U=A*m/d<=K0.
Define the additive group

    L={x in Q^r: sum_i x_i alpha^(a_i) belongs to O0}.
                                                                    (3)

It contains Z^r.
Every Laurent monomial alpha^a is a unit of O0, including negative a, because P is monic with constant coefficient +/-1.
A common monomial shift therefore preserves order membership and nonvanishing; its exact signed norm multiplier is nu to that shift.
It changes neither collected coefficient energy nor span.

We first prove that the r actual powers are Q-independent.
If r=1 this is immediate.
Otherwise suppose a nonzero rational relation F(alpha)=0 exists on this dictionary.
Clear no norm denominator and invoke no nonzero norm floor here.
Normalize the first exponent of its actual nonzero support to zero, write T for that support's positive width, S=sum_i c_i^2>0, S1=sum_i abs(c_i), and rho=S1^2/S<=r.
Put alpha_j=r_j z_j for the d original conjugates.
All F(alpha_j) vanish, since a rational relation at alpha is divisible by its minimal polynomial.
The L229 finite-frequency angular estimate and the complete Gram expansion give

    (1/d)sum_j abs(F(z_j))^2 >= S[1-(rho-1)epsilon(U)].      (4)

This is a LOWER Gram bound, with every nonzero frequency bounded by T<=A; it assumes no phase independence.
Define B_j=F(alpha_j)/max(1,r_j)^T=0.
As in the elementary radial comparison, every normalized radial coefficient lies in[0,1] and differs from1 by at most min{1,T*abs(log r_j)}.
Consequently

    abs(F(z_j))^2 <= S1^2 min{1,T*abs(log r_j)}^2
                  <= S1^2 T*abs(log r_j).

The unit identity sum_j abs(log r_j)=2m now shows that the left side of(4) is at most 2rho S*T*m/d<=2rho S*U.
Thus the relation would force

    1 <= (rho-1)epsilon(U)+2rho U
       <= 6epsilon(U)+14U
        <6/100000+14/10000<1,                             (5)

a contradiction.
This proves automatic independence at the SAME K0, not a threshold depending on r.
The argument covers a relation on any smaller actual support.
There is no hidden use of the integer norm of zero.

Next take any nonzero x in L and f(t)=sum_i x_i t^(a_i).
Independence implies f(alpha)!=0.
After normalizing its first actual exponent, let q be its ACTUAL least coefficient denominator, F=qf in Z[t], T its actual width, S=||f||_2^2, and rho=(sum abs(x_i))^2/S<=7.
If T=0, f(alpha)=c alpha^a in O0 implies c in O0 intersect Q=Z, so S=c^2>=1.
If T>0, apply the accepted L229 estimate to the NONZERO integer auxiliary F.
Its exact norm identity is

    Res(P,F)=q^d Norm_K(f(alpha)),

with the normalization unit sign included in the displayed f(alpha).
As the latter norm is a nonzero rational integer, dividing the L229 estimate by q cancels that SAME denominator completely and gives

    1 <= abs Norm_K(f(alpha))^(2/d)
       <= S exp(2T*m/d)[1+(rho-1)epsilon(T*m/d)+4rho*T*m/d]
       <= S D7(U).

Equation(2) therefore proves, also including T0,

    EVERY nonzero x in L has ||x||_2^2>99/100.              (6)

The bound is uniform in coefficient heights, actual q and the original degree.
It applies after subtracting ANY integer coefficient vector whenever the resulting coefficient vector is nonzero.
All such subtractions remain in L.
Independence is what ensures their evaluated values are nonzero.

<a id="seven-power-odd-primary-exclusion"></a>
## 3. Exact cyclic averages exclude every odd prime torsion class

Each class in L/Z^r has finite order: a common rational coefficient denominator of a representative annihilates it.
This point does not assume L/Z^r is finite or finitely generated.
If any class had order divisible by an odd prime p, an integer multiple would have order EXACTLY p.
Take such a representative x, so p*x is integral and x is not integral.

For k=0,...,p-1 choose the coordinatewise nearest-integer residue representative y_k of k*x modulo Z^r.
Each y_k belongs to L.
The class is nonzero for k=1,...,p-1, so y_k!=0 and(6) applies; y_0=0.
A coordinate whose class is zero contributes zero throughout.
At a nonzero coordinate, multiplication by its nonzero numerator permutes all residues modulo p.
The nearest residues are 0 and +/-j/p for j=1,...,(p-1)/2.
Their exact mean square is

    (1/p)*2*sum_(j=1)^((p-1)/2) j^2/p^2
       =(p^2-1)/(12p^2)<1/12.                             (7)

This follows by substituting (p-1)/2 in the finite sum j^2=m0(m0+1)(2m0+1)/6.
Summing over at most seven coordinates gives

    (1/p)sum_(k=0)^(p-1) ||y_k||_2^2 <=7/12.

But(6) gives the STRICT lower bound (99/100)*(p-1)/p>=33/50>7/12, since p>=3.
This contradiction excludes every odd prime divisor in the order of every class.
Thus all individual class orders are powers of2.

<a id="seven-power-half-and-four-cycle"></a>
## 4. Half-class weight and the exact four-cycle obstruction

Consider a nonzero order2 class.
Its nearest representative has entries0 or +/-1/2.
Let w be the number of half entries.
Its energy w/4 is greater than99/100 by(6), hence w>=4.

The case w=4 is impossible for a stronger reason than this coarse norm floor.
Let J be its four distinct active exponents.
For EVERY sign vector sigma in{+1,-1}^J, retain the actual Laurent polynomial

    g_sigma(t)=(1/2)sum_(i in J) sigma_i t^(a_i),
    omega_sigma=1/16.                                    (8)

All sixteen coefficient vectors represent the SAME half class: changing a sign changes a coefficient by an integer.
Thus all sixteen values belong to O0, and independence from Section2 makes all of them nonzero.
None is a signed monomial as a TRUE polynomial.
Retain all labels and their weights; do not delete negative pairs or select a favorable subset.
Averaging all signs cancels every off-diagonal term, giving the exact Laurent identity

    sum_sigma omega_sigma g_sigma g_sigma*=4/4=1.

After one common monomial normalization, this is a C71 packet of ACTUAL q=2, FINAL M=16 and ACTUAL common width T_J=max_(i in J)a_i-min_(i in J)a_i, with 0<T_J<=A.
Its full original signed norms D_sigma=Norm_K(g_sigma(alpha)) are NONZERO integers.
With the common normalization already included,

    Res(P,2g_sigma)=2^d D_sigma,
    product_sigma Res(P,2g_sigma)=2^(16d) product_sigma D_sigma.

No value norm is assumed to be a unit; signs and all sixteen copies are retained.
C71 requires the inequality 2^8[epsilon(2T_J*m/d)+12T_J*m/d]>=1.
Monotonicity and the accepted C74 margin instead give

    2^8[epsilon(2T_J*m/d)+12T_J*m/d]
       <=2^8[epsilon(2K0)+12K0]<2^8/5^8<1.                (9)

This contradiction excludes w4.
Therefore EVERY nonzero order2 class has weight w>=5.

Now suppose a class of order4 exists, represented by x.
Its double is a nonzero order2 class of weight at least5.
Therefore at least five coordinates of x modulo Z have exact denominator4.
Let n4 count those coordinates and n2 count coordinates with exact denominator2; the rest are integral.
Then n4>=5 and n4+n2<=7.
For nearest representatives of k*x, k=0,1,2,3, the coordinate mean squares are EXACTLY

    exact denominator4: (0+(1/4)^2+(1/2)^2+(1/4)^2)/4=3/32,
    exact denominator2: (0+(1/2)^2+0+(1/2)^2)/4=1/8.

Either choice at a half-integer tie has the same square.
Hence the full four-cycle mean energy is

    (3/32)n4+(1/8)n2 <=23/32.                            (10)

The maximum under the displayed constraints occurs at n4=5,n2=2, since increasing n4 at fixed total replaces1/8 by3/32.
On the other hand all three nonzero classes k=1,2,3 have energy>99/100 by(6), so the mean is greater than297/400>23/32.
This is impossible.
Any class of order2^s with s>=2 has a multiple of order4, so EVERY class now has order at most2.

<a id="seven-power-quotient-and-weighted-family"></a>
## 5. Complete quotient classification and arbitrary positive weights

Every representative x now satisfies 2*x in Z^r.
Therefore reduction modulo Z^r embeds L/Z^r as a binary linear subspace of (F2)^r.
Every nonzero codeword has Hamming weight at least5.
If there were two linearly independent words u,v, their three nonzero words u,v,u+v would satisfy

    wt(u)+wt(v)+wt(u+v)=2*abs(supp(u) union supp(v))<=14,

where each occupied coordinate belongs to exactly two of those three supports.
But each weight is at least5, giving a sum at least15.
This contradiction proves

    L/Z^r is either trivial or isomorphic to Z/2Z;
    in the latter case its unique nonzero binary word has weight5,6 or7.
                                                                    (11)

Equivalently, either L=Z^r or L=Z^r+Z*(v/2), the union of Z^r and Z^r+v/2, for one zero-one vector v of weight5--7.
This describes the complete coefficient quotient, not merely the subgroup generated by a selected family.
It does NOT assert that a proper half class actually occurs in this small-cost domain.
In particular at r<=4 the quotient is trivial; that consequence alone does not resolve r5--7 saturation.

Any vector outside Z^r in the second case has at least w coordinates in Z+1/2, hence energy at least w/4>=5/4.
Any nonzero integer vector has energy at least1, with equality exactly when one coordinate is+1 or-1 and all others zero.
Every other nonzero integer vector has energy at least2.
This includes a one-term coefficient of magnitude at least2.
Thus the precise TRUE-polynomial conclusion is

    ||f||_2^2>=1;
    equality holds iff f is a SIGNED monomial +/-t^a;
    if f is not a signed monomial, ||f||_2^2>=5/4.          (12)

Here f has at most seven distinct collected exponents, actual span A with A*m/d<=K0, and nonzero O0 value.
There is no requirement that A<d and no replacement of f by a value-equivalent representative.
The proof of independence controls the actual representation.
All coefficients and coefficient energies are those of the TRUE collected Laurent polynomial.

For ANY finite indexed family of such legal polynomials f_i, with positive rational weights omega_i summing1, define E=sum_i omega_i||f_i||_2^2 and let mu be the total weight of labels whose TRUE polynomials are not signed monomials.
The individual dictionaries may differ, as long as EACH has at most seven terms and satisfies its own span condition.
Multiplying(12) by positive weights and summing proves

    E>=1+mu/4,
    0<=mu<=4(E-1).                                        (13)

In particular E=1 forces EVERY label to be a signed monomial.
This conclusion uses no off-diagonal lag cancellation and assumes no complementary covariance identity.
The conclusion E>=1 also excludes E<1 in this class.
For E>1 the bound on mu is an energy statement only; it is not an upper or lower bound for nonmonomial norm income.
It does not extend to arbitrary full-order O membership, because Section4 invokes C71 specifically in O0.

Each individual actual coefficient denominator divides2 by(11); hence every finite such family has ACTUAL common q in{1,2}, with q=2 exactly when at least one noninteger coefficient occurs.
These are necessary conclusions, not a realization of q2.
The ACTUAL least indexed weight denominator M may be arbitrarily large.
Put m_i=M omega_i in positive integers.
After normalizing the COMMON union of all supports by its first exponent b, set ftilde_i=t^(-b)f_i, F_i=q*ftilde_i in Z[t], D_i=Norm_K(f_i(alpha)), and Dtilde_i=nu^(-b)D_i.
The exact full original signed costs are

    Res(P,F_i)=q^d Dtilde_i,
    product_i Res(P,F_i)^(m_i)
       =q^(dM) nu^(-bM) product_i D_i^(m_i),
    S_int=q^2 E,
    Lambda=(1/d)sum_i omega_i log abs(D_i),
    I_int=log q+Lambda,
    I_int-(1/2)log S_int=Lambda-(1/2)log E.                 (14)

These identities retain every original norm, denominator, sign and indexed copy.
No primitive content is discarded.
The common physical width for this accounting is max(all supports)-min(all supports); it can exceed the largest individual width.
The energy theorem does NOT assert a bound on that union width merely from its individual hypotheses.
At E1, every D_i is a unit sign and q1, so Lambda=0 and full surplus0 irrespective of that width and of M.

<a id="seven-power-legal-mixed-words"></a>
## 6. Exact constant block action

Let a current block of labels have positive rational weights omega_i and TRUE signed monomial inputs f_i=epsilon_i t^(a_i).
The block can have arbitrarily many labels and repeated exponents, but suppose its dictionary of DISTINCT exponents has cardinality at most seven and span A with A*m/d<=K0.
Let B be ANY rational constant matrix on these labels satisfying

    B^T diag(omega_i) B=diag(omega_i).                     (15)

Set g=Bf as TRUE Laurent polynomials, and REQUIRE every output value g_i(alpha) to be NONZERO in O0.
This legality is an assumption; it is not inferred from the matrix identity.
The output support of each row is contained in that block dictionary.
The preserved quadratic form, coefficient by coefficient, gives

    sum_i omega_i ||g_i||_2^2=sum_i omega_i ||f_i||_2^2
                                     =sum_i omega_i.

Apply(12) to every output row.
Positivity of every weight forces equality in every individual energy bound, so EVERY g_i is a signed monomial.
This proves constant-block rigidity without an upper bound on block size, on its matrix denominator, or on weight denominators.
Its output exponent belongs to the existing block dictionary, hence a constant step cannot enlarge the common support interval.
Individual signs, exponent multiplicities and copied-exponent totals need not be preserved.
A matrix entry denominator must not be identified with the ACTUAL output coefficient denominator, which here is1.

## 7. Legal words with all-height binary delays and full costs

Fix ANY finite number N of indexed labels, positive rational weights omega_i summing1 with ACTUAL least denominator M, and TRUE signed monomial seed f_i^(0)=epsilon_i t^(a_i).
Let A0=max a_i-min a_i.
Keep all labels and weights fixed.
Permit ANY finite word of the following factors:

* Rational constant blocks satisfying(15), each acting on a current dictionary of at most SEVEN distinct exponents.
* The precise accepted C84 weighted binary factors: on two labels of coprime positive relative weights u:v, any primitive integer direction(x,y) with xy!=0, S=u*x^2+v*y^2, c_g=gcd(abs(u*x),abs(v*y)), A=u*x/c_g, B=v*y/c_g, L=S/c_g, Pi=(1/L)[[x*A,x*B],[y*A,y*B]], and Id-Pi+t^k Pi for ANY nonzero signed integer k.
* Optional one-coordinate signed monomial shifts, whose absolute exponent shift is charged in the same budget.

REQUIRE every coordinate value at every stage to be NONZERO in the SAME O0, including unchanged coordinates.
Define B_word=A0 plus the sum of abs(k) over every binary delay and every optional coordinate shift.
Constants add no delay charge.
Suppose

    U_word=B_word*m/d<=K0.                                (16)

At a PRE-step true monomial vector the actual global spread is at most A0 plus all prior absolute delay charges.
A constant step is covered by Section6.
For a binary step, its actual pair spread plus abs(k) is at most the updated cumulative bound, so the actual adopted C84 local classification applies and keeps both TRUE outputs signed monomials.
In its permitted branches the pair either stays fixed or receives a common t^k; the common global support interval increases by at most abs(k).
A one-coordinate shift has the same interval bound directly.
This proves induction for the ENTIRE finite word.
There is no re-cleaning of evaluated values inside a covariance identity.

All factors preserve the weighted Laurent covariance of the seed (which is1): for constants this is(15); for the binary factors it is C84's exact weighted star-isometry; an individual monomial shift has modulus-square1.
Alternatively the proved true-monomial induction supplies this identity at every stage.
Therefore EVERY stage and the final packet have

    actual q=1, SAME actual FINAL M,
    E=1, Lambda=0, full surplus=0,
    T_final<=B_word.                                      (17)

M is unchanged because the indexed positive rational weights and all labels are unchanged; no merging or splitting is performed.
If the final polynomials are epsilon_i' t^(b_i), their full signed norms are D_i=(epsilon_i')^d nu^(b_i).
After a common normalization by b=min b_i their integer resultants are (epsilon_i')^d nu^(b_i-b), and their copied signed product is product_i[(epsilon_i')^d nu^(b_i-b)]^(m_i), of absolute value1.
Constants can change signs, so no original-sign invariance for the mixed word is asserted.
Arbitrarily large RAW matrix denominators or fixed weight denominators do not change these actual output facts.

For the same specified legal class without assumption(16), any positive final norm income (or positive final complementary surplus, since the preserved covariance still gives E1) consequently has the STRICT necessary price B_word*m/d>K0.
In particular B_word<=B0*d with fixed B0>0 and positive income forces m>K0/B0.
The charged quantity is the cumulative word expense, not a potentially smaller final physical width after cancellation.
This is a construction-class obstruction uniform in N, word length, M and permitted primitive binary heights.
It does not prove that any allowed construction exists outside the small-cost regime or that every rational weighted isometry factors legally in this class.

If B_word=0, every seed exponent coincides and no nonzero delay is present.
Constant steps have only that one exponent.
Section2's rational-integer argument and Section6 directly give the same conclusion without evaluating epsilon at zero.

<a id="seven-power-control-and-limits"></a>
## 8. Retained positive control, exact advance and limits

The accepted [C87 exact golden-unit control](Yin_C_G0087_v1.md#statement), Part E, shows why the small cumulative domain must remain explicit.
Reuse P=t^2-t-1, alpha=(1+sqrt5)/2, d2, nu=-1, weights1/2,1/2, seed(1,t^5) and constant B=(1/5)[[3,4],[-4,3]].
Its TRUE outputs are (3+4t^5)/5 and(-4+3t^5)/5.
Using alpha^5=5alpha+3 gives actual values3+4alpha and1+3alpha, with FULL signed norms5 and-5.
Their actual coefficient q5, FINAL M2, E1 and actual width5 give Lambda=surplus=(1/2)log5>0.
Integer numerator resultants125 and-125 have copied product-15625=5^4*(-25).
Its U=(5/2)log alpha>K0: alpha>3/2 and log(3/2)>1/3, whereas K0<1/10000.
Thus it lies outside this theorem.
It is an old exact control, not a new source, new scan, near-one family or example of a proper small-U half class.

The substantive new conclusion is the complete seven-power coefficient-quotient restriction(11), its energy gap and positive-weight consequence(12)--(13), and the corresponding enlargement of legal constant blocks in the specified C84 mixed words.
Root supplied the core cyclic-average/code candidate and all central steps, including the new locally reproduced annihilator idea from its C92 work.
Rounding-recovery completed the actual proof, verified the cyclic averages and strict constants, collected the exact order/weight/sign/width interfaces and writes this responsible material.
BOTH are contributors.
Rounding-recovery also contributed to the accepted C71 ancestor; that older acceptance is reused, not independently recertified here.

The obstruction does not supply any actual same-exponent arithmetic lower income A(n)>=eta*d at n<=C*d, a positive uniform packet surplus, or an unrestricted Mahler gap.
It does not assert full saturation for five to seven powers, existence of a nontrivial half coset, a result for eight distinct powers, changing weights or metrics, nonmonomial seeds, zero intermediate values, only-final integrality, arbitrary multicoordinate nonconstant factors, or arbitrary paraunitary factorization.
The C87 full-order constant-only theorem is not enlarged here: this theorem retains O0 because of the C71 four-half-coefficient exclusion.
No pending C92 adoption is required for the local proof in Section2.
All external source/proof scopes enter solely through the explicitly accepted L229/C71/C74/C84 interfaces; no new source or native mathematical computation has been used.


<a id="seven-power-entire-author-freeze"></a>
## 9. Actual author checkpoint at the human-requested pause

Date: 2026-10-12T18:28.
The ENTIRE initial responsible candidate and Sections1--9, equations(1)--(17), are now AUTHOR-COMPLETE and frozen for later independent review.
The mathematical body of Sections1--8 was actually saved at2026-10-12T18:27, before the author received the human's latest instruction to organize current progress and PAUSE.
Since receiving that instruction, the author has only reread the ENTIRE saved body, checked its existing direct interfaces and performed a scoped six-material structural check.
The check returned checked6; it is not a mathematical review or acceptance.
During that closeout read, the informal Section5 group notation `L=Z^r+(1/2)v` was corrected before freeze to the explicit generated group `L=Z^r+Z*(v/2)`, the union of the two cosets already classified in(11).
This notation correction adds no mathematical claim; the original initial candidate and its incomplete-status history remain intact.

The author self-check covered the lower phase Gram versus zero radial comparison without a norm of zero, the strict99/100 rational-energy floor including width0, finite order of every rational class, both exact cyclic averages, all sixteen nonzero sign-packet labels and their original copied norms, the code weight identity, every energy equality case, arbitrary positive indexed weights, actual q and unchanged FINAL M, signed unit normalizations, C84's exact O0 local interface, the pre-step cumulative support induction, and the old C87 positive control outside K0.
This is an AUTHOR verification only.
Root supplied the core candidate and the central arguments; rounding-recovery completed this responsible proof and is also a C71 antecedent contributor.
Neither is independent for a whole review of this draft.

No stated local proof step is left conditional on pending C92 adoption: its relevant zero-relation lemma is fully proved here.
The existence of a nontrivial half coset, saturation at five to seven powers, behavior at eight powers, an unrestricted arithmetic-income construction and the main uniform Mahler-gap problem remain UNSOLVED/OUTSIDE this result, as explicitly stated in Section8.
These are not claimed consequences.
A different noncontributor's actual ENTIRE review is still pending; no whole review has been requested as part of this pause closeout, no new C extraction has begun, and no adoption, retirement or native mathematical execution is performed here.



This complete author checkpoint remains UNREVIEWED at its original scope.
Resumption requires the human's direction and the applicable execution gate.
