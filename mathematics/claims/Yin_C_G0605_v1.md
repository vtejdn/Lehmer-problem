---
author: Yin
---

# Primitive unreduced defects, a forced exterior root and sparse-multiple transfer

Human author Yin.
The paid_comparison contributor developed the content, real-root and multiplier arguments on 2026-10-23 under the selected G0001 continuation.
Root assigned the original-root comparison question and requested fixed registration, but supplied no derivation of these arguments.
Ordinary author checking is retained in the argument; the selected assessment below owns the separate whole review and adoption.
No native program, numerical experiment or new source acquisition is used.

## Statement

All Mahler measures below are TOTAL logarithmic Mahler measures, and all polynomial roots and original embeddings retain their multiplicities.
For a monic nonconstant P in Z[z] with P(0)=1 define the actual UNREDUCED polynomials

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3.

**A. Content.**
H23, H25 and H35 are primitive integer polynomials.
Their degrees are respectively 6d,10d,15d and both endpoint coefficients are 1,11,7, where d=deg P.
In particular H35 cannot equal 7 times a monic integer polynomial, including a monic product of cyclotomic polynomials.
Primitivity alone does not exclude nonmonic factors with every root on the unit circle.
None of these assertions concerns the separately reduced canonical trace representative of g.

**B. Exterior root in the actual trace domain.**
Suppose in addition that P is irreducible, reciprocal and nontorsion of degree d=2r, and that its actual trace field Q(alpha+alpha^(-1)) is totally real.
Put R=max_i abs(alpha_i)>1 over every original root.
Then H35 has a real root beta with

    abs(beta)>R^(1/3)>1,
    m(H35)>log7+(1/3)log R.                       (1)

Its reciprocal beta^(-1) is also a root.
Thus the WHOLE unreduced H35 cannot have all roots on the unit circle in this domain.
The argument uses no full-residual equation and supplies a LOWER Mahler cost, not an upper bound on the original-resultant discrepancy.
It excludes neither a cyclotomic factor of H35 nor zero Haar measure of a different canonical representative.

**C. A fully paid sparse-multiple sufficient class.**
Retain P and its actual totally real trace field from B.
Use the exact C191v2 actual trace quotients a,b,c, their defects e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5, and assume

    f=e+s g=0, g!=0, s in {1,-1}.

The exact original-value normalization from C587v2 is

    G(z)=-z^(-15d/2)H35(z)/k0, k0=30375,
    G(alpha)=g,
    tau=(12/11)log2,
    J_G=2m(H35)-2log k0.

Fix, INDEPENDENTLY of P, constants eta>0, B>=0, integers K_0>=2 and S_0>=1, and a positive rational q satisfying

    exp(tau/2-eta/2)<=q<exp(tau/2).                 (2)

Consider precisely the inputs with J_G<=tau-2eta for which there is a nonzero ordinary polynomial D in Z[z] such that

    P does not divide D, deg D<=B d, m(D)<=eta/4,
    N=D H35,
    #supp(N)<=K_0, ||N||_1/(k0 q)<=S_0.             (3)

Then the complete C196v5 NF1--NF8 theorem applies to the ACTUAL polynomial u=N/(k0 q), at

    C_0=15+B, eta_0=min{eta/4,1},
    m(P)>h_star(K_0,S_0,eta_0)/(15+B)>0.           (4)

Here h_star is exactly the positive finite constant defined in C196v5 NF2 and NF6; no numerical inversion or new constant is asserted.
The normalization, full original norm and actual ordinary degree are

    abs Norm_(Q(alpha)/Q) u(alpha)
       =abs Norm g * abs Norm D(alpha) / q^d
       >=(2^(6/11)/q)^d>1,
    m(u)=J_G/2-log q+m(D)<=-eta/4,
    deg u=15d+deg D.                              (5)

