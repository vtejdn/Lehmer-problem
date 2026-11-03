---
author: Yin
---
# Frobenius ratios in their own fields and polynomial class escape

Opened: 2026-10-15T12:56.
Human author Yin.
Root develops the following new continuation of the adopted C146 criterion and delegates further checking/explicit estimates to g_bridge_audit.
Root supplied the ratio-field construction and the Omega combination below and is a PROOF CONTRIBUTOR to this new inquiry; root is not eligible to be its independent whole reviewer.
This does not change the prior C146v1/R357 review relationships.

<a id="statement"></a>
## Current statement

Let P be the minimal polynomial of a nontorsion algebraic integer unit alpha, with ORIGINAL degree d and total logarithmic Mahler measure m.
For any rational prime p, any prime of its normal closure above p and any residue-Frobenius lift sigma there, let kappa be sigma's ACTUAL conjugacy-class size.
No normality of Q(alpha), unramified-prime or good-power-basis hypothesis is imposed.
Write c=log2/4, h0=c exp(-20), A_p=p(p+1), B_p=4c(log p)^12/(19^12 A_p), and let Omega be the adopted L209 modulus written in Section1.

The complete argument proves the domain split H=A_p kappa m>h0 OR kappa Omega(H)>=log p.
For0<m<1 this gives

    kappa >= min{h0/(A_p m),
                    [B_p/(m log^2(1/m))]^(1/13)}.

The second bound alone holds below the explicit exp(-X_p) cutoff in(13).
Consequently, for each fixed p and0<=theta<1/13, every lift satisfies kappa>m^(-theta) below the explicit cutoff(14)--(15).
The statement is uniform over a fixed finite prime set by taking the stated maximum cutoff.
No near-one sequence is assumed to exist.
For a supplied upper bound kappa<=k, equations(16)--(19) give an explicit positive gap with order k^(-13)(log k)^(-2) at fixed p and large k.

The proof uses rho=alpha^p/sigma(alpha) as a nontorsion unit in its OWN field E of degree D<=kappa d.
It retains selected conjugate mass at least1/kappa, local step1/D, height m_rho<=kappa(p+1)m, the full norm, all degree-drop multiplicities and exact relative signed-norm return to the original field.
The exponents are n<p kappa d and pn<p^2 kappa d, and the relative-product total exponent is below p^2 kappa^2 d.
These are linear in original d only with p,kappa fixed.
Automatic bounded-class coverage and unrestricted G0001 remain open.

## Concrete change and bounded reuse

C146 already proves a positive gap for supplied bounded prime/class size with a fully paid intermediate field.
Its crude Archimedean triangle bound requires local depth2k and costs p^(2k).
The different test below makes a nontorsion conjugate ratio, uses ITS OWN degree for the first valuation amplification, and invokes the already proved actual-height cyclic modulus.
It seeks a polynomial rather than exponential class-size cost.
It is not an extra assumption that the two original conjugates are independent Haar samples.

