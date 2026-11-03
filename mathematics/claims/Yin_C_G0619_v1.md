---
author: Yin
---

# Exact 2-adic and 3-adic endpoint restrictions from the complete root product

Human author Yin.
Root supplied the maximal-root argument, endpoint consequences and 3-adic companion on 2026-10-23 UTC.
Paid_comparison checked and developed the complete root-product lemma, finite valuations, exact expansions, original local-field multiplicities, residual cancellations and paid quotient consequences below.
Both are contributors; neither is an independent reviewer of this mathematics.
The fixed C616 endpoint theorem and C614 construction remain unchanged.
The relevant statement and self-root formulas of C639 were inspected for comparison; none of its new cluster-income conclusions is a premise here.
No native computation, parameter scan, source acquisition or new original-source proof inspection is used.

## Statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient 1 and degree d=2r>=2.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), and assume the actual trace field F=Q(delta) is totally real.
Let T in Z[X] be its monic minimal polynomial; the actual trace interface gives

    [F:Q]=r, [K:F]=2, P(z)=z^r T(z+z^(-1)).

Put

    C2(X)=X^2-2, C3(X)=X^3-3X,
    C5(X)=X^5-5X^3+5X,
    a=T(C2(delta))/2, b=T(C3(delta))/3,
    c=T(C5(delta))/5,
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.          (1)

The trace quotient values a,b,c are nonzero algebraic integers, equal to the divided remainders modulo T evaluated at delta.
The residual defects e,f,g may vanish exactly as allowed by the hypotheses below.
The integers T(2) and T(-1) are nonzero.
Write v_l for the rational l-adic valuation with v_l(l)=1.

**A. Two dyadic fixed points under f=0 alone.**
Assume only f=0.
For each eta in {2,-1},

    v_2(T(eta))>0 implies v_2(T(eta))>=3.          (2)

Thus an even T(2) or T(-1) is divisible by 8.
Here T(2)=P(1), whereas T(-1) is the trace value corresponding to primitive third roots of unity; it is NOT P(-1).
No full-residual conclusion for g is inferred under f=0 alone.

**B. The stronger original dyadic endpoint restriction.**
Assume additionally e+s g=0 and g!=0, with s in {1,-1}.
Then

    2 divides P(1) implies 16 divides P(1).       (3)

In particular P(1)=8 is impossible in this full residual domain.
The proof uses all actual roots of T and does not require a single prime above 2, an unramified prime, a squarefree reduction or a maximal power order.

**C. The original 3-adic endpoint and its actual ramification.**
On the same full residual domain, if 3 divides P(1), then

    v_3(P(1))=1.                                 (4)

There is exactly one prime p of the ACTUAL field F above 3 at which delta reduces to 2.
At that prime let E=v_p(3), j=v_p(delta-2), f_p=[O_F/p:F_3], using integer-normalized v_p.
Then

    f_p=j=1, E>=9, 3 divides E.                   (5)

More precisely, with A=v_p(a), B=v_p(b), C=v_p(c) and W=v_p(b+s),

    B=0, A>E, 2C=E+5A,
    W=E/3>=3.                                    (6)

Other primes above 3 may exist; none is omitted from the original field-degree or root-product accounting.
No assertion that P(1)=3 or -3 is excluded, and no realization of (4)--(6), is made.

**D. Elimination of the old multiplicity exception and paid quotient consequences.**
On the full residual domain retain the exact C614 polynomials

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    F_s=3375s z^(9d/2)H23+8H35-5(z^(5d)+1)H25,
    D_s=F_s/P, nu=ord_P F_s,
    Q_s=F_s/P^nu, Ntilde_s=H35 Q_s.

Combining (3) with the complete fixed C616 endpoint theorem gives

    |P(1)|>1 implies nu<=3,
    max{|P(1)|,|P(-1)|}>1 implies nu<=4,
    nu>=5 implies P(1),P(-1) both belong to {1,-1}. (7)

The old necessary nu=5 configuration with both endpoints 8 is therefore excluded.
The actual nonzero quotient Q_s and its C614 factor c_nu satisfy

    |P(1)|>1 implies c_nu>=500 and |Norm_K Q_s(alpha)|>=500^d,
    max{|P(1)|,|P(-1)|}>1 implies c_nu>=250
                                      and |Norm_K Q_s(alpha)|>=250^d. (8)

