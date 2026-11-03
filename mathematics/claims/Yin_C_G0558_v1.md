---
author: Yin
---

# Complete balanced-overlap powers and genuine infinite-core composition costs

The complete original [L301](../ledger/Yin_L_G0301_v1.md) argument is retained here with both balanced parities and the full actual relative-degree expense.
Its original author and [R776 whole review](../audits/reviews/Yin_R_G0776_v1.md#complete-overlap-complete-independent-review) retain their own dates, actual contribution/source boundaries and fixed inputs.

<a id="statement"></a>
## Complete statement

Let alpha be an ACTUAL algebraic unit with the full original difference law1/4,1/2,1/4.
Torsion is allowed in the finite-word and composition identities.
Write p_n(alpha)=Pr(sum_(j<n)eta_j alpha^j=0),p_0=1 and, for l,N>=0,

    D_l=p_(2l)/p_l^2,
    E_l=p_(2l+1)/(p_l p_(l+1)),
    B_N=p_N/(p_floor(N/2) p_ceil(N/2)).

These formulas explicitly extend D_0=E_0=B_0=B_1=1 in THIS theorem.
For EVERY L>=1 let A_alpha(L)=sup_(l>=L)D_l and C_alpha(L)=sup_(N>=2L)B_N=sup_(l>=L)max(D_l,E_l), with infinity and unattained suprema allowed.
Then p_n/2<=p_(n+1)<=p_n and

    (1/2)max(D_l,D_(l+1))<=E_l<=2min(D_l,D_(l+1)),
    A_alpha(L)<=C_alpha(L)<=2A_alpha(L).

If the extended limit C_alpha(infinity)=lim_L C_alpha(L) is finite, it implies actual critical recurrence F_alpha(R)=1 and mean mu_alpha<=C_alpha(infinity), with R=exp(h2(alpha)).
No converse from finite mean to this all-late certificate is asserted.

For EVERY genuine radical gamma^r=alpha with integer r>=1 and ACTUAL relative degree[Q(gamma):Q(alpha)]=r, the actual order/core product gives

    p_(rl+s)(gamma)=p_l(alpha)^(r-s)p_(l+1)(alpha)^s,
                          l>=0,0<=s<r,
    h2(gamma)=h2(alpha),R(gamma)=R(alpha).

There is no1/r entropy factor.
For every N=2rl+t,0<=t<2r, the COMPLETE balanced overlap is

    B_N(gamma)=D_l^(r-t)E_l^t,             0<=t<=r,
    B_N(gamma)=E_l^(2r-t)D_(l+1)^(t-r),   r<=t<2r.

Thus for EVERY L>=1,

    sup_(N>=2rL)B_N(gamma)=C_alpha(L)^r,
    C_gamma(infinity)=C_alpha(infinity)^r.

For EVEN r the ordinary midpoint alone has the stronger exact identity
sup_(n>=rL)D_n(gamma)=C_alpha(L)^r and limsup_n D_n(gamma)=C_alpha(infinity)^r.
For arbitrary r,
A_alpha(L)^r<=sup_(n>=rL)D_n(gamma)<=[2A_alpha(L)]^r.
The exact realizing times, all original words, both split parities, powers and cutoff/onset costs are retained.
Existence of some finite eventual D-bound transfers in both directions at this actual relative-degree scope.

For beta>1 with ACTUAL irreducible P4=t^4-t^3-t^2-t+1, and EVERY r=2^k,k>=0, gamma_r=beta^(1/r) has ACTUAL minimal P4(t^r) of degree4r, constant1 and neutral real dimension2r.
The elementary nonsquare/negative-real-conjugate induction in the proof establishes every degree.
All original roots are retained, TOTAL m(gamma_r)=log beta=m_0>0 is constant, h2 is unchanged, and the ACTUAL core is the infinite Cartesian product D_actual(beta)^r.
For r>1 the inputs have r expanding conjugates and are not Salem or a near-one sequence.

C526/C546 give actual base recurrence and extended mu_beta>3/2.
For every dyadic r>=2,

    limsup_n D_n(gamma_r)=C_beta(infinity)^r
                          >=mu_beta^r>(3/2)^r.

Beyond EVERY onset there are later values above this threshold, not necessarily every later value.
Any finite eventual upper constant C_r must satisfy
C_r>=C_beta(infinity)^r>exp[(log(3/2)/4)degree(gamma_r)], regardless of its input-dependent onset.
If mu_beta is finite, every radical is positively critically recurrent with mu_(gamma_r)=mu_beta^r and stationary zero mass mu_beta^-r; its full bounded convolution norm is the same mean.
If mu_beta is infinite, the recurrent base is null recurrent and no radical acquires finite-mean attainment, while radicals may be null recurrent or transient under the exact C493 power-sum test.
These exhaustive branches exclude a finite subexponential-degree mean upper theorem on ALL recurrent members including the base, without classifying the unresolved base mean or exhibiting an unconditional positive-recurrent infinite core.
The fixed positive m_0 does not refute a sufficiently-small-total-m, Salem-only or exponential-degree-cost theorem.

For ANY monic irreducible unit polynomial P(t)=sum a_j t^j of degree D, let r=gcd{j>=1:a_j!=0} and P(t)=Q(t^r),d=deg Q=D/r.
Then Q is the actual monic irreducible unit polynomial of beta=alpha^r and has positive-exponent gcd one, called composition-primitive here only in this coefficient sense.
The relative degree is exactly r.
One has m(alpha)=m(beta), h2(alpha)=h2(beta), actual core D_beta^r, finite-mean attainment at alpha IFF at beta, and, when attained, mu_alpha=mu_beta^r.
The complete balanced-tail equalities above hold with onset2rL.
Recurrence only has the implication from alpha to beta; the reverse may fail according to sum_l(R^l p_l(beta))^r.
Every Salem polynomial already has r=1.

A unit Mahler gap on this coefficient-normalized class would therefore imply the same unit gap without normalization.
A HYPOTHETICAL theorem giving recurrence and mu<=A d/m on ALL normalized nontorsion units in some0<m<=epsilon domain, with fixed finite A, would contradict C557 when also m<=2^-16 and log(1/m)>24A.
If that upper theorem were merely conditional on recurrence, transient normalized inputs would remain uncovered.
No such upper theorem, recurrence coverage, new program/source, actual near-one family or unrestricted gap is proved here.

## Complete argument

<a id="argument"></a>

<a id="complete-overlap-reuse"></a>
### 1. Changed target and exact reuse

The complete [C557 critical-delay result](Yin_C_G0557_v1.md#statement) supplies a necessary recurrent mean expense d log(1/m)/(24m) on its tiny-total-measure domain.
It does not give an upper mean estimate.
The initial possibility of using essential spectral radius or reciprocal reversal to rule out finite mean is already excluded as an unsupported inference by [L240](../ledger/Yin_L_G0240_v1.md#critical-convolution-bounded-density-test) and [L236](../ledger/Yin_L_G0236_v1.md).
Those mechanisms are not asserted anew here.

The useful fixed inputs are [C555 whole midpoint/dyadic identities and eventual-bound implication](Yin_C_G0555_v1.md#bounded-doubling-critical-mean-test), [C493 actual radical order/core product and two-way attainment theorem](Yin_C_G0493_v1.md#statement), the [C396 actual infinite quartic core](Yin_C_G0396_v1.md#quartic-infinite-core-theorem), [C526 unconditional critical recurrence for that quartic](Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation), and [C546 exact quartic mean lower bound](Yin_C_G0546_v1.md#statement).
Their actual scopes were read.
In particular L293's repaired argument does not infer infinite mean from unbounded overlaps.
L206 already proves the product mean law and already treats the finite golden core, singleton reciprocal cores and some infinite radical cores.
Those are reused statements, not new discoveries here.

The changed calculation keeps BOTH balanced split parities and obtains an exact complete-tail envelope under actual radical composition, at every cutoff and with no unknown critical radius in the observable.
A separate elementary irreducibility check makes this calculation apply to an entire reciprocal family of ACTUAL infinite quartic-core powers.
The resulting all-late obstruction is stronger in its time quantifier than a finite large peak; it does not require deciding the quartic mean.
Finally, removing the common exponent divisor of a minimal polynomial gives a precise way to avoid paying an artificial composition expense in a future upper-mean theorem.
The elementary polynomial normalization is not claimed as a new irreducibility theorem.
The local exponent-gcd search found the relevant radical identities in L5/L206 and the unrelated minimal-relation gcd interfaces in L44; no additional source theorem is needed for the direct coefficient and quadratic-field calculations below.

No new external source, renewal limit theorem, prime-binomial theorem, numerical experiment or continuing program is used.
There is no novelty-priority claim.
The retained critical Markov/attainment attributions remain those in L201/L206, at their existing inspection boundaries.
Root supplied the broad question only, and no simultaneous D165 deduction is a premise.

Let alpha be an actual algebraic unit, with the ORIGINAL independent difference digits eta in{-1,0,1} of probabilities1/4,1/2,1/4.
For this section and the next two, torsion is permitted.
Put

    p_n(alpha)=Pr(sum_(j<n) eta_j alpha^j=0), p_0=1,
    D_l(alpha)=p_(2l)/p_l^2, l>=0,
    E_l(alpha)=p_(2l+1)/(p_l p_(l+1)), l>=0,
    B_N(alpha)=p_N/(p_floor(N/2) p_ceil(N/2)), N>=0.     (1)

The definitions explicitly give D_0=E_0=B_0=B_1=1.
They extend the previous positive-time D notation only to make finite identities at the initial endpoint unambiguous.
All denominators are positive, because of the all-zero word.
B_(2l)=D_l and B_(2l+1)=E_l.
Concatenation makes every value at least one.
E_l is the genuine split into lengths l and l+1, not an independent-law approximation or a square-norm assertion.

For L>=1 define the extended COMPLETE tail quantities

    A_alpha(L)=sup_(l>=L) D_l(alpha),
    C_alpha(L)=sup_(N>=2L) B_N(alpha)
             =sup_(l>=L) max{D_l(alpha),E_l(alpha)}.    (2)

The suprema may be infinite.
They are not finite enumerations.
Write C_alpha(infinity)=lim_(L->infinity) C_alpha(L), also in the extended sense.
Thus C_alpha(infinity)=limsup_N B_N(alpha).

<a id="balanced-overlap-parity-cost"></a>
### 2. The odd split has a fully paid original-law comparison

For every n>=0 the unchanged digit law gives

    (1/2)p_n <=p_(n+1)<=p_n.                           (3)

The lower bound retains only the last zero difference digit.
For the upper bound, let nu_n be the actual fair-binary endpoint probability on the additive order.
Then p_n=sum_x nu_n(x)^2, while nu_(n+1) is the average of nu_n and its translate by alpha^n.
The elementary inequality ((a+b)/2)^2<=(a^2+b^2)/2, summed over the finite support, gives the result.
No ergodicity, spectral theorem or stationary law is used.

Consequently, for every l>=0,

    (1/2)max{D_l,D_(l+1)} <=E_l
                   <=2min{D_l,D_(l+1)},
    A_alpha(L)<=C_alpha(L)<=2A_alpha(L).               (4)

For example E_l/D_l=(p_(2l+1)/p_(2l))(p_l/p_(l+1)); both factors lie in[1/2,1] and[1,2], respectively.
Likewise E_l/D_(l+1)=(p_(2l+1)/p_(2l+2))(p_(l+1)/p_l) lies in[1/2,2].
This proves the first line, including l=0.
The second line follows termwise from E_l<=2D_l.
Thus boundedness of the entire balanced tail is equivalent to the eventual original D-bound, with an explicit factor two; no unjustified log-convexity of p_n is assumed.

In particular L293's complete dyadic argument implies

    C_alpha(infinity)<infinity
       => F_alpha(R)=1 and mu_alpha:=R F_alpha'(R)
                                            <=C_alpha(infinity). (5)

Here R=exp(h_2(alpha)) is the TRUE original radius, and the inference uses every sufficiently late time: apply L293 to any C>C_alpha(infinity), then decrease C to that limit.
The unit attainment/convolution consequences are precisely those retained in L201/L240.
Without(5)'s finite-tail hypothesis, no recurrence or finite-mean classification is being made.

<a id="exact-complete-tail-composition"></a>
### 3. An exact complete-tail power identity, not only sampled times

Suppose gamma^r=alpha and [Q(gamma):Q(alpha)]=r, for an integer r>=1.
L206 then identifies the ACTUAL order as the direct sum of gamma^j Z[alpha],0<=j<r, the actual core as D_alpha^r, and the chronological kernel after r steps as the r-fold product.
Its complete iid coefficient identity is

    p_(r l+s)(gamma)=p_l(alpha)^(r-s) p_(l+1)(alpha)^s,
                         l>=0,0<=s<r.                (6)

All r residue classes have their original weights.
In particular h_2(gamma)=h_2(alpha), with no factor1/r, and the full critical radius is common.
We reuse(6); the new calculation concerns its entire balanced-tail consequence.

For any N=2r l+t, l>=0 and0<=t<2r, direct substitution into(1) and(6) gives

    B_N(gamma)=D_l(alpha)^(r-t) E_l(alpha)^t,
                                             0<=t<=r;
    B_N(gamma)=E_l(alpha)^(2r-t) D_(l+1)(alpha)^(t-r),
                                             r<=t<2r. (7)

The two expressions agree at t=r.
To check the parity and all multiplicities, when t<=r the numerator of B_N is p_(2l)^(r-t) p_(2l+1)^t.
The two denominator lengths are r l+floor(t/2) and r l+ceil(t/2); their product is p_l^(2r-t) p_(l+1)^t.
This is exactly the first expression, whether t is even or odd.
When t>=r the numerator is p_(2l+1)^(2r-t) p_(2l+2)^(t-r), while the denominator is unchanged.
This gives the second expression.
The formula at t=r can equivalently be obtained from the endpoint representation r(2l+1).
There is no discarded odd time or unmatched chronological endpoint.

For EVERY cutoff L>=1 the result is the exact extended equality

    sup_(N>=2rL) B_N(gamma)=C_alpha(L)^r.              (8)

Indeed every expression in(7) is a product of r factors bounded by C_alpha(L), since l>=L and l+1>=L.
Conversely N=2r l realizes D_l^r, and N=2r l+r realizes E_l^r for every l>=L.
Their supremum is C_alpha(L)^r, also when infinite or unattained.
Neither direction exchanges a supremum with an unproved limit.

If r is even, BOTH of those realizing N are even.
Therefore the usual midpoint statistic alone satisfies the stronger exact identity

    sup_(n>=rL) D_n(gamma)=C_alpha(L)^r,
    limsup_(n->infinity)D_n(gamma)=C_alpha(infinity)^r,
                                                      r even. (9)

For arbitrary r one always has

    C_gamma(infinity)=C_alpha(infinity)^r,
    A_alpha(L)^r<=sup_(n>=rL)D_n(gamma)
                                      <=[2A_alpha(L)]^r. (10)

The first equality follows from(8), because cutoffs2rL are cofinal among all positive cutoffs; the second uses the realizing times n=r l and(4),(8).
These are complete all-late identities/inequalities.
Their expense is exponential in the actual composition multiplicity r, not a time-sampling loss.
Given an eventual base bound D_l<=C for all l>=L, (10) gives the valid lifted bound D_n<= (2C)^r for ALL n>=rL, while (8)--(9) state its exact balanced refinement.
All onset factors are displayed.

In particular the existence of SOME finite eventual D-bound is preserved in both directions under a genuine radical: from base to lift use(10); from lift to base use D_(r l)(gamma)=D_l(alpha)^r.
This is a statement about this sufficient certificate.
It does not add a converse from finite mean to eventual boundedness, which has not been proved here or imported via a renewal limit theorem.

<a id="quartic-radical-irreducibility"></a>
### 4. A genuine reciprocal infinite-core family at every dyadic degree

Let beta>1 be the root of

    P(t)=t^4-t^3-t^2-t+1,
    u=beta+beta^(-1)=(1+sqrt(13))/2.                  (11)

L169 proves its actual irreducible degree four, its two positive real conjugates beta,beta^(-1), its nonreal unit-circle pair, and its infinite actual core.
We check the remaining degree obligation for

    r=2^k, gamma_r=beta^(1/r)>0,
    P_r(t)=P(t^r)=t^(4r)-t^(3r)-t^(2r)-t^r+1.         (12)

First beta is NOT a square in K=Q(beta).
The reciprocal involution sigma sends beta to beta^(-1); its fixed field is K_+=Q(u), because K/K_+ has degree two.
If x in K satisfied x^2=beta, then x sigma(x)=+1 or-1.
In the first case x+x^(-1) belongs to K_+ and its square is u+2.
In the second case x-x^(-1) belongs to K_+ and its square is u-2.
But

    N_(K_+/Q)(u+2)=3,
    N_(K_+/Q)(u-2)=-1.                               (13)

Neither can be a square in K_+: the norm of a square is the square of a rational number, which is neither3 nor-1.
These norms follow directly from u^2-u-3=0, whose other root u' has u+u'=1 and uu'=-3.
Thus t^2-beta is irreducible over K, and gamma_2 has actual degree eight.

For the induction, suppose r>=2 and P_r is irreducible.
Since r is even, -gamma_r is also a real root of P_r, so it is an actual negative real conjugate of gamma_r.
A square in Q(gamma_r) has nonnegative value at every real embedding.
Hence gamma_r cannot be a square in its own field.
Adjoining its positive square root has relative degree two, and P_(2r) is its actual minimal polynomial, by degree.
This proves(12) irreducible for every dyadic r, including the base r=1, without using a general binomial irreducibility theorem or an unproved Kummer premise.

Every P_r is reciprocal, monic and has constant1.
All r roots above beta have modulus beta^(1/r), all r roots above beta^(-1) have modulus beta^(-1/r), and the2r roots above the neutral pair have modulus one.
Consequently

    degree(gamma_r)=4r,  q_neutral(gamma_r)=2r,
    m(gamma_r)=log M(P_r)=log beta=:m_0,
    h_2(gamma_r)=h_2(beta),
    D_actual(gamma_r)=D_actual(beta)^r.               (14)

The last identity is the full L206 actual-core theorem under the degree condition just proved.
Every one of these cores is infinite, and every probability below is still the original1/4,1/2,1/4 law.
The full total measure stays fixed even though each individual expanding modulus tends to one.
For r>1 these are NOT Salem numbers: there are r expanding conjugates rather than one.
They are actual reciprocal multiple-expanding inputs, not cyclotomic degree padding, finite-core surrogates or a near-zero-total-measure sequence.

<a id="infinite-core-all-late-obstruction"></a>
### 5. Complete late-time obstruction and the precise mean dichotomy

By L285, the base beta is critically recurrent.
By L289 its extended complete critical mean satisfies

    mu_beta=R F_beta'(R)>3/2,                         (15)

with infinity permitted.
L293 supplies limsup_l D_l(beta)>=mu_beta.
Applying the EXACT even-r identity(9), for every dyadic r>=2,

    limsup_(n->infinity)D_n(gamma_r)
       =C_beta(infinity)^r
       >=mu_beta^r>(3/2)^r.                          (16)

This is an all-late-time assertion: for every onset N0 and each fixed r, arbitrarily late original midpoint overlaps exceed (3/2)^r.
It is not inferred from a finite peak, does not require recurrence of the lifted input, and does not require deciding whether the base mean is finite.
The extended-power interpretation includes C_beta(infinity)=infinity or mu_beta=infinity.
In particular any proposed eventual bound D_n(gamma_r)<=C_r for all n>=N_r, with arbitrary input-dependent onsets N_r, must satisfy

    C_r>=C_beta(infinity)^r>exp[(log(3/2)/4)degree(gamma_r)]. (17)

No family of such complete upper certificates with log C_r=o(r), in particular no polynomial-in-degree bound at this fixed total measure, can hold.
The unknown common R has canceled from all overlaps.
The result remains valid for the actual infinite cores and neutral dimensions in(14); this is the changed control beyond the earlier finite golden-core example.

The critical MEAN conclusion needs its own branch distinction.
If mu_beta is infinite, the base is critically null recurrent, so a finite complete-mean upper theorem covering this base already fails.
The higher radicals cannot acquire finite-mean critical attainment, by L206; they may be null recurrent or transient, as determined by its full sum sum_l (R^l p_l(beta))^r.
They are not all called recurrent.
If mu_beta is finite, L206 instead gives positive critical recurrence at EVERY gamma_r and

    mu_(gamma_r)=mu_beta^r,
    pi_(gamma_r)(0)=mu_beta^(-r).                     (18)

Their complete bounded dual convolution norms equal the same means by L240.
Therefore, independently of which unresolved base branch is true, there cannot be a finite upper-mean theorem with subexponential degree expense on ALL critically recurrent members of this actual quartic-radical class, including r=1.
In the finite branch it fails exponentially along r; in the infinite branch it fails at the base itself.
This is a logically exhaustive obstruction, not an asserted classification of that base or an assertion of an actually exhibited infinite-core positive recurrent example.

The fixed m_0 is essential.
Equations(16)--(18) do NOT disprove an upper theorem restricted to very small total measure, or to Salem inputs, or to a restricted polynomial structure.
Nor do they refute a bound allowed to be exponential in degree.
They show exactly what a complete multi-expanding bound would have to pay and why an input-dependent late onset cannot repair an inadequate constant.
In particular they do not turn L297's necessary mean lower bound into a positive Mahler gap.

<a id="canonical-composition-mean-normalization"></a>
### 6. Remove the composition expense before seeking an upper theorem

For a general monic irreducible unit polynomial P(t)=sum_(j=0)^D a_j t^j, define

    r(P)=gcd{j>=1:a_j!=0},
    P(t)=Q(t^r), r=r(P), d=degree Q=D/r.              (19)

The coefficient construction makes Q integral and monic, with the same constant+/-1.
It is irreducible: a nontrivial rational factorization of Q would compose to one of P.
Its nonzero exponent gcd is one.
We call this latter property composition-primitive here, solely as a short name for the displayed coefficient condition; it is not multiplicative primitivity of an algebraic unit or a statement about its maximal order.

If alpha is any actual root of P and beta=alpha^r, the irreducible Q is the actual minimal polynomial of beta.
Hence [Q(alpha):Q(beta)]=r exactly, and the entire L206 interface applies with these actual orders.
The elementary root-fiber product gives M(P)=M(Q): over each root lambda of Q, the r lifts each contribute max{1,|lambda|^(1/r)}.
Moreover alpha is a root of unity iff beta is.
Thus

    m(alpha)=m(beta), h_2(alpha)=h_2(beta),
    D_actual(alpha)=D_actual(beta)^r,
    critical attainment at alpha iff at beta,
    and, when attained, mu_alpha=mu_beta^r.           (20)

The complete balanced overlap invariant from(8),(10) gives additionally

    C_alpha(infinity)=C_beta(infinity)^r,
    sup_(N>=2rL)B_N(alpha)=C_beta(L)^r, L>=1.         (21)

This is an exact renormalization of a full late-time certificate, with r and the chronological cutoff paid; taking an rth root changes the object being bounded and cannot be done silently for the original mean or convolution norm.
Critical recurrence does not have a two-way equivalence in(20).
Its exact test is the L206 sum S_r=sum_l (R^l p_l(beta))^r.
Recurrence of alpha implies recurrence of beta, because 0<a_l<=1 and sum a_l^r=infinity implies sum a_l=infinity.
The reverse implication may fail.
Positive recurrence/attainment, unlike recurrence alone, does have the stated equivalence.
A Salem polynomial already has r(P)=1: otherwise the r distinct lifts of any expanding root of Q would supply at least r expanding conjugates of P.
Thus this normalization does not make the original Salem-only question disappear.

This gives a precise refinement of the next upper-mean proposal.
A uniform Mahler gap for composition-primitive unit polynomials would imply the same unit gap without that restriction, since m is unchanged in(20).
It is therefore legitimate to seek a complete upper mechanism only on those normalized inputs, rather than impose an unnecessarily false degree expense on the family(12).
However any accompanying recurrence hypothesis must be proved for those normalized inputs or handled by a separate transient argument; (20) does not provide that missing coverage.

For example, a hypothetical theorem on ALL composition-primitive nontorsion units with0<m<=epsilon saying F(R)=1 and mu<=A d/m, with a fixed finite A, would contradict L297 whenever also m<=2^(-16) and log(1/m)>24A.
It would then give a unit gap, extended by(19)--(20).
This is only a CONDITIONAL consequence identifying the exact missing theorem, not a proved upper estimate or coverage claim.
If its assertion were merely conditional on recurrence, then only that recurrent subclass would be excluded; transient normalized inputs would remain.
The actual d in this comparison is degree Q, and L297's accepted house/entropy degree gate would apply to that actual polynomial, not to a padded degree D.

<a id="complete-overlap-scope-and-self-check"></a>
### 7. Scope, remaining mechanism and self-check

The substantive changed interface is the two-parity exact full-tail identity(7)--(10), followed by its genuine reciprocal infinite-core control(11)--(18) and its precisely scoped canonical use(19)--(21).
No unknown radius, all-late word family, original probability, field multiplicity or time onset has been dropped.
The fixed quartic's recurrence is known, its mean still unclassified, and the branch distinction is essential.
The proof supplies neither an all-late upper bound for the base nor a near-one upper estimate.
It isolates a real obstruction to a broad proposed certificate and a mathematically justified normalization before trying the harder primitive-input question.

The earlier possible finite-box/escaped-excursion approach was not developed into a theorem: a finite state calculation alone has no certified complete critical exit/return tail in the present premises.
Essential spectrum equality, reciprocal reflection, positive recurrence on a finite restriction and finite original p_n values likewise do not supply that missing tail.
These observations motivated the exact composition test; they are not impossibility theorems for those broader methods.
A next useful upper mechanism must act on the entire primitive actual core, including all sufficiently late excursions, with the actual original weights and a justified recurrence or transient alternative.


## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:01 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C555 complete overlap theorem](Yin_C_G0555_v1.md#statement) | Original midpoint/dyadic identities and correctly directed all-late boundedness/limsup consequences, with no renewal converse. |
| dependency | [C493 actual radical product](Yin_C_G0493_v1.md#statement) | Full relative-degree actual order/core product, chronological probabilities, exact power-sum recurrence and two-way finite-mean attainment. |
| dependency | [C396 actual infinite quartic core](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Fixed actual quartic degree/conjugates and infinite zero-to-zero core. |
| dependency | [C526 actual quartic recurrence](Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation) | True-radius q=2 critical recurrence, with no finite-mean conclusion. |
| dependency | [C546 strict quartic mean cost](Yin_C_G0546_v1.md#statement) | Complete original critical mean greater than3/2, permitting infinity. |
| dependency | [C557 tiny-measure conditional mean cost](Yin_C_G0557_v1.md#statement) | Exact hypothetical normalized-input upper-bound comparison only at the actual degree and0<m<=2^-16, without supplying recurrence. |
| dependency | [Original whole dual convolution criterion](../ledger/Yin_L_G0240_v1.md#critical-convolution-bounded-density-test) | Exact norm RFprime+1-F, specialized only on the recurrent finite-mean branch. |
| support | [Original complete proof input](../ledger/Yin_L_G0301_v1.md#complete-overlap-reuse) | Original full Sections1--7/equations1--21, all parity/degree/branch/normalization/source/no-program limits, real 2026-10-10T06:28 freeze and R200 input. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:14 |
| status | proved |
| reason | Adopt the complete retained theorem at its exact hypotheses, full costs and negative limits after actual whole current SELF of the published Statement and entire Argument; no independent arrangement or research resumption is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C555 complete overlap theorem](Yin_C_G0555_v1.md#statement) | Original midpoint/dyadic identities and correctly directed all-late boundedness/limsup consequences, with no renewal converse. |
| dependency | [C493 actual radical product](Yin_C_G0493_v1.md#statement) | Full relative-degree actual order/core product, chronological probabilities, exact power-sum recurrence and two-way finite-mean attainment. |
| dependency | [C396 actual infinite quartic core](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Fixed actual quartic degree/conjugates and infinite zero-to-zero core. |
| dependency | [C526 actual quartic recurrence](Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation) | True-radius q=2 critical recurrence, with no finite-mean conclusion. |
| dependency | [C546 strict quartic mean cost](Yin_C_G0546_v1.md#statement) | Complete original critical mean greater than3/2, permitting infinity. |
| dependency | [C557 tiny-measure conditional mean cost](Yin_C_G0557_v1.md#statement) | Exact hypothetical normalized-input upper-bound comparison only at the actual degree and0<m<=2^-16, without supplying recurrence. |
| dependency | [Original whole dual convolution criterion](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Exact norm RFprime+1-F, specialized only on the recurrent finite-mean branch. |
| support | [Original complete proof input](../ledger/Yin_L_G0301_v1.md#complete-overlap-reuse) | Original full Sections1--7/equations1--21, all parity/degree/branch/normalization/source/no-program limits, real 2026-10-10T06:28 freeze and R200 input. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0745_v1.md#balanced-tail-radical-whole-self) | The complete current Statement and entire Argument, every selected dependency interface and all original failed-scope/source/native limits. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:00 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire Argument after the actual isolated whole review completed2026-10-22T20:49 UTC, with all original domains, costs, failed/negative scopes, source depth and finite-evidence limits retained. The dated original reviews and current SELF findings keep their actual inputs and relationships; this decision neither backfills old review acts nor resumes research. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C555 complete overlap theorem](Yin_C_G0555_v1.md#statement) | Original midpoint/dyadic identities and correctly directed all-late boundedness/limsup consequences, with no renewal converse. |
| dependency | [C493 actual radical product](Yin_C_G0493_v1.md#statement) | Full relative-degree actual order/core product, chronological probabilities, exact power-sum recurrence and two-way finite-mean attainment. |
| dependency | [C396 actual infinite quartic core](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Fixed actual quartic degree/conjugates and infinite zero-to-zero core. |
| dependency | [C526 actual quartic recurrence](Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation) | True-radius q=2 critical recurrence, with no finite-mean conclusion. |
| dependency | [C546 strict quartic mean cost](Yin_C_G0546_v1.md#statement) | Complete original critical mean greater than3/2, permitting infinity. |
| dependency | [C557 tiny-measure conditional mean cost](Yin_C_G0557_v1.md#statement) | Exact hypothetical normalized-input upper-bound comparison only at the actual degree and0<m<=2^-16, without supplying recurrence. |
| dependency | [Original whole dual convolution criterion](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Exact norm RFprime+1-F, specialized only on the recurrent finite-mean branch. |
| support | [Original complete proof input](../ledger/Yin_L_G0301_v1.md#complete-overlap-reuse) | Original full Sections1--7/equations1--21, all parity/degree/branch/normalization/source/no-program limits, real 2026-10-10T06:28 freeze and R200 input. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0776_v1.md#current-balanced-radical-tail) | The complete current fixed Statement and entire Argument, all necessary mathematical interfaces and actual finite-evidence checks at2026-10-22T20:49 UTC; independently reviewed in the disclosed isolated arrangement, without native discovery/reviewer reruns. |

