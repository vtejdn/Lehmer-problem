---
author: Yin
---

# The original first residual is never divisible by128 in the full cofactor family

Human author Yin.
Root proposed the fixed positive norm, the real cyclotomic-order inverse bound, the relative Chebyshev trace gain and the direct norm contradiction modulo1024.
Primitive_second_eight checked all conjugate valuations, positive norm signs, actual order-unit placements, the relative Lagrange coefficient identity, full norm-coefficient integrality and original coefficient-divisibility transfer, and assembled this complete deduction.
Only the elementary UV1--UV4 input in adopted C837 is reused; its Yu theorem, logarithmic bound, finite evaluated alphabet and height argument are not inputs.
No native value, cofactor witness, new numerical probe, maximal-order theorem or codifferent result is used.
The [selected adopted decision](#decision-whole-reviewed-2026-10-28) is proved through [whole independent R1059](../audits/reviews/Yin_R_G1059_v1.md#whole-finding).
That separate review covers the complete new order-unit, trace-gain and norm-congruence argument; the initial OPEN decision below retains its historical scope.

## Statement

### A. Entire actual family and coefficientwise conclusion

Use the integer traces C_0=2,C_1=X,C_(j+1)=XC_j-C_(j-1), complete monic primitive traces z^(varphi(m)/2)F_m(z+z^(-1))=Phi_m(z) for m>2, and B_n=1+sum_(j=1..(n-1)/2)C_j for odd n>1.
Fix exactly

    T_0=F_15^4 F_960 (X-2)^4 F_3^4 F_5^6 F_9^8 B_187^2,
    deg T_0=374.

Let M be the monoid of ALL finite nonnegative products of X-2 and B_n(C_(3^a5^b)), where n>1 is odd, gcd(n,15)=1 and a,b>=0.
The empty cofactor, arbitrary actual parameters, multiplicities, composite n and complete-factor overlaps are included.
For Q in M use the SAME original monic integer divisor T_Q=T_0Q and canonical polynomials

    a_Q=rem_(T_Q)(T_Q(C_2))/2,
    c_Q=rem_(T_Q)(T_Q(C_5))/5,
    F_Q=rem_(T_Q)(2c_Q^2-3a_Q^5).                           (ST1)

Every scalar prime division is an integer coefficient division before evaluation or modular reduction.
For Q=(X-2)^k product B_n(C_(3^a5^b))^e the original trace degree is374+k+sum e*3^a5^b(n-1)/2, and the full reciprocal degree is twice that number.
No lower modular-gate hypothesis or degree bound is imposed.

<a id="uniform-coefficient-precision-ceiling"></a>
For a nonzero integer polynomial H, let nu_2(H) be the minimum dyadic valuation of its nonzero coefficients; put nu_2(0)=infinity.
Then for EVERY Q in the ENTIRE monoid M,

    F_Q not in128 Z[X],
    F_Q!=0,
    nu_2(F_Q)<=6.                                         (ST2)

Equivalently, every integer n>=0 with coefficientwise2^n dividing F_Q satisfies n<=6.
There is no assertion that6 is attained or optimal.
A simultaneous residual precision requiring2^n dividing F_Q obeys the same necessary ceiling, with no separate bound for the other residual alone.
The conclusion concerns the original canonical polynomial, not merely one primary quotient or a redefined canonical system for F_960.

### B. Exact field norm and actual order denominator

Fix a primitive960th root zeta and set

    theta=zeta+zeta^(-1), L=Q(zeta), K=Q(theta),
    [L:Q]=256, [K:Q]=128,
    x_480=zeta^2+zeta^(-2), x_192=zeta^5+zeta^(-5),
    A_Q=a_Q(theta)=T_Q(x_480)/2,
    C_Q=c_Q(theta)=T_Q(x_192)/5,
    rho_Q=2C_Q^2/(3A_Q^5).

These A_Q,C_Q are nonzero and are the genuine original evaluated coefficients.
The subfields Q(x_480) and Q(x_192) have degrees64 and32, respectively.
Their even relative degrees in K fix the norm signs, and the exact norms are

    Norm_(K/Q)(A_Q)=2^32,
    Norm_(K/Q)(C_Q)=2^16,
    Norm_(K/Q)(rho_Q)=3^(-128).                            (ST3)

Every field norm here counts all128 embeddings of K, retaining multiplicities when a value belongs to a proper subfield.
It is not a norm over the reducible original divisor T_Q or a replacement for its degree.

<a id="fixed-norm-and-order-denominator"></a>
Put R_full=Z[zeta], R=Z[theta], Z_(2)={a/b in Q:b odd}, and R_(2)=R tensor_Z Z_(2), viewed inside K.
Then

    R_full intersect K=R,
    w_Q=A_Q^4/2 in R^times,
    1/A_Q^5=A_Q^3/(4w_Q^2) in(1/4)R.                     (ST4)

The order-unit assertion is part of the theorem; it is stronger than a normalized valuation estimate.
Neither R_full nor R is asserted to be a full ring of integers.

### C. Elementary relative trace and norm congruence

<a id="relative-chebyshev-trace-gain"></a>
Set t=C_32(theta), K_0=Q(t), R_0=Z[t] and f_t(X)=C_32(X)-t.
Then[K_0:Q]=4, [K:K_0]=32, f_t is the monic relative minimal polynomial and R=R_0[theta] is free of rank32 over R_0.
Its derivative satisfies

    f_t'(theta)=32u,
    u=(zeta^32-zeta^(-32))/(zeta-zeta^(-1)) in R^times.     (ST5)

For every g in R_0[X],

    Tr_(K/K_0)(g(theta)/f_t'(theta))
       =[X^31](rem_(f_t)g) in R_0,
    Tr_(K/Q)(R) subset32Z.                                (ST6)

This is proved by monic reduction and a polynomial interpolation coefficient, without a codifferent or maximal-order identification.
For every z in R_(2),

    Norm_(K/Q)(1+32z)-1 in1024Z_(2).                       (ST7)

All higher elementary symmetric coefficients are2-integral, including when z has fewer than128 distinct conjugates.
The proof uses only the first trace term and the factor32^2 in every remaining norm term.

### D. Original-divisor transfer and scope

If F_Q=128H with H in Z[X], the ACTUAL order denominator in ST4 gives

    rho_Q-1=32z_Q,
    z_Q=H(theta)A_Q^3/(3w_Q^2) in R_(2).                  (ST8)

Equations ST3 and ST7 contradict

    v_2(3^(-128)-1)=9,

since ST7 would require valuation at least10.
This proves ST2 uniformly in every actual parameter and original degree.
The evaluated norm argument is a necessary consequence of GLOBAL coefficient divisibility, not an inference of global vanishing from one local value.
No primitive factor or even scalar division is silently replaced, and the denominator3 is inverted only in Z_(2).

The theorem is elementary relative to the specified accepted unit and canonical interfaces.
No Yu/logarithmic-form theorem, finite value alphabet, height bound, native image, numerical cofactor or higher-modulus native probe is a premise.
It strengthens C837's logarithmic conclusion without changing C837 or its reviewed proof.
The new order-unit, trace-gain and norm-congruence argument requires its own review.
Optimal precision, attainment of6 and bounds for altered bases or irreducible lifts are not asserted.
The original inputs remain reducible and cyclotomic with total logarithmic Mahler measure0, so no unrestricted Lehmer-gap result or irreducible positive-measure construction follows.

## Complete argument

The complete NC1--NC6 argument below retains the same original polynomial, every field/order distinction, the actual inverse denominator and full norm multiplicities.

### NC1. Entire actual family and a fixed positive rational norm

Retain exactly

    T_0=F_15^4 F_960 (X-2)^4 F_3^4 F_5^6 F_9^8 B_187^2,
    T_Q=T_0Q,
    a_Q=rem_(T_Q)(T_Q(C_2))/2,
    c_Q=rem_(T_Q)(T_Q(C_5))/5,
    F_Q=rem_(T_Q)(2c_Q^2-3a_Q^5).

Here Q is ANY allowed finite nonnegative product of X-2 and B_n(C_(3^a5^b)), with n>1 odd, gcd(n,15)=1 and a,b>=0.
All multiplicities, the empty cofactor and the original prime divisions remain; there are no lower-gate assumptions.
Let zeta be primitive960, theta=zeta+zeta^(-1), and put

    L=Q(zeta), K=Q(theta), [L:Q]=256, [K:Q]=128,
    x_480=zeta^2+zeta^(-2), x_192=zeta^5+zeta^(-5),
    A_Q=a_Q(theta), C_Q=c_Q(theta),
    rho_Q=2C_Q^2/(3A_Q^5).

The original evaluations in C837 give A_Q=T_Q(x_480)/2 and C_Q=T_Q(x_192)/5, both nonzero.
Thus A_Q belongs to K_480=Q(x_480), of degree64, and C_Q belongs to K_192=Q(x_192), of degree32.
These field degrees are phi(N)/2: the primitive cyclotomic field has degree phi(N), and its nonreal root satisfies the quadratic over its real trace field.
Both subfields lie in K, with relative degrees2 and4.
Their norm towers show Norm_(K/Q)(A_Q)>0 and Norm_(K/Q)(C_Q)>0, since the corresponding subfield norms are nonzero rationals raised to even powers.

C837 UV2--UV4 proves that A_Q,C_Q are algebraic S-units supported only above2, and their normalized valuations at EVERY prime above2 are1/4 and1/8.
Every trace embedding sends theta to another primitive960 trace, so the same unit and order calculation applies to each of the128 conjugate values at a fixed dyadic valuation.
The rational norms have no prime support outside2; adding the128 conjugate valuations and using their positive signs gives

    Norm_(K/Q)(A_Q)=2^32,
    Norm_(K/Q)(C_Q)=2^16,
    Norm_(K/Q)(rho_Q)=3^(-128).                        (NC1)

In particular rho_Q!=1 and F_Q(theta)=3A_Q^5(rho_Q-1) is nonzero.
This is the field norm of the primitive960 evaluated value, not the norm of the reducible original divisor T_Q or a replacement of its degree by128.

### NC2. The real cyclotomic order and the exact inverse denominator

Put R_full=Z[zeta] and R=Z[theta].
The relation zeta^2-theta zeta+1=0 expresses every element of R_full as a(theta)+zeta b(theta), with a,b in Z[X].
If that element is fixed by complex conjugation, subtracting its conjugate gives(zeta-zeta^(-1))b(theta)=0.
The domain property and zeta!=zeta^(-1) imply b(theta)=0.
Consequently

    R_full intersect K=R.                              (NC2)

A real unit of R_full has a real inverse and is therefore a unit of R.
No assertion that these orders are the full rings of integers is needed.

The unit constructions used in C837 take place in R_full itself, not merely in O_L.
For nonexceptional cyclotomic pairs C266 gives an integral polynomial Bezout inverse in Z[zeta_N]; in the exceptional cases it proves Phi_(Np^j)(zeta_N)/p is a unit in that SAME cyclotomic order.
All relevant N divide960, and the trace conversion multiplies only by roots of unity.
Thus U_2(Q)=Q(x_480), U_5(Q)=Q(x_192) and the real unit u_a in a_0=u_a F_15(x_480)^4 are units of R_full and hence of R.
Here a_0=T_0(x_480)/2, exactly as in C837.

Let xi=zeta^30, a primitive32nd root, and pi=1-xi.
The actual factor identity for Phi_15 in C837 UV4 gives

    F_15(x_480)=v pi, v in R_full^times.

For every odd j modulo32, the ratio(1-xi^j)/(1-xi) is a unit in Z[xi]: its inverse is the geometric sum for an odd k with jk=1 modulo32.
Multiplying these sixteen unit ratios and using Phi_32(1)=2 proves pi^16/2 is a unit of R_full.
It follows that F_15(x_480)^16/2 is a REAL unit of R_full, hence a unit of R by NC2.
Therefore for EVERY allowed Q,

    w_Q=A_Q^4/2 in R^times,
    1/A_Q^5=A_Q^3/(4w_Q^2) in (1/4)R.                  (NC3)

This is an actual order-membership statement, stronger than a valuation inequality.
It pays the genuine scalar denominator needed in the norm argument.

### NC3. An elementary trace gain of32 in R

Let

    t=C_32(theta)=zeta^32+zeta^(-32),
    K_0=Q(t), R_0=Z[t].

The root zeta^32 has exact order30, so[K_0:Q]=phi(30)/2=4 and[K:K_0]=32.
The monic polynomial

    f_t(X)=C_32(X)-t

has degree32 and root theta, hence is the minimal polynomial of theta over K_0.
Also R_0[theta]=R, and the monic relation provides the free R_0 basis1,theta,...,theta^31; linear independence follows from the field degree.
Since R_0 has the free Z basis1,t,t^2,t^3, this also supplies a free Z basis of128 elements for R.
Direct differentiation of C_32(z+z^(-1))=z^32+z^(-32) gives

    f_t'(theta)=32u,
    u=(zeta^32-zeta^(-32))/(zeta-zeta^(-1)).             (NC4)

The numerator and denominator are root-of-unity multiples of1-zeta^64 and1-zeta^2, whose orders are15 and480.
Both are mixed, not prime powers, so C266 makes these factors units of R_full.
Their quotient u is real, hence u belongs to R^times by NC2.

For g in R_0[X], first take its monic remainder modulo f_t.
Lagrange interpolation at the32 distinct roots of f_t shows

    Tr_(K/K_0)(g(theta)/f_t'(theta))
       =[X^31](rem_(f_t)g) in R_0.                      (NC5)

Indeed the coefficient of X^31 in f_t(X)/(X-theta_i) is1, so summing the interpolation formula gives precisely this relative trace.
For any r in R, choose g with g(theta)=r u, possible because r u belongs to R_0[theta].
Equations NC4--NC5 imply Tr_(K/K_0)(r)/32 is in R_0.
Every element of R_0 is an algebraic integer, so its absolute trace is an integer.
Taking the trace tower proves

    Tr_(K/Q)(R) subset32Z.                              (NC6)

This argument uses monic division and a polynomial coefficient identity, not a maximal-order or codifferent formula.

### NC4. The direct norm congruence at the only needed scale

Let Z_(2) denote the rationals with odd denominator, and let R_(2)=R tensor_Z Z_(2), viewed inside K.
For every z in R_(2), NC6 gives Tr_(K/Q)(z) in32Z_(2).
All elementary symmetric coefficients e_i(z) of its128 embedding values belong to Z_(2), retaining repetitions when z generates a proper subfield.
To see this, write z=r/b with r in R and b odd; the characteristic polynomial of multiplication by r on the finite free Z-order R has integer coefficients, and scaling its conjugates divides e_i by b^i.
Thus the full norm expansion gives

    Norm_(K/Q)(1+32z)
      =1+32 Tr_(K/Q)(z)+sum_(i=2..128)32^i e_i(z),
    Norm_(K/Q)(1+32z)-1 in1024Z_(2).                    (NC7)

The linear term gains the factor32 from NC6, and every higher term already contains32^2=1024.
No general Newton-identity estimate, stronger trace theorem or p-adic logarithmic bound is required.

### NC5. Original coefficientwise divisibility by128 is impossible

Suppose the ORIGINAL canonical polynomial F_Q were coefficientwise divisible by128.
Write F_Q=128H with H in Z[X].
Using the original evaluation and the exact order inverse NC3 gives

    rho_Q-1=F_Q(theta)/(3A_Q^5)
           =32 z_Q,
    z_Q=H(theta) A_Q^3/(3w_Q^2) in R_(2).                (NC8)

Here3 is invertible in Z_(2), while w_Q is an actual R-unit.
Equation NC7 would force v_2(Norm_(K/Q)(rho_Q)-1)>=10.
But NC1 gives Norm_(K/Q)(rho_Q)=3^(-128), and the elementary factorization

    3^128-1=(3-1)(3+1) product_(j=1..6)(3^(2^j)+1)

has dyadic valuation1+2+6=9: every factor in the last product is2 modulo8.
The denominator3^128 is odd, so

    v_2(3^(-128)-1)=9,                                 (NC9)

a contradiction.
Therefore for EVERY Q in the ENTIRE allowed monoid,

    F_Q not in128 Z[X],
    F_Q!=0,
    nu_2(F_Q)<=6,                                     (NC10)

where nu_2 is the largest coefficientwise dyadic divisibility exponent of a nonzero integer polynomial.
No assertion that6 is attained or optimal is made.
A common residual precision that requires2^n dividing F_Q has n<=6 as well; no separate bound for the other residual alone is asserted.

### NC6. Scope and source boundary

The coefficientwise condition was used only in the valid direction F_Q=128H implies H(theta) in R.
All a/c values and prime divisions remain those of the SAME original T_Q; no canonical quotient of a proper factor was substituted.
The necessary primitive-root norm calculation suffices for this upper bound and does not infer a global identity from one local vanishing.
The result is uniform in all actual n,q,multiplicities and original degrees of the fixed T_0M family.
It is a stronger elementary bound than C837's logarithmic conclusion, while C837 itself and its selected review remain unchanged.
C837's review covers its own argument, not the new order-unit, trace-gain or norm-congruence proof here.
No Yu theorem, native value, numerical cofactor or higher-modulus native probe is used.
The potential refinement to exact optimal precision, attainment of6 and bounds for changed bases or irreducible lifts remain unproved here.
Every original input is still reducible and cyclotomic with total logarithmic Mahler measure0; the unrestricted Lehmer objective and the actual irreducible positive-measure obligations remain unresolved.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision entire-monoid-elementary-six-bit-ceiling-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T20:44 |
| status | open |
| reason | Fix the complete entire-monoid obstruction F_Q not divisible coefficientwise by128, hence nu_2(F_Q)<=6, with positive fixed field norm, real cyclotomic-order unit denominator, relative trace gain32 and direct norm congruence modulo1024. Root and primitive_second_eight are substantive contributors. Only C837's elementary unit/evaluation/order part is used; no Yu/logarithmic result, finite alphabet, height bound or native outcome supplies a premise. Exact6 attainment and optimality are unclaimed, and the unchanged-base/cyclotomic/irreducibility/total-measure limits remain. Fresh whole independent review and responsible adoption are outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire-family coefficient ceiling and exact algebraic lemmas](#statement) | ST1--ST8: full monoid and original canonical variables, zero/infinity convention and nu2<=6, positive full K norms, real order and inverse denominator, relative trace and norm congruences, exact coefficient transfer and all limits. |
| argument | [Complete NC1--NC6 proof](#complete-argument) | Full conjugate/positive-sign norm calculation, actual cyclotomic-order units and fixed subring, inverse odd-geometric sums, monic relative basis and Lagrange coefficient identity,2-integral full norm coefficients and the direct128/1024 contradiction. |
| dependency | [Adopted elementary primitive-trace unit interface](Yin_C_G0837_v1.md#decision-whole-reviewed-2026-10-28) | UV1--UV4 ONLY: actual unchanged T0/M, original canonical evaluations, all base/cofactor units, a0=u_a F15(x480)^4, S-unit support only above2 and uniform normalized dyadic orders1/4,1/8 at all primes. The Yu theorem, logarithmic bound, exact finite alphabet and height argument are not used. |
| dependency | [Adopted actual cyclotomic-order inverses](Yin_C_G0266_v1.md#decision-complete-retained-proof-adoption) | Exact-cyclotomic-crt-defect proof: integral Bezout unit inverses at non-prime-power ratios, Phi_(Np^j)(zeta_N)/p as a unit in the actual Z[zeta_N] order, and endpoint mixed-order units. The order placement is inspected directly; no maximal-order identification imported. |
| dependency | [Adopted original canonical operations](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Genuine integer prime-divided own-divisor remainders and exact evaluated cofactor identities, including all common/repeated factors; no canonical system for a proper factor is substituted. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T20:52 |
| status | proved |
| reason | Root read the complete fixed ST1--ST8/NC1--NC6 argument and whole independent R1059 finding and adopts the entire-monoid original coefficient ceiling F_Q not in128 Z[X], hence nu_2(F_Q)<=6. Exact positive full-field norms, actual order inverses, relative Lagrange trace gain and2-integral norm coefficients are paid without Yu, a finite evaluated alphabet or native evidence. The ceiling is not asserted attained or optimal, and the fixed-base, reducible cyclotomic, other-residual and irreducible-lift limits remain; the unrestricted Task is unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire-family coefficient ceiling and exact algebraic lemmas](#statement) | ST1--ST8: full monoid and original canonical variables, zero/infinity convention and nu2<=6, positive full K norms, real order and inverse denominator, relative trace and norm congruences, exact coefficient transfer and all limits. |
| argument | [Complete NC1--NC6 proof](#complete-argument) | Full conjugate/positive-sign norm calculation, actual cyclotomic-order units and fixed subring, inverse odd-geometric sums, monic relative basis and Lagrange coefficient identity,2-integral full norm coefficients and the direct128/1024 contradiction. |
| dependency | [Adopted elementary primitive-trace unit interface](Yin_C_G0837_v1.md#decision-whole-reviewed-2026-10-28) | UV1--UV4 ONLY: actual unchanged T0/M, original canonical evaluations, all base/cofactor units, a0=u_a F15(x480)^4, S-unit support only above2 and uniform normalized dyadic orders1/4,1/8 at all primes. The Yu theorem, logarithmic bound, exact finite alphabet and height argument are not used. |
| dependency | [Adopted actual cyclotomic-order inverses](Yin_C_G0266_v1.md#decision-complete-retained-proof-adoption) | Exact-cyclotomic-crt-defect proof: integral Bezout unit inverses at non-prime-power ratios, Phi_(Np^j)(zeta_N)/p as a unit in the actual Z[zeta_N] order, and endpoint mixed-order units. The order placement is inspected directly; no maximal-order identification imported. |
| dependency | [Adopted original canonical operations](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Genuine integer prime-divided own-divisor remainders and exact evaluated cofactor identities, including all common/repeated factors; no canonical system for a proper factor is substituted. |
| review | [Whole independent six-bit-ceiling finding](../audits/reviews/Yin_R_G1059_v1.md#whole-finding) | Entire ST1--ST8 and NC1--NC6, every selected elementary dependency, all conjugate/sign/order/trace/norm and coefficient-transfer obligations, independently reviewed without a mathematical repair or new native premise. |