These are floors in the actual original order and full original field, not coefficientwise divisibility of the monic Q_s.

For every fixed positive rational q<2^(6/11), the actual normalization

    k0=30375, u_s=Ntilde_s/(k0 c_nu q)

has the following global necessary coefficient cost on the ENTIRE full residual domain:

    ||u_s||_1>=700|P(1)|^7/(30375000q).           (9)

Thus a fixed actual l1 budget bounds |P(1)| even across all remaining multiplicities.
For a paid analytic consumer on the domain with at least one nonunit endpoint, fix eta0>0, integers K_0>=2,S_0>=1 and rational q with

    exp(tau/2-eta0/2)<=q<exp(tau/2),
    tau=(12/11)log 2, J_G=2m(H35)-2log k0.

If the ACTUAL inputs satisfy

    J_G<=tau-2eta0,
    m(D_s)<=log 250+eta0/4,
    #supp(Ntilde_s)<=K_0,
    ||Ntilde_s||_1/(k0 c_nu q)<=S_0,             (10)

then the complete C614/C196 application yields

    m(P)>h_star(K_0,S_0,min{eta0/4,1})/29>0.      (11)

All original degrees, q^d denominators, c_nu scalars, Haar shifts, actual coefficients and finite analytic/source expenses are retained.
No upper Mahler or sparse budget in (10) is established automatically.
The two-unit-endpoint branch, actual input coverage and unrestricted G0001 gap remain unresolved.

## Exact reuse and scope

