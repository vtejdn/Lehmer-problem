---
author: Yin
---

# General reciprocal Perron escape and arithmetic return constraints

Date: 2026-10-10.
Fixed retention by the assigned orbit_research AI for Yin, following the coordinating agent's explicit adoption instruction.
The arithmetic author developed the short-state and Laurent-box argument; the coordinator contributed the general reciprocal extension.
The retaining agent supplied none of this combined theorem and performed the original complete whole-proof check described in the adoption account below.
Its disclosed earlier contribution to the independently reviewed L173 input remains part of that review boundary.

<a id="reciprocal-profile-fixed-scope"></a>
## Adopted scope

For every irreducible reciprocal nontorsion unit of degree d>=12 and logarithmic Mahler measure 0<m<=log(4/3)/2, sufficiently large sigma-invariant finite-prime actual cores with r_S>=exp(-2m) satisfy the explicit zero-profile and restricted-word escape estimates below.
The proof uses the full Mahler measure, not the modulus of one chosen root.
General nonzero short polynomial states have an exact forbidden return interval and a complete original first-return mass bound, which becomes a finite auxiliary-chain occupation bound.
Reciprocal T-fixed Laurent coefficient boxes additionally control the normalized right-vector square with explicit degree, height and counting costs.

These are necessary constraints on actual finite-core profiles.
The Laurent boxes lie in a proper fixed subspace; no lower mass on that subspace, uniform spectral exclusion or unrestricted G0001 conclusion is adopted.
The fixed Salem result in [L181](Yin_L_G0181_v1.md) remains unchanged.
External ESS and Smyth inputs retain their existing inspection scopes.
No new source, computation or J is introduced by this proof-only retention.

The complete original proof and author-checking/contribution account follow.
Historical pending-review wording records the drafting stage; the dated restricted-retention statement above records its actual disposition.
Only heading depth and relative navigation are relocated.

<a id="retained-general-reciprocal-profile-proof"></a>
## General reciprocal Perron escape and short Laurent state returns

Date: 2026-10-10.
Responsible proof draft by resultant_research for Yin.
The coordinating agent proposed extending the fixed [L181](Yin_L_G0181_v1.md) Salem profile theorem to every irreducible reciprocal nontorsion algebraic unit.
That observation is a disclosed contribution.
This draft verifies the general field and collision interfaces and develops a separate arithmetic constraint for nonzero states represented in short polynomial or Laurent windows.
No numerical computation was needed.
Complete independent review is pending; unrestricted G0001 remains active and unresolved.

The fixed L181 remains unchanged at its adopted scope.
The argument below uses the original digit probabilities(1/4,1/2,1/4), explicitly distinguishes the finite auxiliary Doob chain, and retains degree, measure, prime-set and state-domain dependencies.
A forthcoming complete reviewer must be a noncontributor to the combined theorem; the coordinator's check alone would not meet that description.

### Responsible inputs and notation

