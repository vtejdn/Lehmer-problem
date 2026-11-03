---
author: Yin
---

# Complete rational paraunitary denominator and width barriers with exact finite certificates

This retains the complete necessary mathematical argument from [the complete original L377 analytical proof and first finite attempt](../ledger/Yin_L_G0377_v1.md#paraunitary-lift-reuse-and-domain).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Fix the actual monic irreducible Salem polynomial P=t^4-2t^3+t^2-2t+1, K=Q(alpha), tau=alpha+alpha^(-1), tau²=2tau+1, tau_+=1+sqrt(2), and units u_+=tau, u_-=(1-alpha)^(-1)=2+alpha²-alpha³ with full norms+1,-1.
The original roots are beta,beta^(-1), beta>3/2 and beta+beta^(-1)=tau_+, and one unit-circle inverse pair.
For independent integers k,l and signs epsilon,eta in{+1,-1}, seek f,g in Q[t,t^(-1)] with the WHOLE original quotient residues f(alpha)=epsilon alpha^k u_+, g(alpha)=eta alpha^l u_-, and exact identity f(t)f(t^(-1))+2g(t)g(t^(-1))=1.
All residue equalities mean equality at every original conjugate.
Let T be the largest minus smallest exponent in the union of both supports, normalized by one common monomial to[0,T]; the two twists remain independent.

If such a finite-support pair exists and q is its least positive common scalar denominator, F=qf,G=qg are integral Laurent polynomials with FF*+2GG*=q² and sum F_j²+2sum G_j²=q², where star means substitution t->t^(-1).
The integer q is odd, no odd prime p with-2 nonsquare modulo p divides q, F modulo2 is a single monomial, and q>=3.
All normalized full original resultants are Res(P,F)=q^4 and Res(P,G)=-q^4, unchanged by the signs/common monomial; any individual coefficient content divides q and cannot be removed while keeping those old norms/covariance.

No rational finite-support pair with these residues has common union width T<=4, for any independent twists or signs.
The whole-circle bound and complete polynomial Poisson/reverse argument give tau_+ beta^(-k)<=1 and tau_+ beta^(k-T)<=1; hence2<=k<=T-2.
At T=4, k=2 conflicts with the actual nonreduced ring F2[t]/((t²+t+1)²), whose alpha_bar has exact order6 and tau_bar=alpha_bar³: the required F monomial would have exponent5 modulo6 outside[0,4].
The restricted real common-twist width4 case is also excluded by the complete two lag equations a²+2b²+2b=0 and a-2a²-(1+2b)²=0.
For g one has2<=l<=T-1.
Thus width5 has exactly k=2,3 and l=2,3,4, with reversal (k,l)->(5-k,6-l) and independent signs reducing to the three positive-sign k=2 cases.
This is a complete finite gate, not an existence assertion or arbitrary-width nonexistence.

In the larger rational-function class there is the explicit untwisted pair f_rat=A/D,g_rat=B/D,

    D=t^4-8t³+15t²-8t+1,
    A=-t^4+4t³-7t²+4t-1,
    B=-2t³+8t²-8t+2.

It has AA*+2BB*=DD*, exact original residues u_+,u_- and no circle poles.
With x=t+t^(-1), D/t²=x²-8x+13>=1 on[-2,2]; at the original roots D(alpha)=2alpha²(7-3tau)!=0.
The complete resultants are Res(P,D)=64, Res(P,A)=+64, Res(P,B)=-64.
The coprime A,D have genuine nonzero finite poles at two positive reciprocal pairs with traces4+sqrt(3),4-sqrt(3), including inside-disk poles; no monomial removes D.
Its full Mahler expense is the product of the two exterior roots, greater than1.
It is a solved rational-function comparison and cannot be substituted for a scalar-denominator Laurent lift or used with the polynomial inside-disk bound.

A finite Laurent lift, considered as its own full integer bundle with weights1/3,2/3, has coefficient energy q²/3 and norm income log(q), hence surplus log(3)/2 before a change of representatives, paying actual T/d, q, contents and signed full norms.
Individual least-energy residual projection need not preserve constant covariance because removed P multiples and cross terms remain.
No original residual complementarity or general near-one gap follows from an exact quotient identity.
The rational-function pair has the separate nonconstant denominator and numerator norms64, not the scalar q^4 interface.

For the exact original width5/product-degree4 finite attempt, the three seeds are f_seed=t+t³ and g_seed=1-t+t²-t³,1-t-t³,1-t-2t³ for l=2,3,4.
Every rational coefficient representative is f=f_seed+(a+bt)P and g=g_seed+(c+dt)P.
The six equations E_h=sum_(j=0)^(5-h)(f_j f_(j+h)+2g_j g_(j+h))-1_(h=0), h=0,...,5, are the entire weighted covariance identity; negative lags duplicate them.
Including all monomial products with every E_h of total product degree<=4 gives the full integer70-by90 Macaulay matrix A with rhs b equal to the coefficient vector of1.
Each of the three cases has rank50, augmented rank51, and an exact retained left-null witness y with all90 coordinates of y^T A zero and y^T b=1; nonzero witness supports are46,44,49.
This proves exactly the absence of1 in that declared degree4 product span, not nonlinear feasibility, a rational solution, higher-degree certificate absence or width5 nonexistence.
All original equations/coefficients/monomial conventions/matrices/rhs/pivots/witnesses and initial execution/stop limits remain at J85.
The current read-only full reconstruction rechecked every mathematical object without running the author producer or changing native bytes.

Historical prospective/unresolved wording below describes the original22:23 freeze and its first attempt.
The later fixed L384 exact-point account is a separate subsequent result; no current-open-problem assertion or later result is inferred from the three left-null witnesses here.
The related2008 FIR abstract is a search lead only, with no adopted factorization/field-preservation/interpolation proof.
The local polynomial Poisson proof is supplied explicitly; the ABR01 selected attribution remains at its existing reading depth.
No optimizer, solver search, changed polynomial, wider coefficient/certificate domain, new source theorem or unrestricted Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:33 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact actual quartic and full signed units](Yin_C_G0407_v1.md#new-quartic-mixed-unit-identity) | Only the monic irreducible quartic/all four conjugates, trace and mixed unit identities with full norms+1/-1; all new scalar-denominator/width/rational-function and finite matrix deductions are local. |
| dependency | [Original integer-bundle normalization](Yin_C_G0397_v1.md#one-unit-complete-costs-and-boundary) | Only original scalar denominator, signed full norms, coefficient energy and actual degree/covariance distinction, without adopting a residual-projection converse. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:43 |
| status | proved |
| reason | Adopt after actual complete current SELF inspection of all original scalar-denominator/prime restrictions, independent/common twist and width arguments, explicit rational-function identities with full norms/poles/denominator cost, residual-covariance boundary and every exact finite Macaulay reduction/witness limit. Original three-case native objects were fully reconstructed read-only at the fixed domain, with all entries/ranks/pivots/witnesses matching and native bytes unchanged; original R279 initial author-check exposure remains SELF, and later L384 is separate from the original attempt. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0407_v1.md#new-quartic-mixed-unit-identity) | Only the monic irreducible quartic/all four conjugates, trace and mixed unit identities with full norms+1/-1; all new scalar-denominator/width/rational-function and finite matrix deductions are local. |
| dependency | [Exact accepted input](Yin_C_G0397_v1.md#one-unit-complete-costs-and-boundary) | Only original scalar denominator, signed full norms, coefficient energy and actual degree/covariance distinction, without adopting a residual-projection converse. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0632_v1.md#current-paraunitary-whole-finding) | Entire precise current Statement and complete necessary original analytical Sections1–6 plus finite Section8/equations1–13, full local Poisson proof, all original quotient/root/norm/sign/width/cost data, original exact three-case finite certificates and source/later/history/nonuniform boundaries. Actual whole relationship is self-reviewed. |

## Complete retained argument

<a id="argument"></a>
<a id="complete-rational-paraunitary-barriers"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="paraunitary-lift-reuse-and-domain"></a>
## 1. Reuse, source boundary and the exact lifting classes

The actual quartic and its mixed-unit identity are the complete accepted [L372 account](../ledger/Yin_L_G0372_v1.md#new-quartic-mixed-unit-identity), including its untwisted residual-energy failure and common-twist lower bounds.
[L367](../ledger/Yin_L_G0367_v1.md#one-unit-complete-costs-and-boundary) and [L318](Yin_C_G0600_v1.md#common-filter-cancellation-obstruction) already distinguish an algebraic identity from an actual projected covariance.
The [L318 polynomial Poisson majorant](Yin_C_G0600_v1.md#polynomial-poisson-majorant) supplies the elementary inside-circle bound used below.

A bounded local search for paraunitary, polyphase, loop groups, filter banks and rational spectral factorization found no result covering a rational-coefficient lift with the prescribed original quotient residues.
A bounded primary-source search located the UPM author repository's [2008 real two-channel FIR parameterization](https://oa.upm.es/2679/), DOI10.1016/j.sigpro.2008.01.009, whose abstract discusses all REAL FIR paraunitary filters and Bezout equations.
That abstract was read as a related lead only; its proof, coefficient-field preservation and quotient interpolation are NOT accepted inputs.
General complex/real factorization does not automatically preserve Q coefficients in the weighted form diag(1,2).
No external factorization, completion or strong-approximation theorem is invoked here.
The analytical arguments below are direct finite algebra, coefficient congruences and the already accepted Poisson calculation; they use no program or solver.
Section8 separately records the subsequently authorized and predeclared finite J85 attempt.
No novelty claim is made.

Fix the ACTUAL irreducible Salem polynomial and units from L372:

    P=t^4-2t^3+t^2-2t+1,
    alpha=t mod P, tau=alpha+alpha^-1,
    tau^2=2tau+1, tau_+=1+sqrt2,
    u_+=tau, u_-=(1-alpha)^-1=2+alpha^2-alpha^3,
    Norm_K(u_+)=+1, Norm_K(u_-)=-1.                  (1)

The real original roots are beta,beta^-1, beta>3/2 and beta+beta^-1=tau_+; the other two are the original circle pair.
Every prescribed residue below means equality modulo the WHOLE P, hence at every original conjugate.
Signed independent twists are allowed:

    f(alpha)=epsilon alpha^k u_+,
    g(alpha)=eta alpha^l u_-,
    epsilon,eta in{1,-1}, k,l in Z.                   (2)

The desired finite-support class is f,g in Q[t,t^-1] with the exact identity

    f(t)f(t^-1)+2g(t)g(t^-1)=1.                      (3)

For real rational coefficients, (3) is |f|^2+2|g|^2=1 on the ENTIRE circle.
We call (3) the weighted paraunitary identity only as a name for this explicitly given equation.
The common Laurent width is the largest exponent minus the smallest exponent in the UNION of both supports.
Multiplying both functions by the same monomial changes k,l by the same integer, preserves(3), and normalizes the union to[0,T].
This does not identify independent twists with common twists.

The larger class Q(t) of rational FUNCTIONS is kept separate in Section4.
A nonconstant polynomial denominator is an actual additional object, not a rational scalar coefficient denominator or a Laurent monomial.
The original least-energy projection representatives are a third separate requirement.

Authorship: the author developed the scalar-denominator restrictions, the common-twist real width calculation, the explicit rational-function lift and its exact norm/denominator costs.
After that scout, root supplied the independent-twist maximum-modulus/mod2 extension proposed in Section3.
The author verified it completely, replacing an uninspected maximum-modulus appeal by the retained Poisson calculation.
Root's contribution is substantive and is NOT independent whole-proof review of this draft.

<a id="paraunitary-scalar-denominator-primes"></a>
## 2. An exact arithmetic restriction on every rational finite-support lift

Let q be the LEAST positive integer making F=qf and G=qg integral Laurent polynomials.
Thus no prime dividing q divides every coefficient of F and G.
Equation(3) becomes

    F F^*+2G G^*=q^2, h^*(t)=h(t^-1),
    sum F_j^2+2sum G_j^2=q^2.                        (4)

**Theorem 1.** The minimal common scalar denominator q is odd.
No odd prime p for which-2 is a nonsquare modulo p can divide q.
Modulo2, F is a single monomial.
For the prescribed nonzero unit g in(2), q>=3.
These statements hold at every Laurent width; no finite coefficient search is involved.

*Proof at2.* If q is even, reduction of(4) modulo2 gives F F^*=0.
The Laurent polynomial ring over F2 is a domain, so every F coefficient is even.
Write F=2F_1,q=2q_1, divide(4) by2, and reduce again modulo2 to obtain G G^*=0.
Every G coefficient is even as well, contradicting minimal q.
For odd q, F F^*=1 modulo2.
If F had two distinct extreme exponents, the coefficient at their nonzero maximal difference in F F^* could not vanish.
Hence F mod2 is one monomial, with coefficient1.

*Proof at an odd nonsquare prime.* Suppose p divides q.
The reductions satisfy F F^*+2G G^*=0 over Fp[t,t^-1].
Evaluating at t=1, anisotropy of a^2+2b^2 over Fp forces F(1)=G(1)=0.
Both are divisible by t-1.
After dividing them by that factor, its nonzero Laurent norm(t-1)(t^-1-1) cancels from the zero identity, so the same argument applies again.
Multiplying by a common monomial first makes the two reductions ordinary polynomials; indefinite repeated division by t-1 forces both to be zero.
Thus p divides every original coefficient of F,G, again contradicting minimal q.
This is a direct local obstruction, not a unit-group or class-field assertion.

Finally q=1 and nonzero G are incompatible with the last(4), since the integer G coefficient energy alone contributes at least2.
Combined with odd q, this gives q>=3.
It is an arithmetic requirement, not a lower bound on the degree or existence of a lift.
In particular the unconstrained multi-component rational-square denominator2 in L372 is not a solution of this TWO-component weighted norm problem.

For the ACTUAL residues(2), all four original roots give

    Res(P,F)=q^4, Res(P,G)=-q^4.                      (5)

The signed monomial twists and signs have degree-four norm1 and do not change these values.
Individual contents divide q by integrality of their primitive original resultants, but no content is divided out while retaining the old norm/covariance.
All q and both full norm signs remain paid.

<a id="independent-twist-width-four-obstruction"></a>
## 3. No rational lift of common Laurent width at most four, even for independent twists

**Theorem 2.** No pair satisfying(2)--(3) with rational Laurent coefficients has common union width T<=4, for ANY independent integers k,l and either signs.

The key extension was supplied as a root scout and verified here.
Normalize the common union to[0,T].
Equation(3) gives |f|<=1 on the circle.
The L318 Poisson majorant, or its elementary kernel proof, then gives |f(r)|<=1 for0<r<1.
The same applies to its fixed-window reverse f_rev(t)=t^T f(t^-1), which has identical circle modulus.
At the TWO ACTUAL real embeddings this yields

    tau_+ beta^-k<=1,
    tau_+ beta^(k-T)<=1.                              (6)

Here tau_+>beta, while tau_+<beta^2: beta^2=tau_+beta-1 and tau_+(beta-1)>1 follow from beta>3/2,tau_+>2.
Therefore1<log(tau_+)/log beta<2, and the integer inequalities force2<=k<=T-2.
Width less than4 is impossible, and width4 forces k=2 independently of l.

Use Theorem1's odd q and F mod2=t^j with0<=j<=4.
The ACTUAL order modulo2 is

    O/2O=F2[t]/(Pbar), Pbar=t^4+t^2+1=(t^2+t+1)^2.

Its class alpha_bar is a unit with exact order6.
Indeed t^6+1=(t+1)^2 Pbar, whereas t^3+1 and t^2+1 have nonzero classes of degree below4.
Thus alpha_bar^6=1, but its order is neither1,2 nor3.
The relation Pbar also gives alpha_bar^-1=alpha_bar^3+alpha_bar and tau_bar=alpha_bar^3.
Reducing the prescribed F residue, valid because q is odd, therefore requires

    alpha_bar^j=alpha_bar^2 tau_bar=alpha_bar^5.      (7)

There is no j in[0,4] congruent to5 modulo6.
This contradicts F's monomial reduction.
The complete repeated reduction Pbar=Phi3^2 is retained; replacing it by only Phi3 would incorrectly reduce the order to3 and lose this obstruction.
This proves Theorem2 with independent g twists and no solver.

For context, the author's earlier COMMON-twist calculation independently excludes width4 even over real coefficients.
Put k=l=2, which the two-sided energy bounds force in that restricted case.
Every degree<=4 representative has

    f=t+t^3+aP,
    g=1-t+t^2-t^3+bP.

The required lag4 and lag3 equations are

    a^2+2b^2+2b=0,
    a-2a^2-(1+2b)^2=0.                              (8)

The first makes(1+2b)^2=1-2a^2, so the second forces a=1, impossible in the first over R.
This direct calculation is not a finite failed optimizer.
It concerns common twists over R; Theorem2 is the stronger independent-twist statement over Q, with its root-supplied arithmetic scout credited separately.

The first possible rational union width is therefore at least5.
This is a lower bound, not existence at5.
The same bounds give k in[2,T-2].
For g, the circle inequality |g|<=1/sqrt2 and beta<tau_+=1+sqrt2 force2<=l<=T-1.
At T=5 the finite possibilities are k=2,3 and l=2,3,4.
Reversal sends(k,l) to(5-k,6-l), with an allowed sign on g because sigma(u_-)=-alpha u_-.
These describe a precise possible finite next test; NONE has been run or excluded beyond Theorem2.

<a id="explicit-rational-function-norm-lift"></a>
## 4. An explicit exact rational-function lift, with its nonconstant denominator

There is a complete lift in the LARGER rational-function class.
Define

    D=t^4-8t^3+15t^2-8t+1,
    A=-t^4+4t^3-7t^2+4t-1,
    B=-2t^3+8t^2-8t+2,
    f_rat=A/D, g_rat=B/D.                            (9)

All coefficients are displayed integers, with no numerical approximation.
Put x=t+t^-1.
Then

    D/t^2=x^2-8x+13=2(2-x)+(3-x)^2,
    A/t^2=-x^2+4x-5=2(2-x)-(3-x)^2,
    B/t^2=2(3-x)(1-t^-1).

The difference of the first two squares is8(2-x)(3-x)^2, while(B/t^2)(B/t^2)^*=4(2-x)(3-x)^2.
Consequently

    A A^*+2B B^*=D D^*,
    f_rat f_rat^*+2g_rat g_rat^*=1                   (10)

as exact rational identities.
No real or integral spectral-factor theorem is presumed.

At every original conjugate, x=tau satisfies x^2=2x+1.
Therefore

    D(alpha)=2alpha^2(7-3tau),
    A(alpha)=2alpha^2(tau-3)=D(alpha)tau,
    B(alpha)=D(alpha)/(1-alpha).                     (11)

For the last identity use(3-tau)(2-tau)=7-3tau and(1-alpha)(1-alpha^-1)=2-tau.
The denominator is nonzero in K because Norm_F(7-3tau)=-2.
Thus the EXACT original prescribed UNTWISTED residues u_+,u_- are retained, at all four original roots.

On the circle x in[-2,2], D/t^2=x^2-8x+13 is decreasing and at least1.
There are no circle poles, and the identity is an actual bounded circle norm identity.
This fact does not make f_rat a Laurent polynomial: the numerator polynomials in x,2(2-x) plus/minus(3-x)^2, have no common root, since a common root would force x=2 and then3-x nonzero.
Thus gcd(A,D)=1.
The nonconstant D has genuine nonzero finite poles which no monomial multiplication removes.
Its trace roots4+sqrt3 and4-sqrt3 both exceed2, producing two positive reciprocal real pole pairs, one member of each inside the unit disk.
These poles explain why the polynomial inside-circle argument(6) does not apply to this lift.

The FULL original arithmetic cost is

    Res(P,D)=64,
    Res(P,A)=+64, Res(P,B)=-64.                       (12)

Indeed D(alpha)=2alpha^2(7-3tau), Norm_K(2)=16 and Norm_K(7-3tau)=Norm_F(7-3tau)^2=4; Norm_K(alpha)=1.
The numerator relations(11) then give the signs through the actual norms+1,-1.
D is not an original-order unit, and its full resultant64 must be retained; this is not a scalar q^4 normalization or a discarded common polynomial factor.
Its complete Mahler expense is the product of the two exterior reciprocal roots associated with4+sqrt3,4-sqrt3, and is strictly larger than1.
No zero or pole is removed from that expression.

The rational-function construction is a valid solved comparison class.
It does NOT solve the original Laurent-polynomial lift, nor imply that a scalar denominator allowed by Theorem1 can replace D.
Multiplying by D gives polynomial numerators with the altered norms(12), not the unit-residue/common-scalar conditions(5).

<a id="lifting-versus-residual-projection"></a>
## 5. A finite-support lift would still need the original residual comparison

If a future finite-support solution f,g exists, clearing its actual q gives integral F,G with(4)--(5).
A common monomial normalization places them in one actual window[0,T].
Their constant weighted circle covariance is1, so weights1/3,2/3 would have complete original energy q^2/3 and norm income logq, giving true surplus log3/2 BEFORE any change of representatives.
The full degree, denominator q, polynomial contents and signed original norms must remain.

However these F,G need not be the orthogonal least-energy residual representatives of their same original residues.
Projecting each into the original complement of P multiples decreases its individual coefficient norm, but does not preserve the exact constant polynomial FF^*+2GG^*.
The missing removed multiples and cross terms are real polynomial contributions.
Therefore even an exact finite-support paraunitary lift must be evaluated either as its own complete integer auxiliary bundle, paying its actual T/d and contents, or after a newly proved covariance comparison.
No residual complementarity is inherited merely from residue equality or least-energy optimality.

For the rational-function lift(9), even this finite integer auxiliary interface is absent until the nonconstant D is charged.
Its numerators have absolute full norm64 rather than q^4 and an additional denominator with two exterior pairs.
The circle norm identity alone gives no unrestricted Mahler gap or all-input degree bound.

<a id="paraunitary-lift-outcome-and-boundary"></a>
## 6. Outcome and discriminating next step

The new exact results are: every rational finite-support lift must use an odd scalar denominator avoiding all odd nonsquare-(-2) primes; the prescribed independent-twist lift has union width at least5; and an explicit bounded-circle rational-FUNCTION norm lift exists with its unavoidable displayed nonconstant denominator and full resultants+64,-64,64.
The broader arbitrary-degree rational Laurent-polynomial existence remains unresolved.

A useful finite next calculation was identified to address exactly the remaining width5 cases described after(8), with complete exact algebraic certificate or candidate verification and declared first-failure scope.
That proposal was UNRUN when the analytical Sections1--7 were first completed; its separately authorized actual first attempt is now recorded in Section8.
A useful theoretical continuation would remove the nonconstant denominator in(9) while preserving the original weighted norm, or show an obstruction at every degree; neither follows from a bounded width failure.
Any construction needs the actual original scalar denominator, degrees and covariance costs before a near-one/general G0001 inference.

<a id="width-five-declared-macaulay-attempt"></a>
## 8. Complete first bounded width-five certificate attempt

After the complete analytical text had been saved, root explicitly authorized one tiny new test.
The [J85 declaration](../computations/programs/Yin_J_G0085/readme.md) and [standard-library program](../computations/programs/Yin_J_G0085/main.py) were saved BEFORE any mathematical execution.
They fix exactly three canonical cases k=2,l=2,3,4, original width bound5, four coefficient variables a,b,c,d and a degree4 Macaulay PRODUCT bound.
There is no old L355 optimizer, extra original polynomial, alternative precision, random seed, automatic retry, larger multiplier degree or open-ended scan.

For each case, monic reduction gives the complete original seeds

    f_seed=t+t^3,
    g_seed=1-t+t^2-t^3 for l=2,
    g_seed=1-t-t^3 for l=3,
    g_seed=1-t-2t^3 for l=4.

Every width<=5 representative of those residues is f=f_seed+(a+bt)P and g=g_seed+(c+dt)P.
The full six equations E_h(a,b,c,d)=0, h=0,...,5, are the complete original coefficients of ff^*+2gg^*-1, including its constant equation and every positive lag.
Negative lags are identical because the formal coefficients are real.
The native report retains EVERY coefficient of these quadratic equations and all original lift coefficients; the reduction is not inferred from numerical sampling.

Let V_4 have the70 monomial basis elements in four variables of total degree<=4.
For EVERY nonzero equation E_h, include all multiplier monomials X^a with |a|+deg E_h<=4.
The90 resulting product columns form an exact integer70-by90 matrix A; b is the coefficient vector of1.
A unit-ideal certificate IN THIS DECLARED DOMAIN is exactly A z=b.
An exact left-null vector y with

    y^T A=0, y^T b=1                                 (13)

therefore proves only that1 is not in this degree-bounded product span.
It does NOT prove that the original nonlinear equations are feasible, that rational points exist, or that a larger-degree ideal certificate is absent.
A genuine found identity1=sum h_i E_i would exclude the whole corresponding case, but no such identity was found in this first attempt.

The sole native author execution used CPython3.12.14, integers and Fraction arithmetic only.
It started2026-10-11T14:20 and completed 2026-10-11T14:20; worker elapsed1.203seconds and supervisor elapsed1.312seconds, exit0, no60second outer timeout and no retry.
The native data.json (`mathematics/computations/outputs/Yin_J_G0085/data.json`) is COMPLETE for all three DECLARED ATTEMPTS.
Each full system has rank50 and augmented rank51, with its complete exactly checked witness(13).
The witness support sizes are46,44,49 respectively.
The author program directly checked every yA coordinate and yb exactly before recording an outcome.
The original complete matrices, rhs, row/multiplier exponent conventions, original equations, ranks/pivots and all witness entries are retained; no alleged width-five solution or exclusion is manufactured.

An inconsistent Macaulay system was a predeclared ordinary mathematical outcome, so all three cases were processed.
There was NO native failure, missing case, certificate identity, solver candidate or nonlinear-feasibility result.
The first-native-failure stop and outer supervisor remained in force; no higher-degree repair was attempted.
The exact conclusion is the three bounded certificate absences, leaving the degree5 rational paraunitary lifting question unresolved.
Root supplied the authorization and finite gate; implementation and algebraic reduction are by this author.
Separate noncontributor whole proof/program/data review is pending.

### Complete reused polynomial inside-circle proof

The following exact local Poisson calculation is the consumed portion of [L318](Yin_C_G0600_v1.md#polynomial-poisson-majorant), retained here so the width argument does not redirect its necessary proof.

<a id="polynomial-poisson-majorant"></a>
### 2. A polynomial square majorant retaining Fourier signs

Write F(t)=sum_(j=0)^T f_j t^j with real coefficients, permitting zero endpoints in this fixed degree window.
Set

    E_F=sum_j f_j^2,
    A_h(F)=sum_(j=0)^(T-h) f_j f_(j+h), 1<=h<=T.

For0<=r<=1 and |z|=1,

    |F(rz)|^2 <= E_F+2 Re sum_(h=1)^T A_h(F) r^h z^h.
                                                               (2)

Here is a complete elementary proof.
When0<=r<1, use the positive kernel

    K_r(theta)=(1-r^2)/|1-r exp(i theta)|^2
             =sum_(h in Z) r^|h| exp(i h theta).

The series follows by multiplying the two convergent geometric series; its constant term is1, so its normalized circle integral is1.
Convolution with this kernel sends exp(i j theta) to r^|j| exp(i j theta).
Consequently its average of F on the circle is F(rz), while its average of |F|^2 is the right side of(2), because the Fourier coefficients of |F|^2 are E_F and A_h(F).
Cauchy--Schwarz with respect to this positive probability density proves(2).
At r=1 it is the exact Fourier identity, also obtained by continuity.
This proves the required majorant without invoking a general theorem about subharmonic functions.

In particular, if the full circle modulus of an ordinary polynomial is at most1, the positive unit-mass kernel gives |F(rz)|<=1 for0<=r<=1.
The fixed-window reverse has the same full circle modulus, including actual zero end coefficients.
This is the only inside-circle interface used in the width proof above.

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0085](../computations/programs/Yin_J_G0085/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
