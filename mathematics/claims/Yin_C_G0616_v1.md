---
author: Yin
---

# Endpoint rigidity of the maximal residual multiplicity

Human author Yin.
Root supplied the positive-endpoint valuation reduction and subsequently the negative-endpoint and reciprocal-congruence leads on 2026-10-23 UTC.
Paid_comparison checked and completed the prime valuations, all signed finite cases, exact multiplicity ceilings, original-order consequences and paid endpoint-budget consumer below.
Both are contributors and neither is an independent reviewer of this new mathematics.
This new endpoint-domain theorem uses the adopted [C614v1 maximal quotient](Yin_C_G0614_v1.md#statement); that physical version and its [R817 review](../audits/reviews/Yin_R_G0817_v1.md#maximal-quotient-whole-finding) remain unchanged.
All finite arithmetic below is part of the displayed integer proof.
No arithmetic program, parameter scan, new native computation, source acquisition or new original-source proof inspection was performed.

## Statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient 1 and degree d=2r>=2.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), assume the actual trace field Q(delta) is totally real, and let T be its monic minimal trace polynomial.
Use C_p(z+z^(-1))=z^p+z^(-p), theta_p=rem_T T(C_p)/p for p=2,3,5, and the actual values

    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

Assume f=e+s g=0, g!=0, s in {1,-1}.
Retain the SAME ordinary polynomials and maximal multiplicity of C614:

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    h=9d/2, Z=z^(5d)+1,
    F_s=3375s z^h H23+8H35-5Z H25,
    D_s=F_s/P, nu=ord_P F_s,
    Q_s=F_s/P^nu, Ntilde_s=H35 Q_s.              (1)

The fixed construction gives 1<=nu<=14 and a monic reciprocal integral Q_s that is nonzero at every original conjugate.
Put t=P(1), v=P(-1), which are nonzero integers, and epsilon=s(-1)^r.
All following restrictions are NECESSARY for actual inputs; they assert no realization of an endpoint or multiplicity.

**A. Nonunit positive endpoint.**
If |t|>1, then

    t!=8 implies nu<=3,
    t=8 and s=1 implies nu<=4,
    t=8 and s=-1 implies nu<=5.                  (2)

In particular nu>=4 with |t|>1 forces t=8, and nu>=6 forces |t|=1.
The proof includes the complete exact endpoint-divisibility ceiling on the twenty-eight exceptional signed integer values arising from the prime reduction, not a bounded parameter scan.
The condition |t|=1 supplies no positive-endpoint divisibility bound by itself.

**B. The second endpoint and the sole remaining nonunit nu=5 configuration.**
If |t|=1 and nu>=2, then v is one of 1,-1,5,-5.
If additionally |v|=5, then nu<=4.
Hence

    nu>=6 implies t and v both belong to {1,-1}. (3)

More sharply, if |t|>1 and nu=5, then necessarily

    s=-1, d divisible by 4, t=v=8.               (4)

The restriction (4) is a surviving necessary configuration, not an example or an existence claim.
If at least one of |t|,|v| exceeds 1, then nu<=5.
Outside configuration (4), that nonunit-endpoint domain has nu<=4, and the subdomain |t|>1 with t!=8 has nu<=3.

**C. Original-order income and a global endpoint budget.**
Let c_nu be C614's exact guaranteed factor:

    c_1=1000; c_2=c_3=500; c_4=250; c_5=50;
    c_6=...=c_9=25; c_10=...=c_14=5.

On the domain where at least one endpoint is nonunit, its nonzero original-order quotient satisfies

    abs Norm_(K/Q)Q_s(alpha)>=c_nu^d>=50^d.       (5)

Outside (4), the last floor improves to 250^d; on |t|>1,t!=8 it improves to 500^d.
On the two-unit-endpoint domain the unchanged universal 5^d floor remains; no higher multiplicity is excluded there by this theorem.

For every fixed positive rational q<2^(6/11), define the ACTUAL C614 normalization

    k0=30375, u_s=Ntilde_s/(k0 c_nu q).

On the ENTIRE original domain, including the unit-endpoint branch, one now has

    ||u_s||_1>=700|P(1)|^5/(30375000q).           (6)

Thus an actual fixed budget ||u_s||_1<=S_0 implies

    |P(1)|<=[30375000q S_0/700]^(1/5).            (7)

This global fifth-power cost follows from the multiplicity restrictions; it does not assume an actual family with growing endpoints.

For a direct analytic consumer, restrict to at least one nonunit endpoint and fix eta>0, integers K_0>=2,S_0>=1 and a rational q with

    exp(tau/2-eta/2)<=q<exp(tau/2),
    tau=(12/11)log 2, J_G=2m(H35)-2log k0.

If the ACTUAL inputs satisfy

    J_G<=tau-2eta,
    m(D_s)<=log 50+eta/4,
    #supp(Ntilde_s)<=K_0,
    ||Ntilde_s||_1/(k0 c_nu q)<=S_0,             (8)

then the complete C614/C196 norm-only application yields

    m(P)>h_star(K_0,S_0,min{eta/4,1})/29>0.        (9)

The scalar in (8) is still the actual c_nu; its full norm, rational q denominator, degree (30-nu)d and expanded coefficients are retained.
Only the common permitted Mahler ceiling increases from log 5 to log 50 on this restricted domain.
No Mahler ceiling, support bound or coefficient bound in (8) is supplied automatically, and no uniform unrestricted gap is claimed.

## Reuse and scope of the new theorem

The author read the complete fixed C611 endpoint calculation, C614's current statement/proof and adoption, and the common content-retention rules before this continuation.
Targeted local searches for the endpoint constants, exact valuation reductions and maximal-multiplicity endpoint restriction found the original C611 formulas but no theorem at the present scope.
[C611v1](Yin_C_G0611_v1.md#complete-argument) supplies the full all-sign endpoint formula and its nonzero-integer evaluation bound.
[C614v1](Yin_C_G0614_v1.md#complete-argument) supplies the actual maximal quotient, automatic nonvanishing, exact c_nu table, norm, Mahler and degree data, and its complete paid analytic application.
No earlier review is extended to the new valuation theorem.
A new family is appropriate for this endpoint-domain restriction and its new coefficient consequence; the fixed construction and its earlier high-multiplicity qualifications remain historical statements at their exact scopes.

## Complete argument

### 1. Exact positive-endpoint divisibility and its prime constants

C611's actual evaluation is

    D_s(1)=t B_s(t),
    B_s(t)=1250t^3+A_s t+C_s,
    A_s=30375s-1944, C_s=640-27000s.

Since F_s=P D_s, the actual integer identity is

    F_s(1)=t^2 B_s(t).                            (10)

The all-sign bound |D_s(1)|>=100|t|^4 in C611 implies B_s(t)!=0 for every nonzero integer t.
The divisibility P^nu|F_s gives t^nu|F_s(1).
For every prime ell dividing t, with a_ell=v_ell(t)>=1, it follows that

    (nu-2)a_ell<=v_ell(B_s(t)).                   (11)

Here valuations are taken on the absolute nonzero integers; negative t and negative B_s(t) are included.
The constants are

    A_+=28431, C_+=-26360=-2^3*5*659,
    A_-=-32319, C_-=27640=2^3*5*691.              (12)

Write p_+=659 and p_-=691.
Both are prime: their square roots are less than 27, and their remainders at every prime below 27 are displayed here.

| Trial prime | 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 659 remainder | 1 | 2 | 4 | 1 | 10 | 9 | 13 | 13 | 15 |
| 691 remainder | 1 | 1 | 1 | 5 | 9 | 2 | 11 | 7 | 1 |

Each entry is nonzero; these are all possible prime divisors up to the respective square roots.
Moreover A_s is odd, A_s is congruent to 1 modulo 5, A_+ is congruent to 94 modulo 659, and A_- is congruent to 158 modulo 691.
Thus A_s is a unit at each prime dividing C_s.

If ell|t and ell does not divide C_s, then B_s(t) is congruent to C_s modulo ell and its valuation is zero.
Equation (11) then gives nu<=2.
If ell is 5 or p_s and v_ell(t)>=2, the constant term C_s has valuation exactly 1, the linear term has valuation at least 2, and the cubic term has valuation at least 6.
The constant is the unique least-valuation term, so v_ell(B_s(t))=1 and again nu<=2.

For ell=2 let a=v_2(t)>=1.
The cubic, linear and constant terms of B_s(t) have respective valuations

    1+3a, a, 3.

For a=1 or 2 the linear term is uniquely minimal, so v_2(B_s(t))=a and nu<=3.
For a>=4 the constant is uniquely minimal, so v_2(B_s(t))=3<a and nu<=2.
Only a=3 permits nu>=4 among even t.

Consequently, if nu>=4 and |t|>1, then

    t=sign*2^a 5^b p_s^c,
    a in {0,3}, b,c in {0,1},
    t!=1,-1.                                    (13)

There are exactly fourteen signed values for each fixed s, hence twenty-eight total signed inputs.
They are exhausted by the seven positive magnitudes and their negatives in the table below.
This reduction is over all nonzero integers; no endpoint range was guessed.

### 2. Exact ceilings on all twenty-eight reduced inputs

For each reduced nonunit t define the exact endpoint-divisibility ceiling

    E_s(t)=2+min_(ell|t) floor(v_ell(B_s(t))/v_ell(t)). (14)

Then t^n divides F_s(1) exactly for nonnegative integers n<=E_s(t), and every actual nu satisfies nu<=E_s(t).
All t in (13) divide C_s and therefore divide B_s(t).
It follows at once that E_s(t)>=3 on every reduced input.
We now prove the matching exact ceilings, including the only two larger ones.

If p_s divides t in (13), write t=p_s w with

    w in {1,-1,5,-5,8,-8,40,-40}.

Reduction of B_s(t)/p_s modulo p_s gives

    B_+(t)/659 congruent to 94w-40 modulo 659,
    B_-(t)/691 congruent to 158w+40 modulo 691.

For the first expression, 7*94=658 is congruent to -1 modulo 659, so a zero would require w congruent to -280 modulo 659.
No displayed w satisfies that condition, since |w|<=40.
For the second expression the unique root is w congruent to -9 modulo 691, because 158*(-9)+40=-2*691 and 158 is a unit.
Again none of the eight displayed w is such a root.
Thus v_(p_s)(B_s(t))=1 and E_s(t)=3 on all sixteen reduced inputs containing p_s.

The remaining six inputs for each sign are t in {5,-5,8,-8,40,-40}.
At t=5w with w in {1,-1,8,-8}, reduction gives

    B_s(t)/5 congruent to w+3 modulo 5.

For w=1,-1,8 this is nonzero, yielding valuation 1 and E_s(t)=3 at t=5,-5,40 for both signs.
Only w=-8, that is t=-40, requires another prime.

For t=8w with w odd, divide by 8:

    B_s(8w)/8=80000w^3+A_s w+C_s/8.

Modulo 4 the expression is 3w+1 for s=1 and w+3 for s=-1.
At t=-8 or -40 one has w=-1 or -5, both congruent to 3 modulo 4.
Both expressions are then congruent to 2 modulo 4.
Hence v_2(B_s(t))=4, while v_2(t)=3, and E_s(t)=3 at these four signed inputs.

Finally the two exact positive t=8 values are

    B_+(8)=841088=2^7*6571,
    B_-(8)=409088=2^9*799.

Both final factors are odd.
Since 2 is the only prime dividing 8, equation (14) gives E_+(8)=4 and E_-(8)=5.
The entire twenty-eight-input table is therefore

| Positive magnitude for s=1 | Positive magnitude for s=-1 | E_+(positive) | E_+(negative) | E_-(positive) | E_-(negative) |
| --- | --- | --- | --- | --- | --- |
| 5 | 5 | 3 | 3 | 3 | 3 |
| 8 | 8 | 4 | 3 | 5 | 3 |
| 40 | 40 | 3 | 3 | 3 | 3 |
| 659 | 691 | 3 | 3 | 3 | 3 |
| 3295 | 3455 | 3 | 3 | 3 | 3 |
| 5272 | 5528 | 3 | 3 | 3 | 3 |
| 26360 | 27640 | 3 | 3 | 3 | 3 |

The modular arguments and exact factorizations above prove every entry, including the lower bound 3 needed for exactness.
An endpoint ceiling is not a realized polynomial multiplicity.
Outside this table any nu>=4 with |t|>1 was already excluded by (11)--(13).
This proves all of (2).
When t=1 or -1, t^nu|F_s(1) is automatic for every nu and provides no further restriction.

### 3. Exact negative-endpoint formula on the unit positive-endpoint branch

Since d is even, P((-1)^2)=t, P((-1)^3)=P((-1)^5)=v and Z(-1)=2.
Also (-1)^h=(-1)^(9r)=(-1)^r, giving epsilon=s(-1)^r.
Substituting into the full expanded numerator yields exactly

    F_s(-1)=375t^3(81epsilon-2t^2)
              +(640-27000epsilon)v^2-1944v^3+2000v^5. (15)

The divisibility P^nu|F_s gives v^nu|F_s(-1).
When nu>=2, all nonconstant-in-v terms of (15) are divisible by v^2, hence

    v^2 divides 375t^3(81epsilon-2t^2).           (16)

First suppose t=1 or -1.
Then the right side is 375t(81epsilon-2), with odd factor 79 for epsilon=1 and -83 for epsilon=-1.
The integers 79 and 83 are prime: their remainders modulo 2,3,5,7 are respectively (1,1,4,2) and (1,2,3,6), and their square roots are less than 10.
Since 375=3*5^3, square divisibility in (16) leaves only v=1,-1,5,-5.

For v=5w with w in {1,-1}, the exact quotient of (15) by 125 is

    F_s(-1)/125=3t(81epsilon-2)+128-5400epsilon+48056w. (17)

Here w^2=1 and w^3=w^5=w; all scalars are retained.
Its eight values and resulting valuations are

| epsilon | t | w | F_s(-1)/125 | v_5(F_s(-1)) |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 43021 | 3 |
| 1 | 1 | -1 | -53091 | 3 |
| 1 | -1 | 1 | 42547 | 3 |
| 1 | -1 | -1 | -53565=-5*10713 | 4 |
| -1 | 1 | 1 | 53335=5*10667 | 4 |
| -1 | 1 | -1 | -42777 | 3 |
| -1 | -1 | 1 | 53833 | 3 |
| -1 | -1 | -1 | -42279 | 3 |

The six unmarked values are units modulo 5, and 10713 and 10667 are also units modulo 5.
Thus the valuations are exact and never exceed 4.
Since v_5(v)=1, v^nu|F_s(-1) gives nu<=4 whenever |v|=5.
Combining this with (2), any nu>=6 forces first |t|=1 and then |v|=1, proving (3).
It also proves that |t|=1,|v|>1 implies nu<=4, even if nu=1 and the square-divisibility step is not needed.

### 4. Reciprocal restriction and the remaining t=8, s=-1 configuration

By (2), nonunit t and nu=5 already force t=8 and s=-1.
Write P(z)=sum_(j=0)^(2r) p_j z^j, with p_j=p_(2r-j).
Pairing the coefficients gives

    P(-1)-(-1)^r P(1)
      =2 sum_(j=0)^(r-1) [(-1)^j-(-1)^r]p_j,

which is divisible by 4.
Thus t=8 implies 4|v, without any additional trace-polynomial assumption.

In this case (16) becomes

    v^2 divides 375*512*(81epsilon-128).

The last factor is -47 for epsilon=1 and -209=-11*19 for epsilon=-1.
The numbers 11 and 19 have no prime divisor at most their square roots among 2,3, and 47 has none among 2,3,5; they are prime.
These primes are distinct from 2,3,5, and all occur with exponent 1.
Consequently square divisibility and 4|v imply exactly the candidate form

    v=sign*2^a 5^b, a in {2,3,4}, b in {0,1}.    (18)

This is twelve signed values for each epsilon, all derived from (16).
For v_2(v)=a, the four terms in (15) have respective 2-adic valuations

    9, 3+2a, 3+3a, 4+5a.

The coefficient 640-27000epsilon has valuation 3, since it is 8 times the odd integer 80-3375epsilon.
For a=2 its v^2 term is uniquely minimal at valuation 7, so 2nu<=7 and nu<=3.
For a=4 the constant is uniquely minimal at valuation 9, so 4nu<=9 and nu<=2.
Thus nu=5 requires a=3, leaving v=8w with w in {1,-1,5,-5}.

Substitution into (15), still with t=8, gives

    F_s(-1)/512
      =epsilon(30375-3375w^2)-48000+80w^2
                                         -1944w^3+128000w^5. (19)

The eight remaining exact values are

| epsilon | w | F_s(-1)/512 | Decisive valuation and resulting ceiling |
| --- | --- | --- | --- |
| 1 | 1 | 105136=2^4*6571 | v_2(F_s(-1))=13, so nu<=4 |
| -1 | 1 | 51136=2^6*799 | v_2(F_s(-1))=15, so nu<=5 |
| 1 | -1 | -146976=-2^5*4593 | v_2(F_s(-1))=14, so nu<=4 |
| -1 | -1 | -200976=-2^4*12561 | v_2(F_s(-1))=13, so nu<=4 |
| 1 | 5 | 399657000=5^3*3197256 | v_5(F_s(-1))=3, so nu<=3 |
| -1 | 5 | 399765000=5^4*639624 | v_5(F_s(-1))=4, so nu<=4 |
| 1 | -5 | -399857000=-5^3*3198856 | v_5(F_s(-1))=3, so nu<=3 |
| -1 | -5 | -399749000=-5^3*3197992 | v_5(F_s(-1))=3, so nu<=3 |

Every remaining factor in the four dyadic rows is odd, and every remaining factor in the four 5-adic rows is a unit modulo 5.
For the dyadic rows v_2(v)=3; for the other rows v_5(v)=1 and 512 is a 5-adic unit.
Thus every stated ceiling follows exactly from v^nu|F_s(-1).
Only epsilon=-1,w=1 permits nu=5 among these necessary tests.
This forces v=8, and since epsilon=s(-1)^r with s=-1, it also forces r even, equivalently 4|d.
Equation (4) is proved, with no claim that its surviving divisibility configuration is realized.

### 5. Original-order consequences and the fully paid consumer

If either endpoint is nonunit, (2)--(4) give nu<=5.
If configuration (4) fails, that domain has nu<=4: for nonunit t use (2) and Section 4, while for unit t and nonunit v use Section 3.
For nonunit t!=8, (2) gives the stronger nu<=3.
The c_nu table in the fixed C614 theorem then gives c_nu>=50, 250 or 500, respectively.
C614 already proves Q_s(alpha)/c_nu is a nonzero element of Z[alpha], hence its full norm is a nonzero integer.
This proves (5) and its stated refinements with all d original embeddings.
No coefficientwise integral division of the monic Q_s by c_nu is asserted.

C614's exact endpoint bound for the ACTUAL u_s is

    ||u_s||_1>=700|t|^(10-nu)/(k0 c_nu q).        (20)

When |t|>1, (2) gives nu<=5 and hence |t|^(10-nu)>=|t|^5.
When |t|=1, both powers equal 1 for every possible nu.
In both cases c_nu<=1000, so (20) proves the global bound (6).
Combining it with ||u_s||_1<=S_0 proves (7).
This conclusion uses the actual quotient numerator from C614; it does not inherit a coefficient bound from the old N_s by polynomial division.

On the nonunit-endpoint domain, m(Q_s)<=m(D_s) and c_nu>=50 give from (8)

    m(Q_s)-log c_nu<=m(D_s)-log 50<=eta/4.

The same exact scalar identity as in C614 gives

    m(u_s)=J_G/2+m(Q_s)-log c_nu-log q<=-eta/4.

The already proved full norm is at least (2^(6/11)/q)^d>1 and the actual degree is (30-nu)d<=29d.
The two other hypotheses in (8) provide the ACTUAL support and normalized coefficient budgets.
Thus the complete C614 application of C196v5 NF1--NF8 gives (9), with eta_0=min{eta/4,1} and no new analytic or source claim.
All q^d denominators, scalar Mahler shifts and finite frequency/radial/source constants remain at their fixed scopes.
The proof does not supply the Mahler or sparse budgets, and the two-unit-endpoint branch remains subject to the earlier maximal-quotient problem.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision endpoint-rigidity-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T17:09 |
| status | open |
| reason | Register the complete endpoint-domain theorem: global prime reduction and exact twenty-eight positive-endpoint ceilings, both negative-endpoint signed cases, reciprocal refinement of the sole nonunit nu=5 configuration, original-order income and global coefficient cost, with all analytic budgets still explicit. Root and paid_comparison are contributors. Fresh whole review and adoption are required; no endpoint or original-input realization is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire endpoint-rigidity statement](#statement) | Complete original domain and Parts A--C, nonunit multiplicity classification, unit endpoint boundary, refined nu=5 configuration, norm floors, global fifth-power cost and paid restricted-domain consumer. |
| argument | [Complete proof](#complete-argument) | All valuations, prime checks, twenty-eight exact positive-endpoint ceilings, exact negative-endpoint signs and phases, reciprocal congruence, twelve-value reductions, finite tables and all unchanged construction/analytic interfaces. |
| dependency | [Fixed all-sign endpoint formula](Yin_C_G0611_v1.md#complete-argument) | Exact F_s(1)=t^2 B_s(t), nonzero B_s(t) for nonzero integer t and actual F_s polynomial construction; no endpoint realization imported. |
| dependency | [Complete maximal quotient and paid transfer](Yin_C_G0614_v1.md#complete-argument) | Same actual nu, Q_s and Ntilde_s, automatic original nonvanishing, c_nu table, full norm/Mahler/degree/scalar identities, original endpoint exponent and entire C196 NF1--NF8 consumer with every source and analytic expense. |
| support | [Unchanged maximal-quotient review](../audits/reviews/Yin_R_G0817_v1.md#maximal-quotient-whole-finding) | Whole independent evidence for physical C614v1 only, not review or adoption of this endpoint restriction and its consequences. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T17:24 |
| status | proved |
| reason | Adopt the entire endpoint rigidity theorem after reading its complete fixed proof and fresh whole R819 finding. All signed integer endpoints, globally exhaustive valuation reductions, reciprocal phase and exceptional necessary configuration, actual original-order norm floors and global coefficient cost are retained. The conditional analytic consumer keeps every unsupplied budget; no remaining configuration is asserted to exist and no unrestricted gap is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire endpoint-rigidity statement](#statement) | Complete original domain and Parts A--C, nonunit multiplicity classification, unit endpoint boundary, refined nu=5 configuration, norm floors, global fifth-power cost and paid restricted-domain consumer. |
| argument | [Complete proof](#complete-argument) | All valuations, prime checks, twenty-eight exact positive-endpoint ceilings, exact negative-endpoint signs and phases, reciprocal congruence, twelve-value reductions, finite tables and all unchanged construction/analytic interfaces. |
| dependency | [Fixed all-sign endpoint formula](Yin_C_G0611_v1.md#complete-argument) | Exact F_s(1)=t^2 B_s(t), nonzero B_s(t) for nonzero integer t and actual F_s polynomial construction; no endpoint realization imported. |
| dependency | [Complete maximal quotient and paid transfer](Yin_C_G0614_v1.md#complete-argument) | Same actual nu, Q_s and Ntilde_s, automatic original nonvanishing, c_nu table, full norm/Mahler/degree/scalar identities, original endpoint exponent and entire C196 NF1--NF8 consumer with every source and analytic expense. |
| support | [Unchanged maximal-quotient review](../audits/reviews/Yin_R_G0817_v1.md#maximal-quotient-whole-finding) | Whole independent evidence for physical C614v1 only, not review or adoption of this endpoint restriction and its consequences. |
| review | [Independent whole endpoint-rigidity finding](../audits/reviews/Yin_R_G0819_v1.md#endpoint-rigidity-whole-finding) | Complete A--C and all five proof sections, every finite endpoint and prime calculation, all selected and actually used predecessor/source interfaces and the full conditional NF application, with historical relationships preserved. |