Root actually read [C146](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument), the full [L209 quantitative Omega interface](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus), and [L168's earlier finite criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion).
The latter is superseded for the explicit modulus by L209, avoiding an unperformed finite enumeration.
A bounded local search for conjugacy-class/Omega/Frobenius-ratio combinations returned the old L160/L162 comparisons and the current C146; it was not exhaustive and establishes no novelty.
The delegate must complete the relevant reuse check before a final fixed claim.
No new external theorem or mathematical program is used at opening.

<a id="argument"></a>
## Complete argument and retained initial proposal

<a id="ratio-own-field-author-calculation"></a>
## 1. Root's complete proposed ratio-field inequality

Retain C146's original nontorsion integer unit alpha, d=[Q(alpha):Q], total m>0, normal closure L with group G, supplied residue-Frobenius lift sigma at p and its ACTUAL conjugacy-class size kappa=[G:C_G(sigma)].
Let H_alpha=Gal(L/Q(alpha)), H'=H_alpha intersection C_G(sigma), K'=L^(H'), d'=[K':Q], and r=d'/d<=kappa.
C146 proves that sigma is an actual finite-order automorphism of K', and d'/kappa embeddings represented by its centralizer are residue-compatible.
These statements are now adopted inputs, not reassertions of a false original-field normality.
The subgroup H_alpha is distinct from the positive scalar H introduced below.

Put

    rho=alpha^p/sigma(alpha), E=Q(rho), D=[E:Q].           (1)

It is an algebraic integer UNIT.
It is NONTORSION: if rho^M=1, then alpha^(pM)=sigma(alpha)^M, and iteration through the finite order h of sigma on K' gives alpha^((p^h-1)M)=1, a contradiction.
In particular D>=2 and every cyclic norm of rho is nonzero.
D<=d'<=kappa d.

The FULL original conjugate sum gives

    h_abs(rho)<= (p+1)m/d,
    m_rho:=D h_abs(rho)<=kappa(p+1)m.                    (2)

For the first inequality, sum log^+ of tau(alpha)^p/tau sigma(alpha) over ALL embeddings of K'.
It is at most p times the positive sum for alpha plus the negative sum for sigma(alpha).
Both original unit sums equal r m, and right composition by sigma permutes these d' embeddings.
Dividing by d' gives the bound, with no assumption that rho has degree d' or that its conjugates are pairwise independent.

Among these d' embeddings, C146 supplies d'/kappa values of tau(rho) congruent1 modulo the chosen normal-closure prime.
Every E-embedding extends to exactly d'/D K'-embeddings.
Hence at least D/kappa DISTINCT original conjugates of rho have that congruence.
This count may be nonintegral as a lower bound and means at least its ceiling; all D conjugates remain in the eventual norm.

Each such conjugate lies in a copy of E of degree D.
The positive valuation of tau(rho)-1, normalized by v(p)=1, is therefore at least1/e_E>=1/D.
This uses the SAME [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) degree/value-group interface, now in the RATIO FIELD, not K' or the normal closure.
Set

    a=ceil(log_p D), n=p^a<p D.                         (3)

The prime binomial induction raises every selected positive valuation to at least1 after a steps.
Other conjugates of rho^n-1 are integral.
The nonzero FULL rational integer norm in E therefore satisfies

    log|Norm_(E/Q)(rho^n-1)|/D >= (log p)/kappa.         (4)

No relative-degree multiplicity or lost conjugate is ignored; (4) follows from at least D/kappa selected ORIGINAL rho-conjugates.

Now let c0=log2/4, h0=c0 exp(-20), and use the actual L209 function

    b(t)=max(t,sqrt(t/c0) log sqrt(c0/t)),
    Omega(t)=19 b(t)^(1/6), 0<t<=h0.

The actual powered height is n m_rho/D < p m_rho.
Thus if

    H=p(p+1)kappa m <=h0,

L209, its monotonicity and (2)--(4) give the candidate exact inequality

    (log p)/kappa <= Omega(H),
    kappa Omega(p(p+1)kappa m) >= log p.                 (5)

If H>h0, that separate alternative must be retained; applying Omega outside its domain is invalid.
The auxiliary has degree D<=kappa d and exponent n<pD, and every size change is paid explicitly.
This has not yet been independently reviewed.

## 2. Consequence to check and explicit-constant continuation

L209 proves Omega(t)=O(t^(1/12)(1+log(1/t))^(1/6)) as t tends to zero, with absolute constants.
For any FIXED p and theta<1/13, a hypothetical sequence m_j->0 with kappa_j<=m_j^(-theta) would have H_j->0 and

    kappa_j Omega(H_j)
      =O_(p,theta)(m_j^((1-13theta)/12)
                   (1+log(1/m_j))^(1/6)) ->0,           (6)

contradicting(5).
The monotonicity is important when substituting the upper bounds for both kappa and H.
Therefore the proposed stronger necessary escape is kappa>m^(-theta) eventually for EVERY lift at every prime in a FIXED finite prime set, for each fixed theta<1/13.
It remains conditional on a near-one sequence; none is constructed.
The all-lifts quantifier follows because the uniform bound forbids even one exceptional lift with the stated small class.

The delegate should verify the entire construction and scope, screen prior ratio-field uses, and derive a clean explicit inverse/cutoff in p,k if useful.
The central gain being tested is the actual rho-field degree and the use of the already quantified nonlinear cyclic cost; merely improving the old depth constant is not the question.
This is naturally a substantive extension of C146's family if validated, with v1 and R357 retained.
No fixed C revision or adoption has yet been made.

Both original algebraic coverage and the parallel F-inspired problem remain open.
The present inequality would not itself force a bounded Frobenius class on all small-m inputs.

<a id="ratio-focused-reuse-and-check"></a>
## 3. Focused reuse and contributor recalculation

The delegated author read the actual adopted C146v1, including its whole-reviewed decision, and the COMPLETE L209 modulus and degree-adapted applications.
A focused search of G claims/ledgers for Frobenius ratios, conjugate ratios, own-field height and conjugacy-class/Omega interfaces located [L64's additive stability](../ledger/Yin_L_G0064_v1.md#additive-frobenius-error-stability) and [its twisted Fermat quotient](../ledger/Yin_L_G0064_v1.md#derivative-fermat-quotient-link).
Those exact passages were read.
They treat a local unramified component and its first quotient/depth, retaining the distinction between units and local nonunits; they do not give a global ratio-field degree/mass estimate or combine it with L209.
This is a focused project reuse conclusion, not an exhaustive priority search.
The prior C146 source comparison, including the stronger already-known original-Galois coverage, remains in force; no new external theorem is imported here.

The author recalculated(1)--(5) rather than treating their initial proposal as accepted mathematics.
Since alpha and sigma(alpha) are global units, rho and its inverse are integral.
If rho were torsion, the finite-order automorphism argument would contradict the original nontorsion hypothesis.
All embeddings of K' restrict to the original root field and to E with constant fiber sizes r and d'/D, respectively.
Consequently the positive/negative logarithmic sums in(2) and the count at least D/kappa are valid even if E is strictly smaller than K' and the selected embeddings collide on E.
At a selected distinct rho-conjugate, the local positive step comes from its own degree-D field and not from the larger ambient degree.
The binomial induction, including p=2 and a possible exact p-power D, gives n<pD and selected depth at least1.
The inequality h_abs(rho^n)=n m_rho/D <p m_rho<=H is strict at the first comparison but only its non-strict consequence is used.
All hypotheses of L209 are met when H<=h0: rho is a nontorsion algebraic unit and its actual powered degree may drop without invalidating that result.

Thus the inequality(5), with the separate H>h0 alternative, is established by this contributor check.
This is NOT independent project review: root originated the new ratio-field/Omega proof, and this delegate develops its explicit consequences below.

<a id="ratio-original-signed-norm-return"></a>
### 3A. Exact return of the ratio norm to the original field

Keep the SAME n from(3), and put beta=alpha^(pn)-sigma(alpha)^n.
The identity beta=sigma(alpha)^n(rho^n-1), the unit property and the norm tower give

    Norm_(K'/Q)(beta)
      =epsilon * Norm_(E/Q)(rho^n-1)^(d'/D),
    epsilon=Norm_(K'/Q)(sigma(alpha)^n) in {1,-1}.       (7)

Both signed norms are nonzero.
As in C146, eta=Norm_(K'/K)(beta) lies in the full ORIGINAL O_K and Norm_(K/Q)(eta)=Norm_(K'/Q)(beta).
Its relative product has r<=kappa factors involving alpha and actual conjugates h sigma(alpha).
Consequently

    log|Norm_(K/Q)(eta)|/d'
       =log|Norm_(E/Q)(rho^n-1)|/D,
    n<p kappa d,
    pn<p^2 kappa d,
    r pn<p^2 kappa^2 d.                                 (8)

The normalized local income is still (log p)/kappa, and the normalized expense is the actual L209 value.
The equality in(8) pays the repeated E-embeddings exactly.
The product before collecting monomials has at most2^r terms, and its total conjugate exponent is at most r pn.
A cheap one-variable representative in Z[alpha] is not asserted.
For fixed p,kappa these are original-degree-linear bounds; when kappa grows, the displayed factors grow and are NOT called a uniform O(d) window.
Integrality of eta in O_K needs no power-basis-index exclusion, and the sign epsilon in(7) is not silently assumed positive.

<a id="ratio-explicit-logarithmic-class-bound"></a>
## 4. An explicit class-size lower bound, with both height domains

Write c=c0=log2/4, A_p=p(p+1), and define the positive explicit constant

    B_p=4c (log p)^12/[19^12 A_p].                       (9)

On the small-height domain 0<H<=h0=c exp(-20), put x_H=sqrt(c/H)>=exp(10).
Then x_H log x_H>c, so the second entry of L209's maximum is the larger one.
In particular its formula is EXACTLY

    b(H)=sqrt(H/c) * log sqrt(c/H),
    Omega(H)^12=19^12 * (H/c) * [log(c/H)]^2/4.          (10)

Taking the twelfth power of(5), substituting H=A_p kappa m and rearranging gives

    kappa^13 m [log(c/(A_p kappa m))]^2 >= B_p
                                      when H<=h0.       (11)

There is no use of the asymptotic shorthand in this deduction.
If 0<m<1, kappa>=1 and A_p>=6 imply

    0<log(c/(A_p kappa m))<log(1/m)

in this small-H branch.
The large-H branch separately gives kappa>h0/(A_p m).
Combining the two branches proves the all-input finite bound

    kappa >= min{ h0/(A_p m),
                   [B_p/(m (log(1/m))^2)]^(1/13) }
                                for every 0<m<1.        (12)

The first entry is NOT deduced using Omega outside its domain.
A lower bound stated by the minimum is valid in either branch; the strictness available in the large-H branch is not needed.

For an explicit range on which the second entry is the smaller one, set

    X_p=max{1, (1/12) log[B_p (A_p/h0)^13]}.

If x=log(1/m)>=X_p, then x^2 exp(12x)>=B_p(A_p/h0)^13, which is exactly the thirteenth-power comparison of the two entries in(12).
Therefore

    kappa >= [B_p/(m (log(1/m))^2)]^(1/13)
                            whenever 0<m<=exp(-X_p).    (13)

This is the claimed explicit logarithmically corrected polynomial escape.
The exponent1/13 and the logarithmic factor arise from L209's currently proved modulus; no optimality is asserted.
The constants remain functions of the ACTUAL prime p, not uniform constants after an unbounded prime is chosen.

<a id="ratio-explicit-theta-cutoff"></a>
### 4A. A completely explicit cutoff for each exponent below1/13

Fix 0<=theta<1/13 and q=1-13theta>0.
Define

    X_(p,theta)=max{X_p,
           (2/q) log[32/(exp(2) q^2 B_p)]}.             (14)

For x>=0, maximizing x^2 exp(-q x/2) at x=4/q proves

    x^2 exp(-q x)<=16/[exp(2)q^2] * exp(-q x/2).

Thus x>=X_(p,theta) makes the last quantity at most B_p/2.
Together with(13), this yields the finite strict conclusion

    kappa >=2^(1/13) m^(-theta)>m^(-theta)
                      if 0<m<=exp(-X_(p,theta)).         (15)

The maximum in(14) is valid even if its logarithm is negative, since X_p>=1.
The case theta=0 is included.
If theta<0, kappa>=1>m^(-theta) already holds for0<m<1.
For a fixed finite nonempty prime set S, replace X_(p,theta) by max_(p in S) X_(p,theta).
Then(15) holds simultaneously for every p in S, every prime of the normal closure above p and every residue-Frobenius lift there.
This follows by applying the individual statement to each possible lift; neither independence nor a distribution theorem for those lifts is used.
The empty-S assertion is vacuous, and no near-one sequence is assumed to exist.

<a id="ratio-explicit-bounded-class-gap"></a>
## 5. A direct explicit gap for a supplied class bound

For any rational prime p and integer k>=1 define

    y_(p,k)=min{exp(-10), (log p/(38k))^6},
    Z_(p,k)=log(2/y_(p,k)),
    m_*(p,k)=c y_(p,k)^2/[4 A_p k Z_(p,k)^2].           (16)

Then EVERY actual input and supplied lift with kappa<=k satisfies

    m(P)>m_*(p,k)>0.                                    (17)

To prove this, suppose m<=m_*(p,k), write y=y_(p,k), Z=Z_(p,k)>10, and set h_*=c[y/(2Z)]^2<h0.
Then H=A_p kappa m<=h_*.
The exact small-height formula(10) and log(2Z/y)=Z+log Z<2Z show

    b(h_*)= [y/(2Z)] [Z+log Z] <y,
    kappa Omega(H)<=19k b(h_*)^(1/6)
                   <19k y^(1/6)<= (log p)/2.            (18)

This contradicts(5), proving(17).
The domain H<=h0 is guaranteed by the proposed small-m bound, not assumed from the desired conclusion.
All constants are elementary explicit expressions; no inverse special function or unperformed root-finding computation enters.

For fixed p and all k large enough that the second entry defines y, the exact formula is

    m_*(p,k)=
      c (log p/38)^12
       /{4 A_p k^13 [log2+6 log(38k/log p)]^2}.         (19)

Thus this paid lower bound has order k^(-13)(log k)^(-2) for fixed p, unlike C146v1's exponentially small sufficient bound.
For the remaining finite/small k, (16) retains its cap and is the formula to use.
The old C146v1 bound may be numerically stronger at small k; both remain valid and their maximum is an available conservative lower bound.
No pointwise improvement of its constant at every p,k is claimed.
This strengthens the same conditional bounded-class criterion; it is not a proof that general small-m inputs admit such a bounded class, nor a new treatment of a Galois-generator domain that was already covered classically.

<a id="ratio-whole-author-freeze"></a>
## 6. Final scope, actual contributions and whole author freeze

The ENTIRE draft is author-complete and frozen at 2026-10-15T13:07.
Its [statement](#statement) and [argument](#argument) include the complete initial root proof(1)--(6), the focused reuse check, the original signed-norm return, all finite constants/cutoffs and the explicit supplied-bound gap(7)--(19).
The original proposal/check wording in Sections1--2 is historical development, now resolved by the full contributor recalculation in Sections3--5; it does not indicate a remaining mathematical verification assignment inside this author's round.
The candidate still awaits independent whole review and fixed adoption.

Root contributed the NEW ratio-field construction, its nontorsion/height/embedding-fiber argument, the own-degree valuation amplification and L209 combination, together with the proposed below1/13 consequence.
The delegated author g_bridge_audit recomputed the full chain, checked exact reuse, supplied the relative signed-norm return and explicit domain split, constants, cutoffs and inverse gap, and wrote Sections3--6 plus the current statement.
Both are proof contributors and neither is this extension's independent reviewer.
The old C146v1/R357 relationship is unchanged; a reviewer of this strengthened successor must cover the new complete argument.

The final author check covered unit integrality and inverse integrality, global non-torsion of rho, strict smaller ratio-field degree and equal embedding fibers, possible collisions within the selected embeddings, all local ramification in copies of E, the p=2 and exact-power endpoints, the powered-degree-drop clause and positivity domain of L209, negative as well as positive original logarithmic sums, the sign in the norm tower, every original multiplicity and exponent fee, the exact maximum in b, the H>h0 branch, the thirteenth-power comparison defining X_p, the elementary exponential maximum giving X_(p,theta), theta=0/negative theta, fixed finite prime-set quantifiers, and both branches of y_(p,k).
No missing premise was found in this contributor check.
In particular, when kappa grows the original expression's exponent and factor counts grow as(8); the argument never calls that a uniform original-degree-linear certificate.

Direct mathematical inputs are the adopted [C146v1 intermediate-field and selected-embedding argument](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument), [L209's complete actual-height cyclic modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus), and [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) at its exact local-algebra statement/application scope.
L209's earlier Pri11/Dim19 source acceptance and powered-degree conventions are inherited at their recorded limits, not re-audited or strengthened.
L64, L160/L162 and L168 are comparisons/reuse context, not substitutes for the new ratio-field proof.
No new external theorem, source acquisition, mathematical program, J or independent R was made by this author.
The focused one-file structural check returned checked1; that is not mathematical review.

The actual remaining bridge is still automatic arithmetic coverage for ORIGINAL small-m nontorsion polynomials.
This result proves that such hypothetical inputs must have very large fixed-prime Frobenius conjugacy classes; it does not force a small class or construct a near-one family.
Torsion controls do not meet the new ratio's nontorsion premise, and their failure to do so is not used as a counterexample to the original task.
The whole draft is suitable as a substantive strengthening of the C146 family with its old physical version and review preserved.

## Fixed organization

This substantive successor retains the entire frozen ratio-field argument and its explicit inverse bounds.
The earlier [physical v1](Yin_C_G0146_v1.md#decision-whole-reviewed-2026-10-15), its complete nineteen-formula argument, failed two-prime construction, source comparisons and [R357 review](../audits/reviews/Yin_R_G0357_v1.md#bounded-class-whole-independent-finding) remain fixed and applicable at their original scope.
This successor selects that intermediate-field input explicitly, and adds a new entire proof requiring its own whole review.
Root and g_bridge_audit are contributors to this successor; neither is its independent reviewer.
Automatic bounded-class coverage remains unproved.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-15)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T13:09 |
| status | open |
| reason | Retain the whole own-ratio-field strengthening of the bounded-Frobenius-class criterion, including explicit polynomial class escape and bounded-class gaps. Independent whole review of this successor is pending; unrestricted G0001 remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete strengthened statement](#statement) | All-input domain split, finite class lower bound, explicit cutoffs, supplied-class gap, full original norm and exponent costs, and all quantifiers. |
| argument | [Complete strengthened argument](#argument) | All six sections and nineteen formulas, original root proposal and completed contributor proof, failed shortcuts and exact dependency/contribution boundaries. |
| dependency | [Adopted intermediate field](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Small intermediate field, actual automorphism, selected embedding population, local lift and original signed-norm return, with original source boundaries. |
| dependency | [Actual-height cyclic modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact Omega, small-height domain and monotonicity, full ratio-field norm including powered-degree drops and inherited source limits. |
| dependency | [Local ramification interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Positive normalized valuation at least reciprocal own field degree, now for every selected copy of the ratio field; original source proof limits preserved. |

### Decision whole-reviewed-2026-10-15

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T13:20 |
| status | proved |
| reason | Adopt the actual noncontributor whole review of the complete ratio-own-field strengthening: all original norm and ramification costs, explicit polynomial class escape and capped supplied-class gap are covered. Automatic arithmetic coverage and unrestricted G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete strengthened statement](#statement) | All-input domain split, finite class lower bound, explicit cutoffs, supplied-class gap, full original norm and exponent costs, and all quantifiers. |
| argument | [Complete strengthened argument](#argument) | All six sections and nineteen formulas, original root proposal and completed contributor proof, failed shortcuts and exact dependency/contribution boundaries. |
| dependency | [Adopted intermediate field](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Small intermediate field, actual automorphism, selected embedding population, local lift and original signed-norm return, with original source boundaries. |
| dependency | [Actual-height cyclic modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact Omega, small-height domain and monotonicity, full ratio-field norm including powered-degree drops and inherited source limits. |
| dependency | [Local ramification interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Positive normalized valuation at least reciprocal own field degree, now for every selected copy of the ratio field; original source proof limits preserved. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0358_v1.md#own-field-ratio-whole-independent-finding) | Entire actual successor statement and six-section nineteen-formula proof, all direct input interfaces, explicit cutoffs, original norm costs and source/contribution boundaries. |

