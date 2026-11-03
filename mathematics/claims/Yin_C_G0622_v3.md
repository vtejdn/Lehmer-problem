---
author: Yin
---

# Five-adic endpoint exclusion and the nonunit residual quotient

Human author Yin.
This physical v3 retains the complete Parts A--F and their arguments from adopted [v2](Yin_C_G0622_v2.md#decision-whole-reviewed-2026-10-23), and adds Part G with its complete Section 9.
Root authored the rational trace-cluster extension and the new exact divided-polynomial jets; earlier fixed versions and their actual reviews remain unchanged.
An assessment or review of v2 alone does not adopt Part G.
Root supplied the original five-adic endpoint arguments, quotient consequences and coefficient-one consumer.
Paid_comparison checked their complete original-field hypotheses, all root factors, finite valuations, residue-field reconstruction and scalar/degree costs, and made explicit the f-only scope of the negative-endpoint valuation before fixed registration.
The same author check also corrected the candidate's cost boundary: on this fixed-denominator family an actual coefficient-one bound supplies both finite support and a strict negative Mahler margin, as proved in Part E.
Both are contributors; neither is an independent reviewer of this mathematics.
The complete candidate is retained here for separate whole review.
The physical C153, C614, C616 and C619 inputs and their existing reviews remain unchanged.
No native computation, parameter scan, new external-source acquisition or new original-source proof inspection was performed.

## Statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient 1 and degree d=2r>=2.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), F=Q(delta), and assume the actual trace field F is totally real.
Let T in Z[X] be its monic minimal polynomial.
The actual trace interface gives [F:Q]=r, [K:F]=2 and

    P(z)=z^r T(z+z^(-1)).

Use the actual polynomials and trace quotient values

    C2(X)=X^2-2, C3(X)=X^3-3X,
    C5(X)=X^5-5X^3+5X,
    a=T(C2(delta))/2, b=T(C3(delta))/3,
    c=T(C5(delta))/5,
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.          (1)

The values a,b,c are nonzero algebraic integers; the residual defects may vanish as specified below.
These are the same original values as the divided remainders modulo T, not arbitrary integral triples.
All rational-prime valuations v_l use v_l(l)=1; v_p at a number-field prime has integer value group.

**A. The five-adic endpoint restrictions under f=0.**
Assume f=0 only.
Then

    5 does not divide T(2),
    5 does not divide T(-1).                      (2)

Here T(2)=P(1), while T(-1) is the trace value at a primitive third root of unity.
It is not P(-1)=(-1)^r T(-2).
All three displayed trace endpoint values are nonzero under nontorsion irreducibility.

Still under f=0 alone, if 5 divides P(-1), then

    v_5(P(-1))=v_5(T(-2))=1.                     (3)

There is exactly one prime p of the actual field F above 5 at which delta reduces to -2.
At that prime

    [O_F/p:F_5]=1, v_p(delta+2)=1.                (4)

Other primes above 5 may exist; no ramification bound or maximal-power-order hypothesis is imposed.

**B. A full-residual congruence at the negative polynomial endpoint.**
Add e+s g=0 and g!=0 for s in {1,-1}.
If 5 divides P(-1), then, at the prime in (4), the actual residues satisfy

    bbar=0, abar=-1, cbar=-s in F_5,
    P(1) congruent to 3 modulo 5.                (5)

No existence of an original input satisfying these necessary conditions is asserted.

**C. Consequences for the actual maximal quotient.**
On the full residual domain retain the SAME polynomials and multiplicity from C614:

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    F_s=3375s z^(9d/2)H23+8H35-5(z^(5d)+1)H25,
    D_s=F_s/P, nu=ord_P F_s,
    Q_s=F_s/P^nu, Ntilde_s=H35 Q_s.              (6)

The fixed construction has 1<=nu<=14, P does not divide Q_s, and Q_s is monic reciprocal integral with constant coefficient 1 and degree (15-nu)d.
Then

    |P(1)|=1 and |P(-1)|>1 imply nu=1,
    max{|P(1)|,|P(-1)|}>1 implies nu<=3,
    nu>=4 implies P(1),P(-1) both belong to {1,-1}. (7)

With the exact C614 factor

    c_nu=2^max{0,3-floor(nu/2)} 5^(3-floor(nu/5)),

one has c_nu>=500 on every nonunit-endpoint input, and c_nu=1000 on the positive-unit/negative-nonunit subdomain in the first line of (7).
The original nonzero value satisfies

    Q_s(alpha)/c_nu in Z[alpha],
    |Norm_(K/Q)Q_s(alpha)|>=c_nu^d.              (8)

Thus the respective full norm floors are 500^d and 1000^d.
These are original-value divisibilities; Q_s/c_nu is not an integer polynomial, since its leading and constant coefficients are 1/c_nu.
No higher multiplicity is excluded on the two-unit-endpoint branch by this result.

For exact cost conventions, fix any positive rational q<2^(6/11) independently of P and put

    k0=30375, u_s=Ntilde_s/(k0 c_nu q),
    J_G=2m(H35)-2log k0.

The SAME ordinary rational polynomial retains

    deg u_s=(30-nu)d<=29d,
    #supp(u_s)=#supp(Ntilde_s),
    ||u_s||_1=||Ntilde_s||_1/(k0 c_nu q),
    m(u_s)=J_G/2+m(Q_s)-log c_nu-log q,
    |Norm_K u_s(alpha)|>=(2^(6/11)/q)^d>1.        (9)

All m are total logarithmic Mahler measures, and ||.||_1 is the sum of the absolute values of all actual expanded ordinary coefficients.
On the nonunit-endpoint domain the exact degree lies between 27d and 29d, and on the first subdomain in (7) it is 29d.
The endpoint conclusions do not supply a useful Mahler ceiling, uniformly bounded support or a normalized coefficient bound in (9).

**D. Necessary restrictions for the actual coefficient-one class.**
On the full residual domain, with exactly the u_s and fixed q in (9), suppose

    ||u_s||_1<=1.

Then

    P(1) in {1,-1,3,-3}.                         (10)

If P(1)=3 or -3, the actual trace field has degree r>=9, hence the original degree d>=18.
If X divides the reduction of T modulo 2, then this coefficient-one class is impossible.
This last statement uses only the explicit X factor and imports no zero-Haar or unsaturated-class characterization.
These are necessary restrictions, not constructions of any class member or exclusions for larger coefficient budgets.

**E. Complete paid transfer on the actual coefficient-one class.**
For the same fixed q put B_q=30375000q.
If B_q<14, the coefficient-one class is empty.
If B_q>=14, put

    epsilon_q=7/B_q, K_q=ceil(B_q),
    eta_q=-(1/2)log(1-epsilon_q)>0.

Every actual coefficient-one input then satisfies

    #supp(u_s)<=K_q,
    m(u_s)<=-eta_q,
    m(P)>h_star(K_q,1,min{eta_q,1})/29>0.        (19)

Here h_star is the exact finite positive constant of C196v5 NF1--NF8, without numerical inversion or a claimed practical size.
The support follows from the integer numerator and the fixed scalar cap, and the strict Mahler margin uses both actual endpoint coefficients.
More generally a fixed actual budget ||u_s||_1<=S gives #supp(u_s)<=B_q S; a negative margin for arbitrary S>1 is not asserted.
Thus coefficient-one is sufficient for this complete conditional gap theorem; no proof that arbitrary original inputs satisfy coefficient-one is given.

**F. The remaining rational five-adic trace clusters.**
Under f=0 alone, if 5 divides T(1), then v_5(T(1))=1.
There is exactly one actual prime p of F above5 with delta congruent1, and there its residue degree and v_p(delta-1) both equal1.

Under the full residual equations of Part B, if 5 divides T(0), then

    v_5(T(0))=1, 5 does not divide T(-2),
    T(-2) congruent3 modulo5.                   (20)

Exactly one actual prime p of F above5 satisfies delta congruent0; its residue degree and v_p(delta) both equal1.
At that prime bbar=0, abar=-1 and cbar=-s.
Consequently 5 cannot divide both T(0) and T(-2).

Under the same full residual equations, if 5 divides both T(1) and T(-2), then

    T(-1) congruent3 modulo5,
    T(2) congruent3 modulo5.                    (21)

These statements complete necessary restrictions for the five rational trace residue classes represented by -2,-1,0,1,2.
They do not assert simplicity of reduced polynomial roots: the actual ramification index at the unique matching prime may exceed1.
No existence of a surviving original input, higher residue-degree classification or positive density of rational residue classes is claimed.

**G. Exact divided-polynomial jets at the rational trace primes.**
On the same full residual domain, the following signed congruences hold:

    5|T(-2) => T(-2)=-5s modulo25,
    5|T(0)  => T(0)=-5s modulo25.                (22)

If 5 divides both T(1) and T(-2), then T(1)=-5s modulo25.
More generally, if 5 divides T(1), define residues

    u=s*T(1)/5 modulo5,
    v=s*T(-2)/3 modulo5,

where T(1)/5 is the actual integer quotient, while division by3 is in F5.
Then u is nonzero and

    (u,v) in {(1,3),(1,4),(2,3),(2,4),
              (3,1),(4,0),(4,2)},
    T(-1)=3u^2 modulo5,
    T(-2)=3s v modulo5,
    T(1)/5=s u modulo5.                        (23)

This seven-pair condition is exactly equivalent to the two residual equations at the actual trace1 F5 prime with the specified nonzero a,c residues and fixed T evaluations.
It is not a converse construction of an original polynomial or field.
In particular T(-1) belongs to {2,3} modulo5.
If 5 divides both T(0) and T(1) and s=1, then T(-1)=2 modulo5 and T(1)=15 modulo25.
All prior necessary-only, original-input and higher residue-degree limitations remain.

## Reuse and exact source roles

The entire preserved author candidate and the actual fixed input interfaces were read before this registration.
The local search for five-adic endpoint exclusions, negative-endpoint congruences and the coefficient-one calculation found the continuing candidate and the existing maximal-root/endpoint methods, with no fixed result at this new scope.
The [C153v2 trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) supplies the actual field degrees and nonzero integral quotient values.
The complete root-product comparison and full original local-factor count are [C619v1](Yin_C_G0619_v1.md#complete-argument), now selected proved through its existing whole review.
The elementary prime-5 application below retains every root and states its new inequalities explicitly.
It does not invoke C619's 2-adic or 3-adic conclusions at the wrong prime.

The [C616 endpoint classification](Yin_C_G0616_v1.md#complete-argument) supplies exactly the positive-unit/nu>=2 restriction at P(-1).
The [C614 maximal quotient](Yin_C_G0614_v1.md#complete-argument) supplies its complete original-order, norm, degree and actual rational-circle costs.
C619 also supplies the already proved nu<=3 statement for nonunit P(1), its seventh-power coefficient bound, even-endpoint divisibility and actual 3-prime ramification theorem.
Those fixed statements are reused at their exact scope.
Their reviews are not prospective reviews of this new five-adic argument or coefficient-one consumer.
For the additional cost correction, targeted reuse found the existing [C151 coefficient-lattice and Jensen/Parseval account](Yin_C_G0151_v1.md#fixed-lattice-energy-accounting), including its exact Eq.20 support and Mahler comparisons.
The elementary coefficient calculation is written for the present actual numerator below; no new general Parseval or coefficient-lattice theorem is claimed.
The finite analytic consumer is the entire [C196v5 norm-only theorem](Yin_C_G0196_v5.md#norm-only-sparse-transfer), and the integrable circle-log convention is the existing [Smy08-U001 normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
No new external theorem or source-proof claim is required.

For Part F, the focused local search for T(0), T(1), five-adic and linear-five conclusions found no fixed result at this scope.
The retained Parts A--B and complete C619 maximal-root comparison provide a sufficient mechanism.
C150's weighted valuation argument and C182's local cancellation argument are related context; neither supplies the new rational-cluster conclusion.
The new proof uses only direct polynomial expansions and the original local-factor accounting already used in Sections 1--4, with no new external theorem or native computation.

For Part G, the integral Frobenius divided-polynomial mechanism is already explicit in [C150's actual prime5 control](Yin_C_G0150_v1.md#actual-extra-five-control).
That original nonreciprocal control is attribution for the evaluation method, not a hypothesis or example satisfying this trace residual system.
The new trace specialization and entire four-unit-value arithmetic are supplied in Section 9, with no new external theorem or native search.

## Complete argument

### 1. Nonzero trace values and complete root-product setup

The exact trace identity gives T(2)=P(1) and T(-2)=(-1)^r P(-1).
Neither polynomial endpoint vanishes, since an irreducible nontorsion P has neither 1 nor -1 as a root.
For a primitive third root of unity zeta one has

    P(zeta)=zeta^r T(-1).

The same nontorsion hypothesis excludes zero, proving T(-1)!=0.
This both establishes finite endpoint valuations and distinguishes the trace argument -1 from the negative polynomial endpoint.

Work in a finite extension L/Q_5 containing all r actual roots delta_i of T, with v(5)=1 and v(0)=infinity.
The roots are integral because T is monic integral.
For eta in {2,-1,-2} put

    t_i=v(delta_i-eta)>=0,
    J=v_5(T(eta))=sum_(i=1)^r t_i.

Every t_i is finite by the nonzero endpoint just proved.
If J>0, choose an actual root delta_*=eta+w with maximal t=v(w)>0.
Every original conjugate is still present in the sum; roots sharing a residue are not collapsed.
The actual a,b,c at this embedding are the values in (1), and their field identities remain valid.

The precise root-product facts from C619 are especially direct here.
If v(z-eta)>t, then unequal valuations give v(z-delta_i)=t_i for every i, so v(T(z))=J.
If v(z-eta)=t, every factor has valuation at least t_i, so v(T(z))>=J.
Tied cancellation only raises a valuation in the second assertion.
Nonzero actual quotient values ensure that every T(Cp(delta_*)) used below has finite valuation.

### 2. Exclusion of 5 at eta=2 and eta=-1 under f=0

Suppose J=v_5(T(eta))>0 for one of eta=2,-1.
The exact C5 expansions are

    C5(2+w)-2=25w+50w^2+35w^3+10w^4+w^5,
    C5(-1+w)+1=-5w+5w^2+5w^3-5w^4+w^5.

Every term has valuation greater than t: the coefficients of the first four powers are divisible by 5 and the final term has valuation 5t>t.
The complete root product therefore gives

    v(T(C5(delta_*)))=J,
    C=v(c)=J-1.                                  (11)

The exact C2 expansions are

    C2(2+w)-2=4w+w^2,
    C2(-1+w)+1=-2w+w^2.

Their linear coefficients are 5-adic units and the quadratic term has larger valuation.
Thus the corresponding image has distance exactly t from eta, and

    A=v(a)=v(T(C2(delta_*)))>=J,                 (12)

because 2 is a 5-adic unit.
At 5, the equation 2c^2=3a^5 has valuation identity 2C=5A, since both 2 and 3 are units.
Equations (11)--(12) would imply

    2(J-1)=5A>=5J,

which is impossible for J>0.
This proves (2) under f=0 alone, without either the second residual equation or a g valuation.

### 3. Exact valuation and matching prime at the negative polynomial endpoint

Still assume only f=0, but now suppose J=v_5(T(-2))>0.
Choose an actual maximal-distance root delta_*=-2+w.
The expansion

    C5(-2+w)+2=25w-50w^2+35w^3-10w^4+w^5

again has valuation greater than t, yielding C=v(c)=J-1.
On the other hand

    C2(-2+w)=2-4w+w^2

reduces to 2 in the residue field.
By (2), T(2) is a 5-adic unit, so T(C2(delta_*)) has the same nonzero residue as T(2).
Consequently A=v(a)=0.
The identity 2C=5A forces C=0 and J=1, proving (3).
The stronger f-only scope of this step is explicit; the full residual hypothesis is not used until Section 4.

For every actual prime p of F above 5, let E_p=v_p(5), f_p=[O_F/p:F_5], and j_p=v_p(delta+2)>=0 in the integer normalization.
The complete local decomposition of the minimal trace polynomial has a factor of degree E_p f_p for that prime, and each of its roots has normalized distance j_p/E_p from -2.
This is the same original local-factor argument as in C619, with 5 in place of 3: F tensor Q_5 is the product of its completions, and local embeddings preserve the extended absolute value.
Taking the product over ALL r roots gives

    1=v_5(T(-2))=sum_(p|5) f_p j_p.              (13)

Every summand is a nonnegative integer.
Exactly one prime has j_p>0, and there f_p=j_p=1.
This proves (4) and in particular identifies its residue field as F_5.
It does not say that this is the only prime of F above 5, or that its ramification index equals 1.
No smaller coordinate field, normal closure or maximal power-order assumption replaces F.

### 4. Residue reconstruction using the full residual equations

Now add e+s g=0 and g!=0.
At the unique prime in (4), the preceding argument makes a and c units.
Since C3(-2)=-2, one has T(C3(delta))=0 in the residue field, while the denominator 3 is a unit.
Thus bbar=0.
The residue field is exactly F_5, so the two equations reduce to

    2 cbar^2=3 abar^5=3 abar,
    abar^3=s cbar^3.                              (14)

Both abar and cbar are nonzero.
The cube map is bijective on F_5^*: its group order is 4 and gcd(3,4)=1.
Equivalently the inverse cube map is again the cube map, so the second equation in (14) gives abar=s cbar.
The first equation gives abar=4 cbar^2=-cbar^2.
Cancelling nonzero cbar yields cbar=-s and then abar=-1.

Finally C2(delta) reduces to 2 and T(C2(delta))=2a.
It follows that

    T(2) congruent to 2abar=-2=3 modulo 5.

Since T(2)=P(1), this proves (5).
The argument would not justify replacing the residue field by an arbitrary extension of F_5; the exact f_p=1 conclusion in (13) is part of the proof.

### 5. Maximal multiplicity and all original costs

Assume the full residual domain and |P(1)|=1, |P(-1)|>1.
If nu>=2, the fixed C616 theorem forces P(-1) to belong to {1,-1,5,-5}.
Only 5 or -5 remains under the negative nonunit assumption.
But (5) would then force P(1) congruent to 3 modulo 5, whereas 1 and -1 have residues 1 and 4.
This contradiction proves nu<2, and the actual C614 lower bound nu>=1 gives nu=1.

When |P(1)|>1, adopted C619 gives nu<=3.
These are the two disjoint cases of at least one nonunit endpoint, proving every statement in (7).
The complete C614 factor table gives c_1=1000 and c_2=c_3=500.
Its original-order identity Q_s(alpha)=c_nu b_s(alpha), with b_s(alpha) a nonzero element of Z[alpha], yields (8) on the full original field of degree d.
The two stated stronger norm floors follow immediately.
No content is removed from the monic polynomial Q_s itself.

The cost statements in (9) use the same actual expanded numerator Ntilde_s=H35 Q_s.
Its degree is (30-nu)d, its leading and constant coefficients are 7, and scalar division leaves its support unchanged.
The exact original evaluation is

    u_s(alpha)=-alpha^(15d/2)g b_s(alpha)/q.

The phase has absolute norm 1 and the full q denominator contributes q^d.
The fixed C614 arithmetic input gives |Norm_K g|>=2^(6d/11), while |Norm_K b_s(alpha)|>=1, proving the norm bound in (9).
For the actual circle polynomial, scalar Mahler additivity gives the printed identity for m(u_s); it supplies no upper bound on m(Q_s).
The exact support and coefficient costs are those of Ntilde_s, not those of the earlier numerator before division by P.
No lower-degree remainder representing b_s(alpha) is substituted on the circle.
The original C614/C196 analytic requirements therefore remain substantive.

### 6. The coefficient-one consumer and its precise boundary

Use the exact q and u_s in (9), and assume ||u_s||_1<=1.
The fixed C619 seventh-power estimate is

    ||u_s||_1>=700|P(1)|^7/(30375000q).            (15)

First, 2^(6/11)<3/2: raising both positive sides to the eleventh power reduces this to

    2^17=131072<177147=3^11.

For |P(1)|>=5, equation (15) therefore gives

    ||u_s||_1>700*5^7/45562500
              =54687500/45562500>1,

a contradiction.
Thus |P(1)| is one of 1,2,3,4.
The full-residual C619 theorem says that any even P(1) is divisible by 16, excluding magnitudes 2 and 4, with both signs included.
This proves (10).

If P(1)=3 or -3, C619 gives an actual prime of F over 3 with residue degree 1 and ramification index E>=9.
The complete original-field degree sum r=sum_(p|3) E_p f_p gives r>=9, so d=2r>=18.
No own-field degree of an auxiliary value is substituted for r.

Finally, if X divides Tbar in F_2[X], then T(2) is congruent to Tbar(0)=0 modulo 2.
Hence P(1)=T(2) is even, contradicting (10).
This conditional X-factor exclusion needs no characterization of a zero-Haar class and supplies none.
No actual original input, general large-budget exclusion or unrestricted Lehmer gap is asserted.

### 7. Coefficient lattice, endpoint mass and complete norm-only transfer

Write the actual integer numerator as Ntilde_s=sum_j n_j z^j.
Every nonzero integer n_j has |n_j|>=1, so for any fixed S>0 with ||u_s||_1<=S,

    #supp(u_s)=#supp(Ntilde_s)
       <=||Ntilde_s||_1=k0 c_nu q ||u_s||_1
       <=30375000q S=B_q S.                     (16)

This holds despite any cancellation in the quotient construction, because it uses the coefficients AFTER that construction.
It does not require the displayed rational scalar to be a least denominator.
In particular S=1 supplies the integer term bound K_q=ceil(B_q) when the class is nonempty.

The constant and leading coefficients of Ntilde_s are both 7, and its degree (30-nu)d is positive.
Thus u_s has two DISTINCT coefficients of absolute value

    a_nu=7/(k0 c_nu q)>=7/B_q=epsilon_q.

If B_q<14, these two coefficients alone have total mass greater than 1, proving emptiness.
Suppose henceforth B_q>=14, so 0<epsilon_q<=1/2 and K_q>=14.
Let x_j be the absolute values of all coefficients of u_s, and let M be their maximum.
At least one of those two endpoint coefficients is different from a coefficient realizing M.
Consequently

    M+epsilon_q<=sum_j x_j<=1,
    sum_j x_j^2<=M sum_j x_j<=1-epsilon_q.        (17)

All sums include the actual expanded numerator; no support assumption has been added to (17).

For normalized Haar measure mu, finite Fourier orthogonality gives

    E_2=integral |u_s(z)|^2 dmu(z)=sum_j x_j^2>0.

This is the direct finite Parseval identity, obtained by integrating each z^(j-k) term.
The polynomial is nonzero, and its finite circle zeros have integrable logarithms under the retained scalar Mahler convention.
Apply log y<=y-1 off those zeros to y=|u_s|^2/E_2 and integrate; the right side has integral zero.
It follows that

    m(u_s)<= (1/2)log E_2
           <=(1/2)log(1-epsilon_q)=-eta_q<0.      (18)

This is precisely the existing finite coefficient-energy mechanism identified in the reuse paragraph, specialized with the two fixed endpoint masses.

Now every C196v5 NF1 hypothesis is supplied: P is the original monic irreducible nontorsion unit of degree d>=2; the rational u_s has degree 1<=(30-nu)d<=29d; (16) bounds its support by K_q; the assumed coefficient norm is at most S_0=1; (18) gives m(u_s)<=-min{eta_q,1}; and (9) gives its full original norm greater than 1.
That theorem's complete NF2--NF8 argument therefore gives (19) with C_0=29.
The fixed rational q determines all constants independently of P and of the actual nu.
All original embeddings, rational q^d and c_nu scalars, degree, Fourier, radial and source-constant expenses are retained.
No original-value integrality of u_s itself is asserted or needed.

The earlier candidate left the support and Mahler requirements stated as unresolved even after imposing coefficient-one.
Equations (16)--(18) correct that boundary for this specific family; without an actual fixed coefficient bound the endpoint statements do not provide it.
The unresolved global issue is coverage of the original full-residual domain by a useful coefficient budget, not a missing support or negative-margin proof within the coefficient-one class.

<a id="remaining-rational-five-clusters"></a>
### 8. The remaining rational trace clusters

T(0) and T(1) are nonzero: a vanishing value would give an original root of unity with trace0 or1, contrary to irreducibility and nontorsion.
All actual trace and field hypotheses are those in the Statement; no arbitrary integral triple replaces the same T.

Use v_5(5)=1 in a splitting field containing every actual root of T.
For an integer eta with J=v_5(T(eta))>0 choose a root eta+w maximizing t=v(w)>0 among all roots.
The complete product comparison gives v(T(z))=J when v(z-eta)>t and v(T(z))>=J when v(z-eta)=t.
All factors and repeated reduced roots are retained.

For eta=1 the exact expansion is

    C5(1+w)-1=-5w-5w^2+5w^3+5w^4+w^5.

Every term has valuation greater than t, giving C=v(c)=J-1.
Since C2(1+w)=-1+2w+w^2 and Part A gives T(-1) a5-adic unit, A=v(a)=0.
The equation f=0 gives 2C=5A, hence C=0 and J=1.
For the actual field primes, the full original norm decomposition is

    1=v_5(T(1))=sum_(p|5) f_p v_p(delta-1).

All summands are nonnegative integers, so precisely one is nonzero and both its factors equal1.
This conclusion does not require the second residual equation.

For eta=0 the exact expansions are

    C5(w)=5w-5w^3+w^5,
    C3(w)=-3w+w^3.

Thus C=J-1, while B=v(b)>=J because the linear coefficient -3 and the divisor3 are units at5.
If A>0, f=0 gives C=5A/2>0.
It follows from B>=J=C+1 that

    2B>3A,
    5B>3C.

The two terms in each defect then have unequal valuations, giving v(e)=3A and v(g)=3C.
But e+s g=0 requires v(e)=v(g), contradicting C=5A/2>A.
Therefore A=0, then C=0 and J=1.
At the original maximal-root prime, C2(delta) reduces to -2 and T(C2(delta))=2a is a unit, so T(-2) is a5-adic unit.
As above the complete norm identity

    1=v_5(T(0))=sum_(p|5) f_p v_p(delta)

gives the unique actual prime with f_p=v_p(delta)=1 and residue field exactly F5.
At that prime C3(delta) reduces to0 and T(0) reduces to0, so bbar=0.
The a and c residues are units.
The full residual equations become

    2 cbar^2=3 abar^5=3 abar,
    abar^3=s cbar^3.

The bijective cube map on F5^* gives abar=s cbar, whence abar=-1 and cbar=-s exactly as in Section 4.
Since T(C2(delta))=2a, reduction gives T(-2)=2abar=3 modulo5.
This proves every assertion for T(0), including exclusion of simultaneous divisibility of T(-2).

Finally suppose 5 divides T(1) and T(-2).
The f-only result at1 supplies the unique actual prime with residue field F5 and delta congruent1.
There a and c are units, while C3(1)=-2 and T(-2) is divisible by5, so bbar=0.
The same two residue equations force abar=-1 and cbar=-s.
Here C2(1)=-1, so T(-1)=2abar=3 modulo5.
The retained Part B conclusion at the negative polynomial endpoint gives T(2)=3 modulo5.


<a id="exact-rational-five-jets"></a>
### 9. Exact divided-polynomial jets and the complete trace1 residue table

The elementary Frobenius divided-polynomial mechanism is already present in C149's integral quotients and C150's actual prime5 control, where evaluating a divided polynomial is distinguished from dividing a zero residue.
For the actual trace polynomial define the integer polynomial

    Q5_T(X)=[T(C5(X))-T(X)^5]/5.

It is integral because C5(X)=X^5 modulo5 and Frobenius gives T(X)^5=T(X^5) modulo5.
At the actual root delta, c=Q5_T(delta).
For eta in{-2,0,1}, C5(eta)=eta exactly.
Whenever 5 divides T(eta) and delta reduces to eta at an actual prime over5, integer-polynomial evaluation therefore gives

    cbar=Q5_T(eta)=T(eta)/5 modulo5.             (J1)

Indeed T(eta)^5/5 is divisible by5.
The expression T(eta)/5 is an ordinary integer, and no division of a vanishing residue has been performed.
This is a specialization of the existing integral-quotient mechanism, not a new general integrality theorem.

#### Modulo25 endpoint consequences

Parts A, B and F supply valuation1, the unique actual residue-degree-one prime and cbar=-s at eta=-2 and eta=0 whenever their values are divisible by5 under the full residual equations.
Equation (J1) strengthens these two conclusions to

    5|T(-2) => T(-2)=-5s modulo25,
    5|T(0)  => T(0)=-5s modulo25.               (J2)

The other retained consequences remain T(2)=3 modulo5 in the first case and T(-2)=3 modulo5 in the second.
In particular the two divisibilities cannot hold together.
If 5 divides both T(1) and T(-2), the same Part F residue reconstruction at1 gives

    T(1)=-5s modulo25, T(-1)=3 modulo5.         (J3)

These are signed restrictions for the actual original T, without claiming any original input exists.

#### Complete residue table at the trace1 cluster

Assume 5 divides T(1).
Part F gives v_5(T(1))=1 and a unique matching prime with residue field exactly F5.
Set u=s*T(1)/5 modulo5 and v=s*T(-2)/3 modulo5, where division by3 means multiplication by its residue inverse.
Then cbar=s u, bbar=s v and u is nonzero.
Since C2(1)=-1, one has abar=T(-1)/2 modulo5.
The first residual equation gives

    abar=-u^2, T(-1)=3u^2 modulo5.

The second equation is equivalent to

    (v-1)^2=1-u^2-u^3 in F5.                  (J4)

There are exactly the following seven residue pairs:

| u | v | T(-1) modulo5 | T(-2) modulo5 |
| --- | --- | --- | --- |
| 1 | 3 | 3 | 4s |
| 1 | 4 | 3 | 2s |
| 2 | 3 | 2 | 4s |
| 2 | 4 | 2 | 2s |
| 3 | 1 | 2 | 3s |
| 4 | 0 | 3 | 0 |
| 4 | 2 | 3 | s |

To verify completeness, the right side of (J4) at u=1,2,3,4 is respectively4,4,0,1.
The square roots give v=3,4; v=3,4; v=1; v=0,2 respectively.
The last column is exactly3s v, and T(1)/5=s u determines the original integer value modulo25.
This direct four-unit-value calculation needs no native scan or J record.
The table is equivalent to the two residual equations at this exact F5 prime with nonzero a,c and the fixed T evaluations; it is not a converse construction of a field or polynomial.

In particular, 5|T(1) forces T(-1) in{2,3} modulo5.
If also 5|T(-2), the sole row is u=4,v=0, recovering (J3).
If instead 5|T(0) and s=1, the earlier T(-2)=3 forces the unique row u=3,v=1, hence T(-1)=2 modulo5 and T(1)=15 modulo25 whenever 5 also divides T(1).
No assertion for a residue field larger than F5 is imported.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision exact-five-jets-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T18:31 |
| status | open |
| reason | Retain the complete adopted v2 statement and proof and add exact signed modulo25 trace-endpoint jets and the complete seven-pair trace1 residue table, using the actual integral divided polynomial before reduction. Root is a contributor. The unchanged v2 evidence remains at its physical scope; the complete v3 requires separate review and adoption. No original input construction, higher residue-degree classification or unrestricted gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire five-adic endpoint statement](#statement) | Full actual trace domain and Parts A--G, separate f-only/full-residual hypotheses, original matching prime and residue field, exact multiplicity/norm/cost data, coefficient-one restrictions, its complete paid conditional gap, and every remaining rational five-adic cluster restriction, signed modulo25 jets and the complete trace1 residue table. |
| argument | [Complete argument](#complete-argument) | Every original root factor, exact C2/C5 expansion, full prime-degree sum, finite F_5 reconstruction, fixed endpoint consumption, all rational-circle costs, exact coefficient-one arithmetic and full coefficient-lattice/endpoint-mass/finite-transfer proof, and all Section 8 maximal-root, local cancellation, matching-prime and joint congruence arguments, and all Section 9 integral divided-polynomial and seven-pair calculations. |
| dependency | [Actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same P/K/F/T, full original degrees, reciprocal identity and nonzero integral a,b,c at every embedding. |
| dependency | [Complete maximal-root endpoint input](Yin_C_G0619_v1.md#complete-argument) | All-root product comparison and original local-factor method; accepted nonunit-P(1) multiplicity bound, seventh-power coefficient cost, even-endpoint divisibility and actual 3-prime ramification/degree restriction, each at its stated prime and domain. |
| dependency | [Positive-unit endpoint classification](Yin_C_G0616_v1.md#complete-argument) | Only the exact implication abs P(1)=1 and nu>=2 gives P(-1) in {1,-1,5,-5}; no surviving endpoint configuration is treated as realized. |
| dependency | [Actual maximal quotient and complete costs](Yin_C_G0614_v1.md#complete-argument) | Same nu,Q_s,c_nu,Ntilde_s, automatic original nonvanishing, original-order factor table, full norm and Mahler identities, degree/support/coefficient accounting and unresolved analytic-budget boundary. |
| dependency | [Complete norm-only analytic theorem](Yin_C_G0196_v5.md#norm-only-sparse-transfer) | Entire NF1--NF8 at K_q=ceil(B_q), S_0=1, C_0=29 and min(eta_q,1), with all actual hypotheses supplied and every finite/source/radial/Fourier expense retained. |
| dependency | [Scalar Mahler convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only its scalar circle-integral and integrable-zero convention used for (18), at the already accepted source-inspection scope. |
| support | [Prior coefficient-lattice mechanism](Yin_C_G0151_v1.md#fixed-lattice-energy-accounting) | Attribution and exact reuse context for integer-coefficient support and Jensen/Parseval energy comparisons; the present two-endpoint coefficient-one proof is written completely in Section 7. |
| support | [Existing divided-polynomial evaluation mechanism](Yin_C_G0150_v1.md#actual-extra-five-control) | Attribution for evaluating the integral Frobenius quotient before reducing at a prime; the old nonreciprocal example is not a premise in the present trace theorem. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T18:41 |
| status | proved |
| reason | Adopt the entire physical v3 Parts A--G and Sections 1--9 after main reading and the isolated whole R824v3 finding. The actual compared v2 chain remains intact; the new integral divided-polynomial evaluation, signed modulo25 restrictions and exhaustive seven-pair trace1 equivalence are separately checked. All original scalar, field, support and analytic costs remain. These are necessary local restrictions and a coefficient-one conditional gap, not general budget coverage, original realization or unrestricted completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire five-adic endpoint statement](#statement) | Full actual trace domain and Parts A--G, separate f-only/full-residual hypotheses, original matching prime and residue field, exact multiplicity/norm/cost data, coefficient-one restrictions, its complete paid conditional gap, and every remaining rational five-adic cluster restriction, signed modulo25 jets and the complete trace1 residue table. |
| argument | [Complete argument](#complete-argument) | Every original root factor, exact C2/C5 expansion, full prime-degree sum, finite F_5 reconstruction, fixed endpoint consumption, all rational-circle costs, exact coefficient-one arithmetic and full coefficient-lattice/endpoint-mass/finite-transfer proof, and all Section 8 maximal-root, local cancellation, matching-prime and joint congruence arguments, and all Section 9 integral divided-polynomial and seven-pair calculations. |
| dependency | [Actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same P/K/F/T, full original degrees, reciprocal identity and nonzero integral a,b,c at every embedding. |
| dependency | [Complete maximal-root endpoint input](Yin_C_G0619_v1.md#complete-argument) | All-root product comparison and original local-factor method; accepted nonunit-P(1) multiplicity bound, seventh-power coefficient cost, even-endpoint divisibility and actual 3-prime ramification/degree restriction, each at its stated prime and domain. |
| dependency | [Positive-unit endpoint classification](Yin_C_G0616_v1.md#complete-argument) | Only the exact implication abs P(1)=1 and nu>=2 gives P(-1) in {1,-1,5,-5}; no surviving endpoint configuration is treated as realized. |
| dependency | [Actual maximal quotient and complete costs](Yin_C_G0614_v1.md#complete-argument) | Same nu,Q_s,c_nu,Ntilde_s, automatic original nonvanishing, original-order factor table, full norm and Mahler identities, degree/support/coefficient accounting and unresolved analytic-budget boundary. |
| dependency | [Complete norm-only analytic theorem](Yin_C_G0196_v5.md#norm-only-sparse-transfer) | Entire NF1--NF8 at K_q=ceil(B_q), S_0=1, C_0=29 and min(eta_q,1), with all actual hypotheses supplied and every finite/source/radial/Fourier expense retained. |
| dependency | [Scalar Mahler convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only its scalar circle-integral and integrable-zero convention used for (18), at the already accepted source-inspection scope. |
| support | [Prior coefficient-lattice mechanism](Yin_C_G0151_v1.md#fixed-lattice-energy-accounting) | Attribution and exact reuse context for integer-coefficient support and Jensen/Parseval energy comparisons; the present two-endpoint coefficient-one proof is written completely in Section 7. |
| support | [Existing divided-polynomial evaluation mechanism](Yin_C_G0150_v1.md#actual-extra-five-control) | Attribution for evaluating the integral Frobenius quotient before reducing at a prime; the old nonreciprocal example is not a premise in the present trace theorem. |
| review | [Independent whole exact-jets v3 finding](../audits/reviews/Yin_R_G0824_v3.md#exact-five-jets-v3-whole-finding) | Entire physical v3 statement and proof, every actual dependency/source interface, exact unchanged-v2 comparison and separately checked Section9; historical SELF and UNKNOWN relationships remain unchanged. |