The inputs are the [general reciprocal field involution in C214](../claims/Yin_C_G0214_v1.md#inverse-trace-orbit), the [complete collision rank bound in L154](Yin_L_G0154_v1.md#uniform-small-unweighted-return-tail), the [general actual-core radius identity in L173](Yin_L_G0173_v1.md#core-operator-collision-sandwich) and its [finite-prime exhaustion](Yin_L_G0173_v1.md#finite-prime-spectral-exhaustion), and the [finite Doob and occupation argument in L181](Yin_L_G0181_v1.md#finite-critical-return-profile).
The latter exhaustion retains the accepted ESS02 source dependency through L157.
The proofs of those external inputs are not re-audited here.
The general inequality h_2<=m will be recovered directly from the already proved norm-grid collision bound, so no Salem entropy approximation is imported.

For a nontorsion algebraic unit alpha of degree d, put O=Z[alpha], let P be its monic irreducible minimal polynomial, and put m=log M(P)>0.
In general m is not log|alpha|.
The ambient original process is X_(n+1)=alpha X_n+eta_n, with independent eta having probabilities p_(-1)=p_1=1/4 and p_0=1/2.
Write p_n=Pr_0(X_n=0); the identical notation p_eta for a one-step digit is distinguished by its subscript.
A finite-prime restricted core D_S consists of states on actual zero-to-zero words whose every nonzero intermediate state is an S-unit in the maximal order.
Its original killed matrix is K_S.
It is not replaced by the ambient intersection with the S-unit set.

For a nontrivial D_S, [L177](Yin_L_G0177_v1.md#finite-prime-near-one-size-cost) gives 1/2<r_S:=r(K_S)<1.
Put h_S=-log r_S.
Let v,w be positive right and left Perron vectors and use the finite auxiliary chain

    Q_S(x,y)=K_S(x,y)v(y)/(r_S v(x)),
    pi_S(x)=w(x)v(x)/sum_y w(y)v(y).                 (1)

These probabilities belong to the auxiliary chain only; the original matrix is unchanged.
Unless otherwise specified normalize the right vector by sum_x v(x)^2=1.

<a id="general-reciprocal-profile-escape"></a>
### 1. The profile theorem applies to every reciprocal nontorsion unit

Assume P is reciprocal.
The map sigma(alpha)=alpha^(-1) defines a field automorphism of Q(alpha): alpha^(-1) is another root of the same irreducible P, belongs to Q(alpha), and generates the same field.
Its square is the identity.
This is the already retained L9 involution, with no condition on the number or shape of off-circle conjugate pairs.
It preserves O because alpha is a unit, preserves the maximal order, and permutes its prime ideals.

Choose S invariant under sigma and define the additive involution

    T(x)=alpha^(-1)sigma(x).

Indeed T^2(x)=alpha^(-1)alpha x=x.
Since alpha is a unit, T preserves the set of nonzero S-units and fixes zero.
An original edge y=alpha x+eta satisfies

    alpha T(y)-eta=T(x).                            (2)

Thus the reversed transformed edge has digit -eta, with exactly the same original probability.
Reversing an entire restricted closed word proves that T preserves D_S.
If U is the permutation induced by T, then

    K_S^T=U K_S U,    U^2=I.

For the normalized positive right vector v, Uv is a left vector.
With c=<v,Uv>, positivity and Cauchy--Schwarz give 0<c<=1 and

    pi_S(x)=v(x)v(Tx)/c;
    T(x)=x implies v(x)^2<=pi_S(x).                 (3)

In particular this holds at zero.
Prime invariance is a hypothesis; it is achieved cofinally by replacing any finite set by its union with its sigma image.

The required entropy upper bound is general.
The already proved [L154 equation(11)](Yin_L_G0154_v1.md#complete-weighted-return-tail-lower-bound), using the L91 norm-grid support estimate and Cauchy--Schwarz, says

    p_n >= (4n)^(-d) M(P)^(-(n-1)).                 (4)

At each fixed input, take -logarithms, divide by n and let n tend to infinity.
The original collision-rate existence and L173 radius identity give

    h_2(alpha)<=m,    r(K_act)=exp(-h_2)>=exp(-m).

No degree-varying limit is used in this step.
L173 proves r_S increasing to r(K_act) along a cofinal finite-prime exhaustion.
Since m>0, the limiting radius is strictly above exp(-2m), so every sufficiently large term of a symmetrized exhaustion satisfies

    r_S>=exp(-2m).                                  (5)

This is a lower bound on a finite radius, not a lower entropy estimate from a finite compression.

Now assume

    d>=12,    0<m<=log(4/3)/2,
    sigma(S)=S,    r_S>=exp(-2m).                    (6)

Every line of the L181 finite argument applies: its first-return estimate already holds for all units; equations(2)--(3) give the needed left/right comparison; and(4)--(5) supply the cofinal radius condition.
For completeness, writing

    T_d=d 2^(-d)[1+8/(3(d-2))],
    b=1-1/(2r_S),

the finite occupation and Jensen identities give

    pi_S(0)<=h_S/[b log(b/T_d)]

whenever the displayed logarithm is positive.
Under(6), h_S<=2m, r_S>=3/4 and b>=1/3.
For d>=12,

    T_d<=(13/9)d 2^(-d),
    3T_d<=2^(-d/2),

by the retained elementary estimate (13/3)d<=2^(d/2).
Hence the logarithm is at least d log2/2, and

    pi_S(0)<=12m/(d log2),
    v(0)^2<=12m/(d log2),
    E_(Q_S,0) tau_0>=d log2/(12m).                  (7)

Here tau_0 is the first positive return under the auxiliary chain.
The same edgewise Perron bound v(y)<=4r_S v(x) proves, for the ball B_R(S) reached from zero in at most R actual restricted edges,

    sum_(x in B_R(S)) v(x)^2
       <=[(48^(R+1)-1)/47] 12m/(d log2).             (8)

Thus the entire explicit L181 degree/measure profile and restricted-word escape conclusion extends to every irreducible reciprocal nontorsion unit.
The constants do not depend on the number of expanding conjugate pairs.
All state sets, vector normalizations and path restrictions do depend on the input as stated.

The [accepted reduction in L1, Section2](Yin_L_G0001_v1.md) says that any hypothetical sequence of positive Mahler measures tending to zero can be reduced to irreducible reciprocal noncyclotomic monic units of unbounded degree.
Its nonreciprocal step accepts Smyth's theorem at the audited survey-statement scope; the original 1971 proof was not audited there and is not newly adopted here.
Consequently(7)--(8) impose a necessary profile pattern on that full unresolved near-one class, including multiple expanding pairs.
This corrects the scope restriction of the earlier Salem application; it neither reduces the class to Salem numbers nor proves a uniform gap.

<a id="short-state-return-rarity"></a>
### 2. Nonzero short polynomial states have a forbidden return interval

This section does not require reciprocity.
Let alpha be any nontorsion algebraic unit of degree d>=3.
Suppose x is nonzero and has an integer polynomial representative X(alpha), with e=deg X<d.
An original length-n return to x gives

    (alpha^n-1)X(alpha)+Q_n(alpha)=0,
    Q_n(t)=sum_(j=0)^(n-1) eta_j t^(n-1-j).

The integer polynomial (t^n-1)X(t)+Q_n(t) is nonzero of degree n+e: its highest coefficient comes from t^n X and cannot cancel against -X or Q_n, whose degrees are e and at most n-1.
Since it vanishes at alpha, irreducibility gives

    n>=d-e.                                        (9)

This concerns returns to the nonzero state itself, including the absence of a one-step self-loop when d-e>1.
It does not assert that a short representative gives a short path from zero.

The complete displacement law mu_n is an autocorrelation of the fair binary law nu_n.
As proved in [L173, Section3](Yin_L_G0173_v1.md#core-operator-collision-sandwich),

    Pr_x(X_n=x)=mu_n((1-alpha^n)x)<=mu_n(0)=p_n.    (10)

This is an ambient return bound with the original digit probabilities.
Every restricted first return to x is a subset of this event.
For n<d, a zero displacement has a polynomial relation of degree at most n-1<d, so every eta_j is zero and p_n=2^(-n).
For n>=d, L154's basis-block proof gives

    p_n<=b_(floor(n/d))^d,
    b_q=binom(2q,q)/4^q,
    sum_(n>=d) p_n<=d sum_(q>=1)b_q^d<=T_d.         (11)

The last bound follows from the complete collision estimate itself, not just from the first-return conclusion recorded there: each block qd<=n<(q+1)d has exactly d terms.
All terms are nonnegative and the convergent rank bound applies for d>2.

For x in a nontrivial finite restricted core, let f_(n,x)^S be its original first positive return masses and a_x=sum_n f_(n,x)^S.
Equations(9)--(11) give

    0<a_x<=A_(d,e),
    A_(d,e):=2^(1-d)(2^e-1)+T_d.                   (12)

Indeed the possible terms before d start at d-e, and their sum is at most sum_(n=d-e)^(d-1)2^(-n)=2^(1-d)(2^e-1).
This sum is empty when e=0.
The later terms are bounded by(11).
Positivity follows from finite-core irreducibility.

The auxiliary first-return distribution at any x is q_(n,x)=f_(n,x)^S r_S^(-n); telescoping in(1) cancels the endpoint vector at x as it does at zero.
A finite irreducible chain returns almost surely with finite mean.
The occupation argument from L181, now starting and ending at x, gives E_(Q_S,x) tau_x=1/pi_S(x).
Thus

    a_x=E_(Q_S,x) exp(-h_S tau_x),
    1/pi_S(x)>=max{d-e, log(1/A_(d,e))/h_S}.        (13)

Jensen gives the second term, using a_x<=A_(d,e); the first term is the exact forbidden interval(9).
In particular, if A_(d,e)<1,

    pi_S(x)<=h_S/log(1/A_(d,e)).                    (14)

Unlike the zero-state proof, there is no separately normalized one-step mass b here: the entire return distribution at a nonzero short state has the arithmetic small-mass bound(12).
Neither(13) nor(14) presumes recurrence or critical normalization of the infinite original process.

<a id="reciprocal-laurent-profile-boxes"></a>
### 3. A concrete family of T-fixed arithmetic states

Return to reciprocal P and sigma-invariant S.
Fix integers L>=1 and H>=0 with 2L-1<d, and form the explicit finite set

    C_(L,H)={sum_(j=0)^(L-1) a_j(alpha^j+alpha^(-j-1)):
                              a_j in Z, |a_j|<=H}.  (15)

Every element is an algebraic integer in O and is fixed by T.
This is a particular additive sublattice window; it is not the whole order or all actual core states.
These (2H+1)^L coefficient vectors give distinct states: multiplying a nonzero difference by alpha^L would give a nonzero integer polynomial of degree at most 2L-1<d vanishing at alpha.
Its nonzeroness also follows directly from the distinct nonnegative powers supplied by alpha^L alpha^j and the distinct lower powers supplied by alpha^L alpha^(-j-1).

For a nonzero x in(15), let ell-1 be the largest index with nonzero a_j, so 1<=ell<=L.
Its displayed Laurent representative X(t) has extreme exponents -ell and ell-1, with nonzero equal extreme coefficients.
For a length-n return, multiply the relation (t^n-1)X(t)+Q_n(t) by t^ell.
The result is an integer polynomial whose leading degree is n+2ell-1.
This term comes from t^(n+ell)X; the other two degrees are at most 2ell-1 and n+ell-1, strictly smaller for n>=1, ell>=1.
Therefore

    n>=d-(2ell-1)>=d-(2L-1).                        (16)

The argument of(10)--(14) uses only this return exclusion, not that the representative is an ordinary polynomial of the displayed degree.
It consequently applies verbatim with e=2L-1:

    pi_S(x)<=h_S/log(1/A_(d,2L-1)),
    v(x)^2<=pi_S(x),                               (17)

for nonzero x in D_S intersect C_(L,H), provided A_(d,2L-1)<1.
The second inequality uses the exact T-fixed property in(3).
Core membership is explicitly intersected; no assertion that every coefficient vector is reachable or co-returnable is needed.

There is a simple uniform-in-height window estimate.
Under(6), also assume

    d>=4L+2.                                       (18)

Writing e=2L-1, this gives e<=d/2-2.
The estimates in Section1 give T_d<=(1/3)2^(-d/2), while

    2^(1-d)(2^e-1)<2^(1-d+e)<= (1/2)2^(-d/2).

Hence A_(d,e)<(5/6)2^(-d/2)<2^(-d/2).
Combining(17) with h_S<=2m yields

    x nonzero in D_S intersect C_(L,H)
       implies pi_S(x)<=4m/(d log2),
               v(x)^2<=4m/(d log2).                (19)

Including zero with the separate bound(7), and using the exact cardinality of(15), proves

    sum_(x in D_S intersect C_(L,H))v(x)^2
       <=[4(2H+1)^L+8] m/(d log2).                 (20)

The same estimate holds for the sum of pi_S over that intersection.
Every dependence is explicit.
In a hypothetical m tending to zero family from Section1, d tends to infinity and(18) eventually holds for any fixed L,H.
Both masses on that fixed-complexity arithmetic box then tend to zero.
If such a box is to carry at least one half of the right-profile norm squared, a necessary condition is

    (2H+1)^L >= d log2/(8m)-2,                      (21)

whenever(6) and(18) hold.
This is an arithmetic representation constraint, distinct from the restricted-word distance estimate(8); it does not depend on the availability or length of a chosen zero-to-state path.

### 4. What this adds and what remains open

The general reciprocal extension is needed for the unrestricted near-one core and uses only already valid general interfaces.
The new return exclusion(9)/(16), combined with the complete maximum-atom and rank bounds, yields a separate constraint at explicitly represented nonzero arithmetic states.
In particular one cannot explain a near-one finite Perron profile by placing a uniformly positive mass on a fixed T-fixed integer coefficient box.
The original finite chains would have to send both their stationary mass and right-vector norm away from each such box while their exact [L177 Dirichlet energy](Yin_L_G0177_v1.md) tends to zero.

There is no contradiction so far.
The boxes in(15) lie in a proper T-fixed additive subspace; they are not a growing exhaustion of every core state as L changes without restriction, and no lower mass bound on that subspace has been proved.
For general non-T-fixed short polynomial states, (14) controls the stationary product of left and right vectors, not the right-vector square separately.
Outside the small-window condition(18), the exact bound(12)--(14) remains the relevant one and can become weak or vacuous.
Increasing H,L carries the explicit counting cost in(20).
No exchange of degree, finite-prime, or infinite-time limits removes these dependencies.

A discriminating continuation would have to connect the full reciprocal edge energy to mass on controlled arithmetic representations, or to derive an equally explicit obstruction on states escaping all these windows.
Integrality of 4K_S, connectivity through zero and finite-prime approximation alone do not supply that missing mass constraint.
The present theorem is a necessary condition on genuine actual-core profiles, not an independently constructed near-one family or a uniform spectral exclusion.

### 5. Contribution and check boundary

The coordinating agent proposed the extension from Salem inputs to every reciprocal unit using the involution, original edge reversal and the general collision/radius bound.
The arithmetic agent verified the precise existing hypotheses, reconstructed the general proof in Section1, and derived Sections2--3 and their interpretation, including the nonzero-state leading-term argument, all-return summation, finite critically tilted occupation bound, T-fixed Laurent boxes and exact constants.
The field involution, maximum-atom inequality, norm-grid estimate, rank bound, ESS finite-prime theorem and zero-profile calculation are fixed-interface reuse with links above; no historical novelty is claimed for these ingredients or for the assembled argument.

The author self-checked the polynomial noncancellation, both Laurent extreme exponents, exact low-degree return probabilities, block counting in(11), direction of Jensen and of finite-prime radius approximation, finite positive-return normalization at an arbitrary state, the distinction between a stationary product and a right-vector square, box injectivity, the constants in(19)--(21), and all fixed-input/family limit boundaries.
No mathematical program or J was needed, and no new source theorem was acquired.
Complete noncontributor review of this draft is pending.
Both agents are contributors to the combined theorem; a coordinator check would be contributor-aware.
G0001 remains unresolved.







<a id="reciprocal-profile-retention-record"></a>
## Original adoption and contribution boundary

The coordinating agent contributed the general reciprocal extension.
The arithmetic author verified the general interfaces and supplied the nonzero short-state and Laurent-box deductions.
On2026-10-10 the separately assigned orbit_research reviewer checked the complete frozen D53 notation, Sections1--5/equations(1)--(21), both return exclusions, all finite-chain/constants/box/family limits and the invoked L1 Section2 near-one reduction, finding no mathematical defect or missing hypothesis.
Its exact mathematical input is the original [retained combined D53 argument](#retained-general-reciprocal-profile-proof), with the actual full-Mahler and accepted ESS/Pet20/Smyth source boundaries.
It supplied none of D53 and had authored part of the previously fixed L173 input.
That upstream authorship does not establish target-proof participation.
The actual initial mathematics in the shared context and assigned focus is unestablished, so its original whole relationship is unknown.
The original listed author checks remain [SELF in R85](../audits/reviews/Yin_R_G0085_v1.md#reciprocal-profile-original-author-check-finding), without inventing another whole author event or an actual coordinator check from the hypothetical contributor-aware sentence.

The original2026-10-10 adoption instruction above followed that complete noncontributor check, and the orbit agent retained the D53 proof under that instruction.
This was restricted mathematical retention, not C acceptance or Task completion.
The [later R660 whole finding](../audits/reviews/Yin_R_G0660_v1.md#isolated-general-reciprocal-whole-finding) is a new2026-10-22 inspection of C448v2 and an explicit comparison of the complete original D53 scope and source history.
It does not substitute a later review for the old dated adoption.
No program, output or previously fixed mathematical statement is changed.
Later substantive work requires its responsible material/version and corresponding review.
