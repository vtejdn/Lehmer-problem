---
author: Yin
---

# Uniform logarithmic dyadic precision in the entire fixed cyclotomic cofactor family

Human author Yin.
Root proposed the prime-above3 nonvanishing test, fixed-algebraic-input logarithmic route, entire-monoid exact value alphabet, literal factor-count bound and coarse height bounds.
Primitive_second_eight checked every base/cofactor value and prime division, uniform normalized dyadic orders, exact centered periods, full-monoid exponent aggregation and accepted external-theorem hypotheses, and assembled this complete deduction.
The external Yu theorem is used at [Yu99-U001's checked statement and hypothesis scope](../audits/literature/Yu99/Yin_U001.md#fixed-input-logarithmic-bound); its original proof was not reviewed.
No native root approximation, alphabet enumeration, source-image value, target, correcting word, logarithm value or numerical cutoff is an input.
This entire-monoid theorem is [adopted proved](#decision-whole-reviewed-2026-10-28), through [whole independent R1057](../audits/reviews/Yin_R_G1057_v1.md#whole-finding), retaining the accepted Yu source-proof boundary.

## Statement

### A. Actual monoid, original residual and uniform units

Use C_0=2,C_1=X,C_(j+1)=XC_j-C_(j-1), complete monic primitive traces z^(varphi(m)/2)F_m(z+z^(-1))=Phi_m(z) for m>2, and B_n=1+sum_(j=1..(n-1)/2)C_j for odd n>1.
Fix exactly

    T_0=F_15^4 F_960 (X-2)^4 F_3^4 F_5^6 F_9^8 B_187^2,
    deg T_0=374.

Let M be the monoid of ALL finite nonnegative products of E=X-2 and B_n(C_(3^a5^b)), with n>1 odd, gcd(n,15)=1 and a,b>=0.
There is no bound on actual n,q=3^a5^b, multiplicities or the number of factors.
The empty cofactor, composite n and complete-factor overlaps are included.
For Q in M define at the SAME original divisor

    T_Q=T_0Q, D=deg T_Q=374+deg Q,
    a_Q=rem_(T_Q)(T_Q(C_2))/2,
    c_Q=rem_(T_Q)(T_Q(C_5))/5,
    F_Q=rem_(T_Q)(2c_Q^2-3a_Q^5).                           (ST1)

All prime divisions are genuine integer coefficient divisions before restriction or evaluation.
The full reciprocal degree is2D.
For a literal expression Q=E^k product B_n(C_(3^a5^b))^e, the exact cofactor degree is k+sum e*3^a5^b(n-1)/2.
No F4/X2, F8/X4 or other modular-gate hypothesis is imposed.

Fix a primitive960th root zeta and put

    L=Q(zeta), [L:Q]=256, theta=zeta+zeta^(-1),
    x_480=C_2(theta), x_192=C_5(theta),
    a_0=T_0(x_480)/2, c_0=T_0(x_192)/5,
    U_2(Q)=Q(x_480), U_5(Q)=Q(x_192).

The symbol theta denotes the trace point; D is the variable original trace-polynomial degree, and256 is the fixed number-field degree.
For every N dividing960, use the compatible root zeta_N=zeta^(960/N).
For EVERY Q in M, U_2(Q),U_5(Q) are global algebraic units in O_L, and

    a_0=u_a F_15(x_480)^4,
    c_0=u_c F_3(x_192)^4,
    u_a,u_c in O_L^times.                                   (ST2)

Thus a_0,c_0 and every a_Q(theta),c_Q(theta) are nonzero algebraic S-units supported ONLY above2.
The genuine original evaluations are

    a_Q(theta)=a_0 U_2(Q), c_Q(theta)=c_0 U_5(Q),
    F_Q(theta)=2c_0^2 U_5(Q)^2-3a_0^5 U_2(Q)^5.              (ST3)

For every prime mathfrak q of L above3,

    ord_mathfrak q(F_Q(theta))=0.                           (ST4)

In particular F_Q(theta)!=0 and F_Q is NEVER identically zero in this entire monoid.
No replacement canonical system for the proper factor F_960 is used.

<a id="primitive-trace-unit-product"></a>
**Definition (fixed primitive-trace unit product).**
For any actual allowed generator A set

    eta=2c_0^2/(3a_0^5), gamma_A=U_5(A)^2/U_2(A)^5.

Every gamma_A is a global unit.
At EVERY prime mathfrak p above2, normalize v_2=ord_mathfrak p/e_mathfrak p so that v_2(2)=1.
Then

    v_2(a_0)=1/4, v_2(c_0)=1/8, v_2(eta)=0,
    F_Q(theta)=3a_0^5 U_2(Q)^5[eta product_A gamma_A^(e_A)-1],
    v_2(F_Q(theta))=5/4+v_2(eta product_A gamma_A^(e_A)-1).   (ST5)

The bracket is always nonzero, because eta has valuation -ord_mathfrak q(3) above3 whereas every gamma_A has valuation0 there.
No multiplicative independence is asserted or required.

### B. A fixed finite EXACT evaluated alphabet for all of M

<a id="exact-evaluated-cofactor-alphabet"></a>
**Definition (fixed exact evaluated alphabet).**
Let Q_weight contain the least ACTUAL3^a5^b among0<=a,b<=16 in each represented residue modulo960.
The adopted C832 arithmetic construction covers every actual smooth q and has |Q_weight|<=65.
Let R be the512 unit residues1,...,1919 modulo1920, replacing1 by the ACTUAL allowed integer1921.
Set

    A_val={E} union {B_r(C_q):r in R,q in Q_weight},
    s=|A_val|=1+512|Q_weight|<=33281,
    t=1+s=2+512|Q_weight|<=33282.                            (ST6)

These are labeled counts, not assertions of distinct algebraic values.
The exact number-field pair(U_2(B_n(C_q)),U_5(B_n(C_q))) has sufficient periods n1920 and q960.
Thus every literal generator in the entire M has the same pair and gamma as a selected member of A_val.
The r=1921 representatives are genuine allowed polynomials with paired values1; no B_1 is introduced as a physical generator.
The centered geometric-sum signs are included, and these periods are proved directly in L rather than inferred from finite coefficient jets.

Aggregate the literal multiplicities of ANY Q by those paired-value labels, obtaining m_A>=0.
Then the gamma product is unchanged and

    sum_A m_A=k+sum e<=deg Q=D-374,
    0<=m_A<=D-374.                                         (ST7)

This uses the ORIGINAL factors, each of degree at least1, without replacing their degrees by residue-representative degrees or identifying the replaced polynomial with Q.
For Q=1 all m_A are zero.

### C. Explicit effective bound for original coefficientwise precision

Fix one prime mathfrak p above2 in L and write e=e_mathfrak p, f_p=f_mathfrak p.
Let h_0 be the absolute logarithmic Weil height with the [Yu99-U001 conventions](../audits/literature/Yu99/Yin_U001.md#prime-ideal-valuation-and-height-conventions).
The fixed evaluated algebraic inputs satisfy

    h_0(gamma_A)<=H_gamma=7log1921,
    h_0(eta)<=H_eta=log3+5236log2.                           (ST8)

These are heights of fixed algebraic numbers, not the total Mahler measure of a varying original polynomial.
All logarithms are natural.
Define

    K_hat=19(20 sqrt(t+1)*256)^(2(t+1)) e^(t-1)
       *2^(f_p)/(f_p log2)^2
       *log(exp(5)*t*256) H_eta H_gamma^(t-1),
    C=K_hat/e.                                             (ST9)

This is a fixed positive effective constant, independent of every allowed Q,D,n,q and multiplicity.
The source's integer ideal valuation is divided by e before comparing with v_2(2)=1.
The full field L contains zeta_3=zeta^320 as required at p=2; the real trace field or the degree of a residual value is not substituted for L and its degree256.
No numerical evaluation, optimized constant or practical cutoff is asserted.

<a id="uniform-coefficientwise-precision-bound"></a>
For EVERY Q in the ENTIRE monoid M and every integer n_F>=0 such that F_Q is coefficientwise divisible by2^(n_F),

    n_F < 5/4+C log(max(3,D-374)).                          (ST10)

The weaker inequality with <= also holds.
Because F_Q is nonzero, its largest coefficientwise dyadic divisibility exponent is finite and satisfies ST10.
The max includes Q=1; no second-residual hypothesis is needed.
A simultaneous precision condition including2^(n_F) dividing F_Q necessarily obeys the same bound, with no separate upper bound for the second residual alone.
This uses coefficient divisibility to bound one evaluated valuation, not the converse, and makes no assertion about arbitrary matrix or primary-ideal orders.

### D. Source and original-problem boundaries

The accepted [Yu99-U001 statement](../audits/literature/Yu99/Yin_U001.md#fixed-input-logarithmic-bound) supplies the fixed-input logarithmic bound without a multiplicative-independence assumption.
Root checked its primary statement, constants and hypotheses; its original proof was not reviewed, and this application retains that accepted-external-input limit.
Every project-specific unit, nonvanishing, exact-value-period, finite-alphabet, height and literal-degree obligation is proved below.
No new numerical image, rank, target, witness, native probe or p-adic logarithm computation supplies a premise.
The same constant covers the ENTIRE M, with no growing alphabet or changing field hidden in O(log D).
Along every sequence in this family with D tending to infinity,

    n_F/(sqrt(2D)log(2D)) ->0.                              (ST11)

All original reciprocal inputs remain reducible and cyclotomic with total logarithmic Mahler measure0.
This does NOT apply [C720's irreducible positive-measure criterion](Yin_C_G0720_v1.md#paid-characteristic-zero-certificate) to them; it is a separately proved precision/degree barrier for this exact T_0M family.
An irreducible lift, changed base, other cofactor class or changing field needs its own canonical precision, actual degree and total-measure argument.
No such transfer, characteristic-zero construction, unrestricted Lehmer-gap conclusion or completed original Task is asserted.

## Complete argument

The complete UV1--UV8 proof retains every original base factor, exact prime division, field-value period, valuation normalization and literal degree cost.
The trace point is denoted theta throughout, separately from the original trace degree D and fixed number-field degree256.

### UV1. Actual family, field and original canonical evaluation

Retain the complete monic primitive traces F_m and Chebyshev traces C_j from C832, and put

    T_0=F_15^4 F_960 (X-2)^4 F_3^4 F_5^6 F_9^8 B_187^2,
    deg T_0=374,
    T_Q=T_0 Q,
    D=deg T_Q=374+deg Q.

Here Q is ANY finite nonnegative product of E=X-2 and W_(n,a,b)=B_n(C_(3^a5^b)), with n>1 odd, gcd(n,15)=1 and a,b>=0.
The empty word and all repeated complete factors are included.
For a chosen literal expression Q=E^k product W_(n,a,b)^e, its actual degree is

    deg Q=k+sum e*3^a5^b(n-1)/2.                         (UV1)

Let zeta be a fixed primitive960th root, L=Q(zeta), and theta=zeta+zeta^(-1).
The field degree is[L:Q]=phi(960)=256 and zeta_3=zeta^320 belongs to L.
Set

    x_480=C_2(theta)=zeta^2+zeta^(-2),
    x_192=C_5(theta)=zeta^5+zeta^(-5).

These are primitive480 and192 traces, respectively.
Use the ORIGINAL canonical integer polynomials

    a_Q=rem_(T_Q)(T_Q(C_2))/2,
    c_Q=rem_(T_Q)(T_Q(C_5))/5,
    F_Q=rem_(T_Q)(2c_Q^2-3a_Q^5).

Their integer prime divisions and full divisor are the [accepted C736 interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25), not a new canonical system for F_960 alone.
Because T_Q(theta)=0, evaluation gives EXACTLY

    a_Q(theta)=a_0 U_2(Q),       a_0=T_0(x_480)/2,
    c_Q(theta)=c_0 U_5(Q),       c_0=T_0(x_192)/5,
    U_2(Q)=Q(x_480),         U_5(Q)=Q(x_192),
    F_Q(theta)=2c_0^2 U_5(Q)^2-3a_0^5 U_2(Q)^5.             (UV2)

All a_Q(theta),c_Q(theta),F_Q(theta) are algebraic integers because the canonical polynomials are integral.
No original F4, X2, F8 or X4 hypothesis is needed in UV1--UV2.

### UV2. Every allowed cofactor value is a global unit

The exact C266 interface gives, for distinct positive indices A,B, unit cyclotomic resultant unless max(A,B)/min(A,B) is a prime power.
It also gives Phi_(A p^j)(zeta_A)/p as a unit in Z[zeta_A] when j>=1.
For a nonexceptional pair the polynomial Bezout identity shows Phi_m(zeta_N) is a unit in Z[zeta_N]; multiplying by the root-of-unity factor in

    Phi_m(zeta_N)=zeta_N^(phi(m)/2) F_m(x_N)

makes F_m(x_N) a global algebraic unit in L.
The real value and its inverse remain algebraic integers in the real subfield; no maximal-order equality Z[x_N]=O_(Q(x_N)) is assumed.

C815 RC1 gives the FULL integer factorization

    B_n(C_(3^a5^b))=
      product_(r|n,r>1) product_(0<=i<=a,0<=j<=b) F_(3^i5^j r).
                                                               (UV3)

Every displayed order m=3^i5^j r is odd and has r>1 prime to15.
For N=480 or192, if m>N then m/N is not an integer because N is even.
If m<N and N/m were an integer, the odd m would divide the odd part15 or3 of N, impossible because of r.
Thus neither ratio can be a prime power, and EVERY factor in UV3 evaluates to a unit at x_480 and x_192.
For the endpoint,

    x_N-2=zeta_N^(-1)(zeta_N-1)^2.

The pair of cyclotomic indices1,N is nonexceptional since480 and192 are not prime powers; hence zeta_N-1 and the endpoint value are units as well.
Multiplying all factors with their actual multiplicities proves

    U_2(Q),U_5(Q) belong to O_L^times for EVERY Q in M.    (UV4)

This is a global algebraic-unit assertion, not only a dyadic-unit test or a binary target statement.

### UV3. All base factors, exact prime divisions and nonvanishing above3

The exceptional C266 formula, with(A,B,p)=(480,960,2) and(192,960,5), gives

    F_960(x_480)/2 in O_L^times,
    F_960(x_192)/5 in O_L^times.                         (UV5)

The root-of-unity conversion from Phi to F does not change unit status.
At x_480, F_15 is the sole nonunit among the remaining base factors: E,F_3,F_5,F_9 and B_187 are units.
Indeed the ratios480/3=160 and480/5=96 are not prime powers,9 does not divide480, and B_187 is already an allowed n=187,q=1 rectangle covered by UV4.
At x_192, F_3 is the sole nonunit among the remaining base factors: E,F_15,F_5,F_9 and B_187 are units.
None of15,5,9 has a prime-power ratio with192.
The only exceptional remaining ratios are480/15=32 and192/3=64, both powers of2.
All complete base exponents therefore give

    a_0=u_a F_15(x_480)^4,
    c_0=u_c F_3(x_192)^4,
    u_a,u_c in O_L^times.                               (UV6)

This accounts for the single F_960, the two different scalar divisions and every exponent in T_0.
Both a_0,c_0, and hence every a_Q(theta),c_Q(theta), are nonzero algebraic S-units supported ONLY at primes above2.
In particular at every prime mathfrak q above3 they have valuation0.
The two terms2c_Q(theta)^2 and3a_Q(theta)^5 have distinct valuations0 and ord_mathfrak q(3)>0, so

    ord_mathfrak q(F_Q(theta))=0,
    F_Q(theta)!=0,
    F_Q is not the zero polynomial.                       (UV7)

This excludes exact canonical F=0 throughout the ENTIRE monoid M, with no lower-gate or finite-alphabet restriction.
It does not assert that F has bounded dyadic precision independent of degree.

### UV4. Uniform normalized dyadic orders and the nonzero unit-product form

Fix any prime mathfrak p above2 in L and use v_2=ord_mathfrak p/e_mathfrak p, so v_2(2)=1.
For a primitive2^r root xi in L, reduction at mathfrak p gives xi=1 in the residue field.
For every odd j, (1-xi^j)/(1-xi) is a geometric sum whose residue is j=1 in characteristic2, so it is a mathfrak p-unit.
The product over all odd j modulo2^r is Phi_(2^r)(1)=2.
All2^(r-1) factors have the same valuation, proving

    v_2(1-xi)=1/2^(r-1)                                  (UV8)

at EVERY prime above2.
The exact identities

    Phi_15(z)=(z^15-1)(z-1)/[(z^5-1)(z^3-1)],
    Phi_3(z)=(z^3-1)/(z-1)

show that Phi_15(zeta_480) is a unit times1-zeta_32 and Phi_3(zeta_192) is a unit times1-zeta_64.
For the first identity the other root orders are480,96 and160; for the second the denominator order is192.
Each is mixed rather than a prime power, so its1-root factor is a global unit by C266.
The trace conversion is again a root-of-unity unit.
Using UV6 and UV8 gives uniformly

    v_2(a_0)=1/4,       v_2(c_0)=1/8,
    eta=2c_0^2/(3a_0^5),       v_2(eta)=0.                (UV9)

At every prime above3, eta has valuation -ord_mathfrak q(3).
For any actual generator A define the global unit

    gamma_A=U_5(A)^2/U_2(A)^5.

Then the exact original identity is

    F_Q(theta)=3a_0^5 U_2(Q)^5 [eta product_A gamma_A^(e_A)-1],
    v_2(F_Q(theta))=5/4+v_2(eta product_A gamma_A^(e_A)-1).   (UV10)

Every gamma_A is a global unit by UV4, and eta is a mathfrak p-unit by UV9.
The bracket never vanishes: eta product gamma_A^(e_A) still has strictly negative valuation above3 and cannot equal1.
This nonvanishing is established for all actual Q before invoking a logarithmic-form theorem.

### UV5. A fixed finite EXACT value alphabet for all of M

The following periods are proved in the number field L, not inherited from a coefficient quotient or from C832's modular period statement.
For N=480 or192 and an actual odd q=3^a5^b put w=zeta_N^q.
Its order retains the nontrivial2-part of N, so w!=1.
The centered identity is

    B_n(C_q(x_N))=w^(-(n-1)/2) S_n(w),
    S_n(w)=(1-w^n)/(1-w).                               (UV11)

The denominator is nonzero in L.
Under n -> n+2N, the centering multiplier is w^(-N)=1 and the geometric numerator is unchanged.
Under q -> q+N, w itself is unchanged.
Thus exact sufficient periods are n960/q480 at x_480 and n384/q192 at x_192.
The JOINT pair has sufficient periods

    n1920, q960.                                        (UV12)

This pays the centering sign rather than silently treating n+N as an identity.
No least-period claim is made.

Reuse only the ARITHMETIC representative construction in [C832 FH6](Yin_C_G0832_v1.md#fh6-faithful-laurent-periods-full-finite-kernel-and-positive-costs): Q_weight chooses the least ACTUAL3^a5^b among0<=a,b<=16 in each represented residue modulo960.
It has at most65 members, and every actual smooth q has a representative in it.
Let R consist of the512 units r in1,...,1919 modulo1920, replacing the residue1 by the ACTUAL allowed integer1921.
The512 count follows from the eight units in each block of30 and1920=64*30.
The finite actual value alphabet is

    A_val={E} union {B_r(C_q):r in R,q in Q_weight},
    s=|A_val|=1+512|Q_weight|<=33281.                     (UV13)

This is a labeled alphabet, not an assertion of distinct algebraic values.
Every literal generator of M has the SAME pair(U_2,U_5), and hence the same gamma, as its residue-selected label in A_val.
The r=1921 labels are genuine allowed polynomials whose paired values are1; no B_1 is introduced as a physical generator.
No algebraic-value or residue table has been enumerated.
The use of actual representatives here supplies finite algebraic inputs, not replacement degrees for the original polynomial Q.

### UV6. Literal exponent cost and fixed height bounds

Given any literal allowed expression Q=E^k product W^e, aggregate its multiplicities by the finite paired-value labels of UV13, obtaining m_A>=0.
This preserves the product of gamma values EXACTLY.
Every actual factor has degree at least1, so

    sum_A m_A=k+sum e<=deg Q=D-374,
    0<=m_A<=D-374.                                     (UV14)

This uses the original literal costs in UV1, with no substitution of a residue representative's degree and no assertion that the replaced polynomial equals Q.
It is valid for any allowed expression, even when factor overlaps permit more than one expression for Q.
For the empty cofactor all m_A are zero.

Use the [absolute logarithmic height convention](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) selected by Yu99-U001.
The local height formula gives h_0(alpha beta)<=h_0(alpha)+h_0(beta), and reversing the primitive minimal polynomial gives h_0(alpha^(-1))=h_0(alpha).
Every conjugate of a rectangle value at x_N is a sum of r roots of unity, so h_0(U_2(A)),h_0(U_5(A))<=log r for its value representative r<=1921.
The endpoint values have absolute value at most4 under every embedding and hence height at mostlog4.
The values are algebraic integers by their polynomial definitions.
Thus every label in A_val satisfies

    h_0(gamma_A)<=H_gamma=7log1921.                     (UV15)

Every root of the complete monic trace polynomial T_0 lies in[-2,2], with multiplicity retained.
Every conjugate of x_480 or x_192 is also in[-2,2], so |T_0(x_N')|<=4^374.
Since a_0,c_0 are algebraic integers, h_0(a_0),h_0(c_0)<=374log4=748log2.
Using h_0(2/3)=log3 gives

    h_0(eta)<=H_eta=log3+5236log2.                      (UV16)

These deliberately coarse symbolic bounds are independent of Q and its exponents.
No numerical height or practical cutoff has been evaluated.

### UV7. Yu's checked input and a uniform whole-monoid coefficient bound

Choose the one fixed L=Q(zeta_960), of degree256, and one fixed prime mathfrak p above2.
Write e=e_mathfrak p and f_p=f_mathfrak p for its ramification index and residue degree.
Use the fixed ordered list

    alpha_1=eta,
    alpha_(A)=gamma_A for all A in A_val,
    t=1+s=2+512|Q_weight|<=33282.                        (UV17)

Repeated values and identity values may remain in the list; the accepted [Yu99-U001 statement](../audits/literature/Yu99/Yin_U001.md#fixed-input-logarithmic-bound) requires nonzero mathfrak p-units, not multiplicative independence.
Every listed number is nonzero and a mathfrak p-unit by UV4/UV9, and zeta_3 belongs to L as required at p=2.
The exponent of eta is1, the others are the m_A from UV14, and the difference from1 is nonzero by UV10.
For

    B=max(3,D-374)

all exponent bounds required by the source therefore hold, including Q=1.
The source proof is accepted externally at the stated statement/hypothesis inspection scope; it is not re-proved or independently audited here.

One fully defined effective upper constant follows from the printed337 consequence retained in Yu99-U001:

    K_hat=19(20 sqrt(t+1)*256)^(2(t+1)) e^(t-1)
       *2^(f_p)/(f_p log2)^2
       *log(exp(5)*t*256) H_eta H_gamma^(t-1),
    C=K_hat/e.                                         (UV18)

H_eta and H_gamma exceed log2 and bound the respective absolute logarithmic heights by UV15--UV16.
The fixed field, prime, actual finite ordered list and their invariants make C fixed and effective, independent of every allowed Q, n, q, multiplicity and literal factor count.
No numerical evaluation of C or useful numerical threshold is asserted.
Yu's bound concerns the INTEGER ideal valuation ord_mathfrak p; division by e is essential and gives

    v_2(eta product_A gamma_A^(m_A)-1)<C log B.          (UV19)

Now let n_F>=0 be an integer such that the ORIGINAL canonical polynomial F_Q is coefficientwise divisible by2^(n_F).
Its value at the algebraic integer theta belongs to2^(n_F)O_L, so n_F<=v_2(F_Q(theta)).
Combine this direction of evaluation, UV10 and UV19 to obtain

    n_F < 5/4+C log(max(3,D-374))                       (UV20)

for EVERY Q in the ENTIRE monoid M.
The weaker inequality with <= also holds.
Since F_Q is never the zero polynomial, its largest coefficientwise dyadic divisibility exponent is finite and satisfies this same bound.
A simultaneous F/X precision is necessarily bounded by UV20 through its F component; no separate upper bound for the X residual alone is asserted.
This is a coefficientwise original-residual bound, not a converse from one local value to all coefficients or a statement about arbitrary matrix or primary-ideal order.

### UV8. Consequence and original-problem boundary

The constant in UV20 is uniform over the entire cofactor monoid because its exact paired values have the fixed finite alphabet of UV13.
There is no growing-alphabet or changing-number-field constant hidden in the O(log D) conclusion.
For any sequence in this family with D tending to infinity, the possible original F precision satisfies n_F/(sqrt(2D)log(2D)) ->0.
This does not apply [C720's irreducible positive-measure theorem](Yin_C_G0720_v1.md#paid-characteristic-zero-certificate) to these reducible cyclotomic inputs.
Rather, it proves a separate necessary precision/degree barrier within the actual fixed family, while C720 retains its SAME irreducible reciprocal nontorsion input and controlled positive-total-measure requirements.
An irreducible lift or a changed base/profile would need its own canonical precision, full degree and total-measure argument; those properties do not transfer from this monoid.
No unrestricted Lehmer gap, characteristic-zero construction, practical exponent cutoff, new native outcome or optimization of the fixed constant is asserted.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision whole-monoid-logarithmic-precision-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T20:20 |
| status | open |
| reason | Fix the complete entire-monoid global-unit and exact nonvanishing argument, uniform dyadic orders, finite EXACT evaluated alphabet and explicit effective logarithmic coefficient-precision bound at the unchanged T0/F960 profile. Root and primitive_second_eight are substantive contributors. Yu99 is an accepted established external statement with its source-proof inspection limit preserved; all project-specific hypotheses, exponents and degrees are paid. No native value, practical cutoff, irreducible lift, positive-measure control or unrestricted G0001 result is asserted. Fresh whole independent review and responsible adoption remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire-monoid unit and precision theorem](#statement) | ST1--ST11: full actual monoid and canonical polynomial, exact units/nonvanishing, normalized dyadic orders, finite evaluated alphabet and literal exponent bound, explicit effective constant, coefficientwise precision and all source/Task limits. |
| argument | [Complete UV1--UV8 proof](#complete-argument) | All base/cofactor resultant cases and prime divisions, direct dyadic valuation calculation, exact centered periods including signs, finite whole-monoid aggregation, height bounds, every Yu hypothesis and ideal-valuation conversion, original coefficient implication and asymptotic scope. |
| dependency | [Accepted fixed-input Yu bound](../audits/literature/Yu99/Yin_U001.md#yu99-u001) | Fixed-input-logarithmic-bound section: published1999 printed337--339 Theorem1 and displayed consequence, full field/unit/nonvanishing hypotheses, height conventions and explicit constant. Primary statement/hypotheses checked by root; original proof unreviewed. No changing-field or growing-alphabet uniformity is imported. |
| dependency | [Adopted exact cyclotomic ideal/resultant interface](Yin_C_G0266_v1.md#decision-complete-retained-proof-adoption) | Full exact-cyclotomic-crt-defect argument: unit Bezout case for non-prime-power ratios, prime support in exceptional cases and Phi_(ap^j)(zeta_a)/p as a unit. Its selected self-review scope is retained; no new original-source or independent inspection asserted. |
| dependency | [Adopted full rectangle factorization](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) | RC1 complete integer factors F_(3^i5^j r), all divisor orders, exact degrees and no new odd parts3/5/15. No local classification, native image or target is used. |
| dependency | [Adopted actual family and smooth representative construction](Yin_C_G0832_v1.md#decision-whole-reviewed-2026-10-28) | Exact T0 degree374, complete endpoint/rectangle monoid and canonical variables; FH6 arithmetic construction of actual q representatives modulo960 with exponents0..16 and at most65 classes. Its modular period theorem is not used to infer the new exact number-field periods. |
| dependency | [Adopted original canonical integer operations](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Genuine prime-divided own-divisor remainders and evaluation/weighting identities before all field and modular calculations, including repeated/common factors. |
| dependency | [Accepted absolute-height convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Smy08-height-normalization section: primitive minimal-polynomial and common-field local formulas, finite-place contributions, rational scalar height and field-extension invariance; elementary product/inverse estimates are derived at use. Other reported bounds and questioned source claims are not inputs. |
| support | [Original irreducible precision boundary](Yin_C_G0720_v1.md#paid-characteristic-zero-certificate) | Comparison only: same irreducible reciprocal nontorsion input, positive total measure and full-degree finite-precision thresholds. Not applied to the current reducible measure-zero family or used to prove ST10. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T20:29 |
| status | proved |
| reason | Root read the complete ST1--ST11/UV1--UV8 deduction and whole independent R1057 finding, including the primary Yu statement/hypothesis check and every project-specific unit, norm-place, period, degree and height obligation. Adopt the entire-monoid nonvanishing and uniform effective logarithmic coefficient-precision bound at the fixed base. Yu remains an accepted established external input whose original proof was not audited; no practical constant, irreducible lift, positive-measure control or unrestricted Task conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire-monoid unit and precision theorem](#statement) | ST1--ST11: full actual monoid and canonical polynomial, exact units/nonvanishing, normalized dyadic orders, finite evaluated alphabet and literal exponent bound, explicit effective constant, coefficientwise precision and all source/Task limits. |
| argument | [Complete UV1--UV8 proof](#complete-argument) | All base/cofactor resultant cases and prime divisions, direct dyadic valuation calculation, exact centered periods including signs, finite whole-monoid aggregation, height bounds, every Yu hypothesis and ideal-valuation conversion, original coefficient implication and asymptotic scope. |
| dependency | [Accepted fixed-input Yu bound](../audits/literature/Yu99/Yin_U001.md#yu99-u001) | Fixed-input-logarithmic-bound section: published1999 printed337--339 Theorem1 and displayed consequence, full field/unit/nonvanishing hypotheses, height conventions and explicit constant. Primary statement/hypotheses checked by root; original proof unreviewed. No changing-field or growing-alphabet uniformity is imported. |
| dependency | [Adopted exact cyclotomic ideal/resultant interface](Yin_C_G0266_v1.md#decision-complete-retained-proof-adoption) | Full exact-cyclotomic-crt-defect argument: unit Bezout case for non-prime-power ratios, prime support in exceptional cases and Phi_(ap^j)(zeta_a)/p as a unit. Its selected self-review scope is retained; no new original-source or independent inspection asserted. |
| dependency | [Adopted full rectangle factorization](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) | RC1 complete integer factors F_(3^i5^j r), all divisor orders, exact degrees and no new odd parts3/5/15. No local classification, native image or target is used. |
| dependency | [Adopted actual family and smooth representative construction](Yin_C_G0832_v1.md#decision-whole-reviewed-2026-10-28) | Exact T0 degree374, complete endpoint/rectangle monoid and canonical variables; FH6 arithmetic construction of actual q representatives modulo960 with exponents0..16 and at most65 classes. Its modular period theorem is not used to infer the new exact number-field periods. |
| dependency | [Adopted original canonical integer operations](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Genuine prime-divided own-divisor remainders and evaluation/weighting identities before all field and modular calculations, including repeated/common factors. |
| dependency | [Accepted absolute-height convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Smy08-height-normalization section: primitive minimal-polynomial and common-field local formulas, finite-place contributions, rational scalar height and field-extension invariance; elementary product/inverse estimates are derived at use. Other reported bounds and questioned source claims are not inputs. |
| support | [Original irreducible precision boundary](Yin_C_G0720_v1.md#paid-characteristic-zero-certificate) | Comparison only: same irreducible reciprocal nontorsion input, positive total measure and full-degree finite-precision thresholds. Not applied to the current reducible measure-zero family or used to prove ST10. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G1057_v1.md#whole-finding) | Entire fixed statement and complete argument, all selected dependency applications and exact stated limits; independently reviewed at the recorded whole scope. |