The actual trace degree, nonzero integrality and same-conjugate evaluation interface is [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain).
The complete local identities used are [C178 at 2](Yin_C_G0178_v1.md#argument), [C182's non-affine local 3-prime section](Yin_C_G0182_v1.md#singleton-three-adic-companion) and [C184's exact expansion R23](Yin_C_G0184_v1.md#singleton-unramified-three-exclusion).
Their actual passages were read before this derivation; no integer affine relation or C184 odd-index restriction is imposed in the new use of the displayed expansion.
The all-embedding local-factor method in [C191v2 Section 1](Yin_C_G0191_v2.md#argument) was also reread; the needed original-field count at 3 is proved explicitly below.
The accepted [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) supplies the original local-degree and valuation normalization at its recorded source-inspection scope.

Targeted local searches for maximal-root endpoint restrictions and the precise T(2),T(-1) divisibilities found no retained theorem at this scope.
C639 concerns different weighted cluster-income conclusions and is comparison context only.
[C616](Yin_C_G0616_v1.md#complete-argument) and [C614](Yin_C_G0614_v1.md#complete-argument) supply only the fixed endpoint and quotient consumer interfaces explicitly used in Part D.
No predecessor decision, source audit or review is silently enlarged to the new proof.

## Complete argument

### 1. Actual trace endpoints, conjugates and finite valuations

The fixed trace identity gives T(2)=P(1)!=0, since an irreducible nontorsion P cannot have root 1.
If zeta is a primitive third root of unity, then zeta+zeta^(-1)=-1 and

    P(zeta)=zeta^r T(-1).

Nontorsion irreducibility also excludes P(zeta)=0, proving T(-1)!=0.
This explains both the nonzero integer valuations and the distinct meaning of the trace argument -1.
Indeed P(-1)=(-1)^r T(-2), which is a different evaluation.

For a rational prime l, work in one finite extension L/Q_l containing all r roots delta_1,...,delta_r of T.
Use its extended valuation v with v(l)=1 and v(0)=infinity.
Every root is integral because T is monic integral.
For eta an integer with T(eta)!=0, define

    t_i=v(delta_i-eta)>=0,
    J=v_l(T(eta))=sum_(i=1)^r t_i.

Each t_i is finite, and J is a finite nonnegative rational-integer valuation.
If J>0, the maximum t=max_i t_i is positive and finite; choose an actual root delta_* attaining it.
This is an actual embedding of the original degree-r trace field.
The a,b,c and residual equations transport through that embedding, and the quotient values at delta_* are exactly T(C2(delta_*))/2, T(C3(delta_*))/3 and T(C5(delta_*))/5.
No arbitrary triple is substituted for these self-composition values.
All r characteristic-zero roots are retained; distinct roots with the same residue are not collapsed.

### 2. Complete root-product comparison at a maximal distance

Two elementary consequences will be used.
If v(z-eta)>t, then for every i the two distances v(z-eta) and t_i are unequal, so

    v(z-delta_i)=t_i,
    v(T(z))=J.                                   (12)

This remains valid if z=eta, since every t_i is finite.

If instead v(x-eta)>=t and v(y-eta)>=t, then every factor x-delta_i or y-delta_i has valuation at least t_i.
The exact product difference is

    T(x)-T(y)=(x-y) sum_(j=1)^r
                    [product_(i<j)(x-delta_i)]
                    [product_(i>j)(y-delta_i)].

The j-th product has valuation at least J-t_j>=J-t.
The ultrametric inequality for the sum proves

    v(T(x)-T(y))>=v(x-y)+J-t.                     (13)

A zero difference or factor is allowed through v(0)=infinity.
In particular v(x-y)>t implies v(T(x)-T(y))>J.
Possible cancellation increases the valuation and never invalidates the lower bound.
No derivative estimate, minimum root separation, ramification assumption, Hensel lift or root-count approximation is used in (12)--(13).

### 3. The f-only dyadic restrictions at eta=2 and eta=-1

Work at l=2 and assume f=0.
For either stated eta with J=v_2(T(eta))>0, choose delta_*=eta+w with v(w)=t as above.
The exact C2 expansions are

    C2(2+w)-2=4w+w^2,
    C2(-1+w)+1=-2w+w^2.

Every displayed term has valuation strictly greater than t.
Thus (12) gives v(T(C2(delta_*)))=J and, writing A=v(a), C=v(c) at this embedding,

    A=J-1.

Since a,c are nonzero integral and 2c^2=3a^5, one has

    1+2C=5A, A>0,
    C=(5J-6)/2.                                  (14)

In particular J>=2 before the stronger comparison.
The relevant C5 self-differences are exactly

    C5(2+w)-(2+w)=24w+50w^2+35w^3+10w^4+w^5,
    C5(-1+w)-(-1+w)=-6w+5w^2+5w^3-5w^4+w^5.

Their valuations are strictly greater than t, because the linear coefficients are even and every higher power of w has valuation greater than t.
The images C5(delta_*) have distance exactly t from eta: the linear coefficients in C5(eta+w)-eta are respectively 25 and -5, which are odd, and every higher term has larger valuation.
Apply (13) with x=C5(delta_*), y=delta_*.
Since T(delta_*)=0, it gives

    v(T(C5(delta_*)))>J.

The actual c is nonzero, so the valuation on the left is finite and equals C because 5 is a 2-adic unit.
Together with (14), this yields (5J-6)/2>J, hence J>2.
Since J is an integer, J>=3 and (2) follows for both eta.
This proof used only f=0, not the complete residual or any g valuation.

### 4. The full dyadic comparison and exclusion of P(1)=8

Now impose the full residual assumptions and work at eta=2 with J=v_2(T(2))>0.
The same maximal-root calculation gives A=J-1 and C=(5J-6)/2, with J>=2 (indeed Part A already gives J>=3).
The selected embedding restricts to an actual prime of the trace field.
Dividing C178's integer-normalized valuations by that prime's ramification index gives the exact identity

    v(g)=3C.

Since C-A=(3J-4)/2>0, the residual identity b^2-a^3=-s g has valuation 3C>3A.
The ultrametric equality for unequal valuations therefore forces

    2B=3A, B=v(b)=3(J-1)/2.

Moreover C-B=(2J-3)/2>0.
As 3 and 5 are 2-adic units, it follows that

    v(T(C5(delta_*))-T(C3(delta_*)))
      =v(5c-3b)=B.                               (15)

The exact expansions are

    C3(2+w)-2=9w+6w^2+w^3,
    C5(2+w)-2=25w+50w^2+35w^3+10w^4+w^5,
    C5(2+w)-C3(2+w)=16w+44w^2+34w^3+10w^4+w^5.

Both images have distance exactly t from 2, since their linear coefficients 9 and 25 are odd.
Every term in their difference has valuation greater than t.
Thus (13) makes the left side of (15) strictly greater than J, so

    3(J-1)/2>J.

This is equivalent to J>3, and its integrality gives J>=4.
Because T(2)=P(1), (3) follows.
All conjugate factors were used in obtaining the exact J; there is no assumption that their residue cluster comes from a single prime.

### 5. The full 3-adic endpoint restriction

Work at l=3, eta=2 and J=v_3(T(2))>0, choosing an actual maximal-distance root delta_*=2+w.
The expansion C3(2+w)-2=9w+6w^2+w^3 has every term of valuation greater than t.
Equation (12) therefore gives, in the normalization v(3)=1,

    B=v(b)=J-1.                                  (16)

On the other hand C2 and C5 have respective derivatives 4 and 25 at 2, both 3-adic units, so both images have distance t from 2.
Their exact difference is

    C5(2+w)-C2(2+w)=21w+49w^2+35w^3+10w^4+w^5.

Its valuation is greater than t.
Equation (13) gives

    v(T(C5(delta_*))-T(C2(delta_*)))>J.

At this prime C182's exact local identities give 2C=1+5A and C>A, where A=v(a), C=v(c).
Since 2 and 5 are 3-adic units, the last polynomial difference equals 5c-2a and has valuation A.
Consequently

    A>J.                                         (17)

If J>=2, (16) gives B>0, so the same C182 local theorem yields 2B=3A.
It would follow that A=2(J-1)/3<J, contradicting (17).
Thus J=1, proving (4).
At the selected prime (16)--(17) give B=0 and A>1 in the normalized valuation.
No assertion about the sign or absolute size of T(2) follows from its 3-adic valuation alone.

### 6. The actual unique 3-prime, complete multiplicity and index at least 9

We now explain all original-field multiplicities needed to refine the J=1 case.
For each prime p of F over 3, let E_p=v_p(3), f_p be its residue degree and j_p=v_p(delta-2)>=0, using the integer value group.
These valuations are finite because delta!=2.
The complete local-factor decomposition is

    F tensor Q_3=product_(p|3) F_p,
    T=product_(p|3) T_p, deg T_p=E_p f_p.

Here Q_3[delta]=F_p in the p-th factor, so the characteristic polynomial of multiplication by delta is its degree-E_p f_p minimal polynomial.
Its roots in the common splitting field have distance j_p/E_p from 2, because each local embedding preserves the extended 3-adic absolute value.
Their total contribution to the complete root product is f_p j_p.
Thus

    1=v_3(T(2))=sum_(p|3) f_p j_p.               (18)

Every term is a nonnegative integer.
There is exactly one prime with j_p>0, and there f_p=j_p=1.
At every other prime delta has residue different from 2.
This proves the uniqueness assertion without replacing F by a normal closure or its smaller coordinate fields.

For completeness, the unique prime's local factor reduces to (X-2)^E, where E=E_p.
Use the free Z_3 lattice O_(F_p), of rank E f_p=E, with multiplication by delta.
Its characteristic polynomial is T_p.
Filtering its reduction modulo 3 by the E maximal-ideal powers gives E one-dimensional quotients over the residue field F_3.
On every quotient delta acts as the scalar 2.
Hence T_p modulo 3 is (X-2)^E, with every original root counted.
For the other primes, the same filtration gives powers of the minimal residue polynomial of delta, none of which vanishes at 2.
It follows that the multiplicity of 2 in the COMPLETE reduction of T modulo 3 is exactly E.
This argument does not assume O_(F_p)=Z_3[delta].

At the unique prime return to integer-normalized A,B,C.
The selected maximal root belongs to this prime; every root in this cluster has distance 1/E.
Equations (16)--(17) therefore give B=0, A>E, while C182 gives 2C=E+5A and C>A.
Rewrite the exact residual equation as

    b^2(1-2s b^3)=a^3-s c^3.

The right side has valuation 3A because C>A, and B=0.
Thus v_p(1-2s b^3)=3A>3E.
Reduction gives bbar^3=-s and hence bbar=-s, since the cube map is injective in a characteristic-3 field.
Put w_b=b+s and W=v_p(w_b)>0.
The exact C184 expansion is

    1-2s b^3=3-6s w_b+6w_b^2-2s w_b^3.          (19)

If w_b=0, the valuation would be E, contradicting 3A>3E.
Thus W is finite and integral.
The four valuations in (19) are E,E+W,E+2W,3W.
Unless E=3W, the least valuation is unique and at most E, again impossible.
Therefore

    E=3W, 3 divides E, E>=3.                     (20)

To obtain the stronger lower bound, set the rational integer u=T(2)/3, which is a 3-adic unit by (4).
Write T(2+X)=sum_(i=0)^r d_i X^i with d_i in Z.
The exact residue multiplicity E just proved means 3 divides d_i for every i<E.
At the actual prime put w=delta-2, so v_p(w)=1, and x=C3(delta)-2.
Its three terms 9w,6w^2,w^3 have valuations 2E+1,E+2,3.
Since E>=3, the last is uniquely smallest and

    v_p(x)=3.

The actual quotient identity gives

    b-u=[T(2+x)-T(2)]/3
        =sum_(i=1)^r d_i x^i/3.

For 1<=i<E each summand has valuation at least E+3i-E=3i>=3.
For i>=E it has valuation at least 3i-E>=2E>=6.
Hence v_p(b-u)>=3.
As bbar=-s, the rational integer u+s is divisible by 3, so v_p(u+s)>=E, including the possibility u+s=0.
Finally

    W=v_p((b-u)+(u+s))>=min{3,E}=3.

Together with (20), this gives E=3W>=9 and proves (5)--(6).
The local degree and all norm weights refer to the original trace field, and primes not reducing delta to 2 remain in the complete degree sum.
No existence assertion or exclusion of T(2)=3,-3 is inferred.

### 7. Exact endpoint and quotient consumers

C616 proves that on |P(1)|>1 any nu>=4 would force P(1)=8.
Equation (3) now excludes that value on the full residual domain, giving the first part of (7).
If |P(1)|=1 but |P(-1)|>1, C616 gives nu<=4.
These two cases prove the rest of (7), and eliminate its former nonunit nu=5 configuration.
The fixed C614 factor table then gives c_nu>=500 when |P(1)|>1 and c_nu>=250 when either endpoint is nonunit.
Its nonzero original-order quotient proves both norm floors in (8).

For the actual normalized polynomial, C614's endpoint proof gives

    ||u_s||_1>=700|P(1)|^(10-nu)/(k0 c_nu q).

When |P(1)|>1, (7) gives nu<=3, so the exponent is at least 7.
When |P(1)|=1, any exponent gives the same value 1.
Since c_nu<=1000 on every stratum, (9) follows globally.
No coefficient estimate is obtained by treating division by P as support-preserving.

On the nonunit-endpoint domain use m(Q_s)<=m(D_s) and c_nu>=250.
Under (10),

    m(Q_s)-log c_nu<=eta0/4,
    m(u_s)=J_G/2+m(Q_s)-log c_nu-log q<=-eta0/4.

The actual full norm remains at least (2^(6/11)/q)^d>1, the degree is (30-nu)d<=29d, and (10) supplies the actual support and normalized coefficient budgets.
The entire fixed C614 application of C196v5 NF1--NF8 therefore yields (11), with all of its source constants and finite analytic costs unchanged.
The stronger endpoint arithmetic does not establish those three missing analytic budgets, either on the remaining bounded-endpoint inputs or on the two-unit-endpoint domain.

## Available review

The completed [independent whole finding R822](../audits/reviews/Yin_R_G0822_v1.md#maximal-root-endpoints-whole-finding) is now available.
The current assessment separately adopts that finding for the exact fixed theorem and its stated limitations.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision maximal-root-endpoints-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T17:31 |
| status | open |
| reason | Register the complete maximal-root endpoint proof: both f-only dyadic fixed points, full residual divisibility by16 at an even P(1), exact positive 3-adic exponent and unique actual ramification at least9, elimination of the old nonunit multiplicity exception and fully paid quotient consequences. Root and paid_comparison are contributors. Fresh whole review and adoption remain separate; no endpoint realization, automatic analytic budget or unrestricted gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire endpoint theorem](#statement) | Complete original domain and Parts A--D, separated f-only/full-residual hypotheses, actual prime/root multiplicities, finite valuations, endpoint distinction and all quotient/analytic boundaries. |
| argument | [Complete argument](#complete-argument) | All-root product and telescoping lemma, exact fixed-point expansions, residual cancellations, original 3-prime and residue multiplicity proof, integer coefficient estimate and fully paid consumers. |
| dependency | [Actual trace field and quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original degrees, monic minimal T, exact reciprocal identity and nonzero integral a,b,c at every actual embedding. |
| dependency | [Exact local 2-prime identity](Yin_C_G0178_v1.md#argument) | Only v_p(g)=3v_p(c) under both full residual equations, g!=0 and the original nonzero integral triple. |
| dependency | [Exact local 3-prime identities](Yin_C_G0182_v1.md#singleton-three-adic-companion) | Complete non-affine local calculation: 2C=E+5A, C>A, and 2B=3A when B>0; no affine conclusion used. |
| dependency | [Exact residual expansion at3](Yin_C_G0184_v1.md#singleton-unramified-three-exclusion) | The algebraic R23 identity and residue bbar=-s; the present E=3W and E>=9 argument is proved here without importing its odd/prime-to3 hypothesis. |
| dependency | [Complete local-factor interface](Yin_C_G0191_v2.md#argument) | Original-field completion and lattice-filtration root counting method, reproduced explicitly at3 here; no cluster-average bound or C639 claim used. |
| dependency | [Original local degree and valuation convention](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Only complete e_p f_p degree accounting and normalized value group in the actual finite number field, at the existing accepted source boundary. |
| dependency | [Fixed endpoint classification](Yin_C_G0616_v1.md#complete-argument) | Nonunit positive-endpoint nu>=4 forces P(1)=8; positive unit and negative nonunit implies nu<=4. These are combined with the new divisibility, without changing physical C616. |
| dependency | [Complete quotient and paid transfer](Yin_C_G0614_v1.md#complete-argument) | Same Q_s,c_nu,Ntilde_s, exact original-order norms, total Mahler and degree identities, endpoint exponent and complete NF1--NF8 consumer with all fixed source/analytic costs. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T18:00 |
| status | proved |
| reason | Adopt the entire fixed maximal-root endpoint theorem after reading its complete argument and the completed isolated whole R822 finding. Both f-only dyadic points, full residual divisibility by16, exact positive 3-adic exponent and unique original prime with ramification at least9, all multiplicity/norm/coefficient consequences and the complete conditional analytic consumer are retained. No actual residual configuration, missing analytic budget or unrestricted Mahler gap is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire endpoint theorem](#statement) | Complete original domain and Parts A--D, separated f-only/full-residual hypotheses, actual prime/root multiplicities, finite valuations, endpoint distinction and all quotient/analytic boundaries. |
| argument | [Complete argument](#complete-argument) | All-root product and telescoping lemma, exact fixed-point expansions, residual cancellations, original 3-prime and residue multiplicity proof, integer coefficient estimate and fully paid consumers. |
| dependency | [Actual trace field and quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original degrees, monic minimal T, exact reciprocal identity and nonzero integral a,b,c at every actual embedding. |
| dependency | [Exact local 2-prime identity](Yin_C_G0178_v1.md#argument) | Only v_p(g)=3v_p(c) under both full residual equations, g!=0 and the original nonzero integral triple. |
| dependency | [Exact local 3-prime identities](Yin_C_G0182_v1.md#singleton-three-adic-companion) | Complete non-affine local calculation: 2C=E+5A, C>A, and 2B=3A when B>0; no affine conclusion used. |
| dependency | [Exact residual expansion at3](Yin_C_G0184_v1.md#singleton-unramified-three-exclusion) | The algebraic R23 identity and residue bbar=-s; the present E=3W and E>=9 argument is proved here without importing its odd/prime-to3 hypothesis. |
| dependency | [Complete local-factor interface](Yin_C_G0191_v2.md#argument) | Original-field completion and lattice-filtration root counting method, reproduced explicitly at3 here; no cluster-average bound or C639 claim used. |
| dependency | [Original local degree and valuation convention](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Only complete e_p f_p degree accounting and normalized value group in the actual finite number field, at the existing accepted source boundary. |
| dependency | [Fixed endpoint classification](Yin_C_G0616_v1.md#complete-argument) | Nonunit positive-endpoint nu>=4 forces P(1)=8; positive unit and negative nonunit implies nu<=4. These are combined with the new divisibility, without changing physical C616. |
| dependency | [Complete quotient and paid transfer](Yin_C_G0614_v1.md#complete-argument) | Same Q_s,c_nu,Ntilde_s, exact original-order norms, total Mahler and degree identities, endpoint exponent and complete NF1--NF8 consumer with all fixed source/analytic costs. |
| review | [Independent whole maximal-root endpoint finding](../audits/reviews/Yin_R_G0822_v1.md#maximal-root-endpoints-whole-finding) | Entire A--D and all seven proof sections, every selected and actually used mathematical/source interface, full original root and prime multiplicities and all analytic costs, with historical UNKNOWN and SELF relationships preserved. |