All norms in (5) are in the FULL original field of degree d.
No integrality of u(alpha) is needed or asserted.
If D is any monic product of cyclotomic polynomials, including D=1, then its nonvanishing at alpha and m(D)=0 are automatic.
For that subclass the same conclusion holds with the stronger eta_0=min{eta/2,1}, while the full degree budget and the two actual numerator budgets in (3) are still required.
Neither bounded degree nor zero Mahler measure of D supplies those numerator budgets.

The result gives a sufficient class and exact obstructions, without proving that the class contains an actual full-residual input.
It supplies no general uniform D_G estimate, no original near-one sequence and no completion of G0001.

## Reuse, source and operation scope

The current question starts from [C587v2's complete direct-original normalization](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse) and [C195v2's complete contact decomposition](Yin_C_G0195_v2.md#c195-original-contact-decomposition).
Those already give u35=H35/(30375q), degree15d and EXACT normalized discrepancy D_G/2, with fixed support and coefficient budgets missing.
They are not presented as new results here.
The changed transfer tests an actual polynomial MULTIPLE of H35, with all multiplier costs and all numerator coefficients retained.
Its final analytic implication is an explicit application of the complete [C196v5 norm-only theorem](Yin_C_G0196_v5.md#norm-only-sparse-transfer), not a replacement theorem or a claim to have proved its source inputs again.

The reuse screen read C195v2 and C587v2 completely, C196v5's complete NF1--NF8 argument and canonical-factor scope, C175's completed moving-test boundary, C159's finite weighted angular statement, C585v2's positivity/interlacing boundary, C605v2's actual trace-field and composition boundaries, and C200's complete torsion calibration.
A targeted search of existing G Claims and ledger records for primitive H35/H25, content at 7/11, exterior H35 roots and cyclotomic sparse multiples located no exact proof of A or B.
This bounded search makes no literature novelty assertion.
The already accepted finite norm, scalar Mahler and elementary polynomial interfaces suffice for the deductions.
In particular [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) supplies the scalar Mahler convention, multiplicativity, integrable circle zeros and the accepted Kronecker characterization at its recorded statement/proof-inspection scope.
No new source proof, numerical library or mathematical program is invoked.

The actual nonnegativity of a in the full residual branch and its corrected interlacer are already retained in [C585v2](Yin_C_G0585_v2.md#actual-trace-positivity-interlacing-screen).
That initial possible route added no new conclusion and was not redeveloped.
The new content argument concerns the UNREDUCED numerators, so it does not change C196v5's canonical factor alternatives or C199v5's canonical zero-Haar investigation.

## Complete author argument

### 1. Endpoint-prime primitivity

Because P is monic of degree d and has constant coefficient1, direct multiplication gives the degrees and endpoints stated in A.
The two summands of each H have the same degree, and their leading coefficients differ by the stated nonzero integer.
Thus H23 is monic and hence primitive.
The positive content of H35 divides7, so the only possible nontrivial content would be7.

Suppose for contradiction that H35 is zero modulo7.
Put F=P mod7 in F_7[z].
Its constant term is1 and its leading coefficient is1, so F is nonconstant.
Let k>=1 be the LEAST positive exponent with nonzero coefficient c in F.
There is such a k because its degree remains d.
Since 250=243=5 modulo7 and5 is nonzero, the assumed vanishing gives

    F(z^3)^5=F(z^5)^3 in F_7[z].

The left side has coefficient5c at z^(3k), while the right side has coefficient0 there: its first possible positive exponent is5k.
No higher coefficient of F can contribute at3k, and a product of at least two positive-degree terms has degree at least6k.
The coefficient5c is nonzero in F_7, a contradiction.
Hence the content of H35 is1.

The content of H25 similarly divides11.
Modulo11, its vanishing would imply F(z^2)^5=F(z^5)^2 because75=64=9 and9 is nonzero.
Using the least positive coefficient c z^k of F=P mod11 gives nonzero coefficient5c at degree2k on the left and zero on the right, again impossible.
Thus H25 is primitive too.
No irreducibility, reciprocity, trace-field or residual premise was used in this argument.

If H35=7Q with Q in Z[z], its content would be divisible by7, contradicting the conclusion.
Every monic integer cyclotomic product has integral coefficients, so that proposed special form is excluded in particular.
This is not a proof that primitive nonmonic circle polynomials do not exist: 7z^2+z+7 is primitive and has two complex conjugate roots of modulus1, since its discriminant is -195 and their product is1.
The stronger whole-H35 exclusion in B uses the actual real-root geometry, not this false inference from content.

### 2. Real-ray exterior zero of H35

Each conjugate delta_i of alpha+alpha^(-1) is real by the actual trace-field assumption.
Every original alpha_i solves z^2-delta_i z+1=0 for its corresponding embedding.
Consequently it either is real or has modulus1: a nonreal conjugate pair of this real quadratic has product1.
Since P is monic irreducible and nontorsion with constant1, its total Mahler measure is positive by the accepted Kronecker characterization.
Equivalently some original root lies outside the unit circle; the unit product prevents all root moduli from being at most1 unless all equal1.
Hence a root alpha_* of maximal modulus R>1 is real.

Let x be its real cube root, so x^3=alpha_*, abs(x)=R^(1/3)>1 and abs(x^5)=R^(5/3)>R.
A monic REAL polynomial of even degree is positive at every real y>R and every real y<-R: there is no real root on those outer rays and its sign at either infinity is positive.
Thus P(x^5)>0, and the exact unreduced definition gives

    H35(x)=250P(x^3)^5-243P(x^5)^3
          =-243P(x^5)^3<0.

The degree of H35 is15d, which is even, and its leading coefficient is7>0.
Therefore H35 tends to positive infinity along the same real ray as x.
The intermediate value theorem gives a real beta strictly farther along that ray with H35(beta)=0 and abs(beta)>abs(x).
Reciprocity of P implies reciprocity of both terms of H35 at the common degree15d, hence beta^(-1) is also a root.
These are distinct roots because abs(beta)>1.

The exact scalar Mahler formula now gives

    m(H35)=log7+sum_(H35(gamma)=0) log^+ abs(gamma)
           >=log7+log abs(beta)
           >log7+(1/3)log R.

All roots in the sum retain multiplicity; no other root contributes a negative term.
This proves (1).
It does not give a uniform positive excess over log7 when R tends to1 and supplies no upper estimate for the resultant discrepancy.
H35 may still have unit-circle roots and cyclotomic factors.
The canonical trace remainder for g is a different polynomial, so its possible zero Haar cost is untouched.

### 3. Multiplication preserves and increases the full norm floor

Return to the actual full residual branch in C.
The arithmetic input is exactly [C191v2](Yin_C_G0191_v2.md#statement), as already matched to the original field in [C587v2 DR1--DR5](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse):

    abs Norm_K g>=2^(6d/11), K=Q(alpha),
    H35(alpha)=-k0 alpha^(15d/2)g,
    Norm_K alpha=1.                               (6)

The exponent15d/2 is an integer because d is even.
Nonzero g and irreducibility imply that every original conjugate value of H35 is nonzero.
The assumption P does not divide D is equivalent to D(alpha)!=0 because P is the monic minimal polynomial of alpha.
Every D(alpha_i) is an algebraic integer, and its full field norm is a nonzero rational integer.
Thus abs Norm_K D(alpha)>=1, regardless of whether D(alpha) generates K.

With u=N/(k0q), evaluation and multiplication of all d original embeddings give

    u(alpha)=-alpha^(15d/2)g D(alpha)/q,
    abs Norm_K u(alpha)
       =abs Norm_K g * abs Norm_K D(alpha) / q^d.

The sign and the centered unit phase have absolute norm1.
The rational scalar q is raised to d, not to a smaller trace or generated-field degree.
Combining this identity with (6) and the strict upper bound on q in (2) proves the norm assertion in (5).
No value-integrality of u or hidden cancellation of D is involved.

The two nonzero polynomials have nonzero leading coefficients, so their ordinary product has EXACT degree15d+deg D.
Mahler additivity and the same rational scalar give

    m(u)=m(H35)+m(D)-log k0-log q
         =J_G/2-log q+m(D)
         <=tau/2-eta-(tau/2-eta/2)+eta/4
         =-eta/4.

This retains any leading coefficient and off-circle roots of D through m(D).
The actual support and coefficient norm of u are exactly those of N scaled by1/(k0q); they are bounded by (3), rather than inferred from the degree or the number of displayed factors.
In particular1<=deg u<=(15+B)d and every NF1 hypothesis holds at the constants in (4).
The complete C196v5 NF1--NF8 conclusion therefore proves (4), with its fixed regularization, Fourier, radial, source-constant and actual-powered-degree costs unchanged.
This is the sole analytic transfer used here.

If D is a monic cyclotomic product, all its roots are roots of unity.
Since alpha is nontorsion, D(alpha)!=0, and the scalar Mahler formula gives m(D)=0 exactly, including D=1.
The same argument then gives m(u)<=-eta/2 and the stated stronger eta_0.
Its original norm is still a nonzero integer and is retained in the exact norm identity; it is used with its legitimate lower bound1, not silently set equal to1.
The full degree of D is still added to15d.
A rational rescaling of D could make its original norm smaller than1 and would require a new paid hypothesis; it is outside (3).

### 4. Dense H35 calibration, exact scope and next obligation

[C200](Yin_C_G0200_v1.md#cyclotomic-h35-energy-log-calibration) gives an explicit reason to examine the actual numerator after multiplication.
For prime p>30 it takes P_p=Phi_p, d=p-1 and

    D0=(z^3-1)^5(z^5-1)^3,
    N_p=250(z^(3p)-1)^5(z^5-1)^3
             -243(z^(5p)-1)^3(z^3-1)^5,
    D0 H35=N_p, deg D0=30, m(D0)=0.

Each displayed summand has at most6*4=24 terms, so #supp(N_p)<=48.
The elementary binomial coefficient sums give ||N_p||_1<=493*2^8=126208.
These are safe upper bounds; no new claim about their optimality is needed.
Meanwhile C200 proves that the expanded H35 coefficient energy diverges and that J_G stays uniformly negative along this torsion family.
The multiplier degree30 is fully retained and, since d>=30 here, is at most d.

These P_p are TORSION and have g=0 and H35(alpha)=0 at every original root.
Their original norm therefore vanishes, so they do not satisfy C, even though they demonstrate that a dense expanded H35 need not prevent a bounded sparse numerator after a genuine zero-Mahler multiplication.
Their nonzero circle logarithm cannot replace that missing original norm.
The above coefficient bounds are read directly from the fixed factorization, without a numerical rerun or change of C200's evidence scope.

For a hypothetical sequence of actual full-residual inputs with m(P)->0 and a fixed saving eta, C implies the following necessary escape: the degree ratios, normalized coefficient bounds and term counts in (3) cannot all remain uniformly bounded for any chosen nonvanishing integral multipliers with m(D)<=eta/4.
Indeed uniform bounds would supply fixed B,K_0,S_0 and contradict the positive constant (4).
This conclusion asserts no such sequence and does not prove any of those quantities diverges separately.

The concrete continuing construction problem is to find or exclude, for the SAME original H35 and residual equations, multipliers meeting (3) on a useful varying-input class.
A multiplier may reduce coefficient complexity through exact cancellation, but this is an unresolved requirement.
The content theorem alone does not produce a multiplier, and the exterior-root theorem supplies a lower cost in the opposite direction from a useful upper comparison.
The current unrestricted D_G comparison and all-input coverage remain open.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T14:43 |
| status | open |
| reason | Register the exact complete author candidate for endpoint-prime primitivity, the actual real-ray exterior zero and the fully paid sparse-multiple sufficient class. Whole separate review and adoption remain pending; no multiplier existence, actual residual input, uniform unrestricted transfer or Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Parts A--C: all monic constant-one content hypotheses; actual trace-domain exterior root; exact full-residual norm, multiplier nonvanishing/Mahler/degree and numerator-budget sufficient class, with every boundary. |
| argument | [Complete author argument](#complete-author-argument) | Every content, sign, reciprocal-root, scalar/full-norm/degree and fixed-transfer step, the torsion calibration and precise remaining construction problem. |
| dependency | [Original residual floor](Yin_C_G0191_v2.md#statement) | Exact actual full-residual nonzero g bound abs Norm_K(g)>=2^(6d/11), with the full original degree and trace hypotheses. |
| dependency | [Actual original normalization](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse) | Unreduced H35, k0, phase, original norm, J_G and rational q domain; no inherited independent review is enlarged. |
| dependency | [Complete norm-only transfer](Yin_C_G0196_v5.md#norm-only-sparse-transfer) | Entire NF1--NF8 at the explicitly supplied C_0,K_0,S_0,eta_0; exact fixed h_star and all inherited analytic/source expenses. |
| dependency | [Scalar Mahler and Kronecker input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted scalar root formula, multiplicativity, integrable circle zeros and Kronecker characterization only; source-proof inspection remains at its existing scope. |
| support | [Exact torsion calibration](Yin_C_G0200_v1.md#cyclotomic-h35-energy-log-calibration) | Complete actual sparse numerator/cyclotomic multiplier and its zero original-norm boundary, without a new execution or nontorsion application. |
| support | [Existing positivity screen](Yin_C_G0585_v2.md#actual-trace-positivity-interlacing-screen) | Reused already-covered positivity/interlacer inquiry only, not a premise of the new content or root proof. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:09 |
| status | proved |
| authority | Yin activated all strategies and continued the unchanged G0001 Task. |
| reason | Adopt the complete primitive-defect and exterior-real-root theorems and the fully paid sparse-multiple sufficient class through isolated whole R807. Every original norm, rational scalar, multiplier cost and actual numerator budget is retained; no full-residual input or useful multiplier existence, uniform discrepancy bound or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Parts A--C: all monic constant-one content hypotheses; actual trace-domain exterior root; exact full-residual norm, multiplier nonvanishing/Mahler/degree and numerator-budget sufficient class, with every boundary. |
| argument | [Complete author argument](#complete-author-argument) | Every content, sign, reciprocal-root, scalar/full-norm/degree and fixed-transfer step, the torsion calibration and precise remaining construction problem. |
| dependency | [Original residual floor](Yin_C_G0191_v2.md#statement) | Exact actual full-residual nonzero g bound abs Norm_K(g)>=2^(6d/11), with the full original degree and trace hypotheses. |
| dependency | [Actual original normalization](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse) | Unreduced H35, k0, phase, original norm, J_G and rational q domain; no inherited independent review is enlarged. |
| dependency | [Complete norm-only transfer](Yin_C_G0196_v5.md#norm-only-sparse-transfer) | Entire NF1--NF8 at the explicitly supplied C_0,K_0,S_0,eta_0; exact fixed h_star and all inherited analytic/source expenses. |
| dependency | [Scalar Mahler and Kronecker input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted scalar root formula, multiplicativity, integrable circle zeros and Kronecker characterization only; source-proof inspection remains at its existing scope. |
| support | [Exact torsion calibration](Yin_C_G0200_v1.md#cyclotomic-h35-energy-log-calibration) | Complete actual sparse numerator/cyclotomic multiplier and its zero original-norm boundary, without a new execution or nontorsion application. |
| support | [Existing positivity screen](Yin_C_G0585_v2.md#actual-trace-positivity-interlacing-screen) | Reused already-covered positivity/interlacer inquiry only, not a premise of the new content or root proof. |
| review | [Whole isolated independent finding](../audits/reviews/Yin_R_G0807_v1.md#unreduced-defects-whole-finding) | Entire exact current statement, complete argument and every selected input at the explicit binding scopes; actual isolated independent review and inherited source/input limits remain distinct. |

