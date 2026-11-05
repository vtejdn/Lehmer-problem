---
author: Yin
---
# A uniform three-pair anti-reciprocal sign margin and binary original-window consequence

Human author Yin.
The sine_bound contributor developed the complete Fourier coefficient and resonance argument on 2026-11-05, Asia/Shanghai, under the coordinating agent's G0001 assignment.
Root checked the proposed resonance-count interface and requested this fixed statement and its same-field arithmetic consequence.
The selected decision below owns the assessment and exact independent review evidence.
All necessary mathematics is fixed below and no rolling draft is a proof premise.

## Statement

Let 1<=s<=3, and let a_1,...,a_s be distinct positive numbers which are either all integers or all half-integers with 2a_j odd.
Put K=max_j a_j and, for epsilon_j in{+1,-1}, define the actual integer polynomial

    A_epsilon(z)=sum_(j=1..s)epsilon_j(z^(K+a_j)-z^(K-a_j)).

Its 2s exponents are distinct integers, its constant and leading coefficients are nonzero, and its degree and span are 2K.
The logarithmic Mahler measure uses the usual unnormalized integer-polynomial convention, retaining all factors and content.
Set

    eta_3=(1/8)log(128/105)>0.

There is a sign choice with

    m(A_epsilon)<=log2-eta_3.                           (S1)

For integer frequencies this is equivalently the same assertion for F_epsilon=sum_j epsilon_j(z^(a_j)-z^(-a_j)), because A_epsilon=z^K F_epsilon and a Laurent monomial preserves measure.
For s=1 or2 every sign choice has m(A_epsilon)=0.
For s=3 the stronger four-sign average estimate (T7) below holds, with no frequency bound or separation hypothesis.

Fix C>0 and let alpha be an actual nontorsion algebraic integer unit, with monic irreducible minimal polynomial P of original degree d and total logarithmic Mahler measure m(P)>0.
Let V in Z[z] have degree T>=1 and satisfy T<=C*d and algebraically integral V(alpha)/2, allowing the value zero.
Assume its coefficientwise reduction modulo2 has exactly s reflected pairs for some 1<=s<=3:

    V(z) mod2=sum_(j=1..s)(z^(T-e_j)+z^(e_j)),
    0=e_1<e_2<...<e_s<T/2.                            (S2)

Then

    m(P)>gamma_3(C)>0,
    gamma_3(C)=min{g(6,6,C,eta_3), K0*6^(-64)/C},
    K0=(log2/4)/(2*36^8*5^64).                        (S3)

Here g is the positive constant of [C139](Yin_C_G0139_v1.md#statement), used through the adopted [C141 zero-removal assembly](Yin_C_G0141_v1.md#reuse-zero-removal).
Thus gamma_3 depends only on C and the already fixed absolute source constant in C139.
No nonzero-value hypothesis is imposed on V(alpha) or on the selected sign lift evaluated at alpha.
All quotient values, embeddings and the degree d remain in the original field Q(alpha).
The assertion is conditional on the supplied integral auxiliary and its actual original window.
It does not supply such an auxiliary for an arbitrary minimal polynomial, cover four reflected pairs, or resolve the unrestricted [Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract).

The binary phase specialization is the following.
Let H in Z[z] have H(0)!=0, actual degree k>=0, coefficient energy sum_r h_r^2<=4 and H different from the two constants +/-2.
Let n be a positive integer and sigma in{+1,-1}, set H*(z)=z^k H(1/z), V=z^n H+sigma H* and T=n+k.
Whenever V(alpha)/2 is integral, T<=C*d, and V modulo2 has at most three reflected pairs, (S3) holds for every such n, without a phase-separation hypothesis.
The possible four-pair case remains outside this assertion.

<a id="normalization-and-small-cases"></a>
## Normalization, zero sets and one or two pairs

On z=exp(i theta),

    A_epsilon(exp(i theta))
      =2i exp(iK theta) sum_j epsilon_j sin(a_j theta).

Thus m(A_epsilon)=log2+integral_0^(2pi) log|sum_j epsilon_j sin(a_j theta)| dtheta/(2pi).
Every sign choice gives a nonzero polynomial, so its finitely many circle zeros have finite order and the logarithm is integrable.
All circle integrals below use normalized Haar measure.

For half-integers put b_j=2a_j, all positive odd integers, and substitute theta=2u.
The resulting normalized logarithmic integral is over [0,pi].
Since every b_j is odd, the absolute value of sum_j epsilon_j sin(b_j u) is pi-periodic.
Its normalized integral on [0,pi] equals its full-circle mean, proving that the integer-frequency bound applies with the same Mahler normalization.
This is only an analytic substitution; it replaces neither the original algebraic field nor the auxiliary polynomial in (S2).

If s=1, the polynomial is +/- (z^(2a_1)-1), whose roots all have modulus1, so m=0.
If s=2, order the frequencies as a<b and remove one overall sign.
The two relative signs give

    A_+=(z^(a+b)-1)(z^(b-a)+1),
    A_-=(1-z^(b-a))(1+z^(a+b)).                        (S4)

Both a+b and b-a are positive integers in either parity case.
Each binomial has leading coefficient of modulus1 and all roots on the circle, so both products have m=0.
Since 0<eta_3<log2, these cases imply (S1).

<a id="argument"></a>
<a id="three-pair-uniform-margin"></a>
## Complete three-pair argument

This author argument was developed by the sine_bound contributor on 2026-11-05, Asia/Shanghai.
It uses the actual circle Fourier coefficients and does not follow from the second and fourth moments of an arbitrary random variable.

Let a_1,a_2,a_3 be distinct positive integers and define S_epsilon(theta)=sum_(j=1..3)epsilon_j sin(a_j theta) and F_epsilon(z)=sum_(j=1..3)epsilon_j(z^(a_j)-z^(-a_j)).
There is a sign choice such that

    m(F_epsilon)<=log2-eta_3,
    eta_3=(1/8)log(128/105)>0.                          (T1)

The normalization in the preceding section extends this conclusion to three distinct positive half-integers with all doubled frequencies odd.

Put s_j=sin(a_j theta), u_j=s_j^2 and

    Q_3=u_1^2+u_2^2+u_3^2-2(u_1u_2+u_1u_3+u_2u_3).

Pairing the signs directly gives

    product_(epsilon_2,epsilon_3 in{+1,-1})
      (s_1+epsilon_2s_2+epsilon_3s_3)=Q_3.             (T2)

Every factor is nonzero as a trigonometric polynomial because the positive frequencies are distinct.
Therefore the product is nonzero and its logarithm is integrable.
We shall prove the uniform circle estimate

    integral_T Q_3^2<=105/128.                          (T3)

For this purpose put X_j=exp(2i a_j theta), let e_j be the standard basis of Z^3 and write X^v=product_j X_j^(v_j).
The elementary identity 4u_j=2-X_j-X_j^(-1) gives the complete Laurent polynomial

    q(X):=16Q_3
      =-6+4 sum_j(X_j+X_j^(-1))
          +sum_j(X_j^2+X_j^(-2))
          -2 sum_(i<j)(X_i+X_i^(-1))(X_j+X_j^(-1)).    (T4)

Equivalently, its coefficients b_v are b_0=-6, b_(+/-e_j)=4, b_(+/-2e_j)=1 and b_(+/-e_i+/-e_j)=-2 for i<j, with all other coefficients zero.
The coefficient of X^v in q^2 is c_v=sum_w b_w b_(v-w).
It depends only on the decreasing rearrangement of (|v_1|,|v_2|,|v_3|).
The full multiplication table is as follows; each coefficient is per exponent vector, and the last column counts its signed coordinate permutations.

| Shape of v | c_v in q^2 | Number of vectors |
| --- | ---: | ---: |
| (0,0,0) | 186 | 1 |
| (1,0,0) | -104 | 6 |
| (2,0,0) | 20 | 6 |
| (1,1,0) | 64 | 12 |
| (3,0,0) | 8 | 6 |
| (2,1,0) | -8 | 24 |
| (1,1,1) | -48 | 8 |
| (4,0,0) | 1 | 6 |
| (2,2,0) | 6 | 12 |
| (3,1,0) | -4 | 24 |
| (2,1,1) | 4 | 24 |

This table is an explicit finite algebraic identity rather than a frequency sample.
Its completeness follows because (T4) has total absolute exponent at most2, so its square has total absolute exponent at most4; the table lists every partition of an integer at most4 into at most three positive parts, together with the zero vector.
For example c_0=(-6)^2+6*4^2+6*1^2+12*(-2)^2=186.
For v=(2,1,1), the two ordered decompositions e_1+(e_1+e_2+e_3) contribute nothing, the pair 2e_1+(e_2+e_3) contributes -4, and the pair (e_1+e_2)+(e_1+e_3) contributes8, leaving c_v=4.
All entries follow from the displayed coefficient rule by the same finite multiplication.
The exact-integer [symbolic program](../computations/programs/Yin_J_G0134/symbolic-signs.py) mechanically checks this displayed expansion without selecting any frequency tuples.

Circle integration now gives the exact expression

    256 integral_T Q_3^2
      =sum_(v in Z^3, v_1a_1+v_2a_2+v_3a_3=0)c_v.    (T5)

Every nonzero positive-coefficient row except (2,1,1) contributes zero.
Indeed rows (k,0,0) would require a_j=0, whereas rows (1,1,0) and (2,2,0) would require equality of two distinct positive frequencies.
Every negative-coefficient contribution may be discarded in an upper bound.
For a fixed doubled coordinate j, the remaining relation of shape (2,1,1), up to overall negation, requires

    2a_j=a_k+a_l  or  2a_j=|a_k-a_l|,
    {j,k,l}={1,2,3}.                                  (T6)

The two alternatives cannot both hold because a_k+a_l>|a_k-a_l| for positive a_k,a_l.
Each possible alternative determines exactly one opposite pair of exponent vectors.
Thus there are at most two contributing vectors for each of the three choices of j, each with coefficient4.
Equation (T5) is consequently at most186+3*2*4=210, which proves (T3).
The argument includes every simultaneous resonance, without requiring a general-position or bounded-frequency hypothesis.

Finally, integration of (T2), followed by Jensen's inequality applied to Q_3^2, gives

    (1/4)sum_(epsilon_1=1)m(F_epsilon)
      =log2+(1/4)integral_T log|Q_3|
      <=log2+(1/8)log(integral_T Q_3^2)
      <=log2-(1/8)log(128/105).                        (T7)

Jensen may first be applied to Q_3^2+delta and then passed to delta decreasing to zero; its nonzero polynomial logarithm is integrable, so circle zeros cause no missing case.
At least one of the four sign classes is no greater than their average, proving (T1).
This establishes only the three-pair analytic input of [D13](../drafts/Yin_D_G0013.md#binary-reflection-reduction); its arithmetic application retains the stated original-window and auxiliary-supply obligations.

<a id="binary-original-window-consequence"></a>
## Binary same-field lift and the original-window consequence

Assume (S2) and put a_j=T/2-e_j.
These frequencies are positive and distinct, and are all integers if T is even or all half-integers with odd doubled frequencies if T is odd.
Their largest value is K=T/2 because e_1=0.
Therefore (S1) supplies a sign choice for

    A(z)=sum_j epsilon_j(z^(T-e_j)-z^(e_j)),
    m(A)<=log2-eta_3.                                  (S5)

Its support has exactly 2s distinct nonzero terms, degree and span T, and coefficient length 2s<=6.
Modulo2 a plus sign equals a minus sign, so A-V belongs to 2Z[z].
Consequently

    A(alpha)/2=V(alpha)/2+((A-V)/2)(alpha)

is an algebraic integer in the original field, including when one or both displayed quotient values vanish.
No new root, extension field, norm or degree normalization is introduced.
The inequalities 0<eta_3<1, together with K_support=6, S_length=6, q=2, T<=C*d and (S5), match every hypothesis of [C141 Section1](Yin_C_G0141_v1.md#reuse-zero-removal).
That accepted assembly gives (S3).

For clarity, its treatment of a zero selected value is part of the invoked result, rather than a norm bound applied to zero.
Suppose for contradiction that m(P)<=gamma_3(C).
If A(alpha)=0, the actual support has r=2s<=6 and span T, so T*m(P)/d<=K0*6^(-64)<=K0*r^(-64).
The C92 short-annihilator input of C141 excludes this nontrivial rational relation.
Hence the selected value is nonzero, and the same C141 assembly applies its nonzero integral-quotient bound from C139 to give m(P)>g(6,6,C,eta_3)>=gamma_3(C), a contradiction.
Combining the branches gives the strict lower bound by the minimum in (S3), with no omitted zero case.
This explanation uses the adopted assembly and introduces no stronger annihilator threshold.

For the phase specialization, every nonzero coefficient of H is +/-1.
A coefficient of modulus2 would exhaust the energy budget, forcing H to be a single monomial +/-2z^r; H(0)!=0 then forces r=0, which is excluded.
The endpoint coefficients of V are h_k and sigma h_k, hence both are odd and nonzero, because n>0.
Its true degree and span are T=n+k.
Reversal about T sends V to sigma V, so its reduction modulo2 is reciprocal.
Any central coefficient comes from a single coincident term h_r+sigma h_r and is even.
Thus its nonzero binary support consists of reflected pairs, includes the endpoints, and has at most four pairs because H has at most four terms and V at most eight before collecting.
If the actual reduced support has at most three pairs, it is exactly of form (S2), so the proved result applies.
This includes overlap of the two support intervals, either reversal sign, nonmonic H and the allowed constant seeds +/-1.
It supplies no assertion for the remaining four-pair support.

<a id="four-pair-second-moment-obstruction"></a>
## The direct product second-moment method fails for four pairs

The analogous attempt to prove integral_T D^2<1 already fails for nonresonant four-frequency inputs.
This is a failure of this sufficient estimate, not a counterexample to a favorable four-pair sign.

For four distinct positive integer frequencies, put s_j=sin(a_j theta), u_j=s_j^2, Q=sum_j u_j^2-2sum_(i<j)u_i u_j and D=Q^2-64u_1u_2u_3u_4.
The exact product of the eight sign classes with epsilon_1=1 is D.
Indeed, pairing the last two signs first gives ((s_1+epsilon_2s_2)^2-u_3-u_4)^2-4u_3u_4, and multiplying the remaining two factors gives D.
For X_j=exp(2i a_j theta), put U_j=2-X_j-X_j^(-1), so u_j=U_j/4.
Then

    q_4=16Q=-24+8sum_j(X_j+X_j^(-1))
                 +sum_j(X_j^2+X_j^(-2))
                 -2sum_(i<j)(X_i+X_i^(-1))(X_j+X_j^(-1)),
    d_4=256D=q_4^2-64U_1U_2U_3U_4.                    (T8)

Expanding (T8), the signed-permutation shapes, coefficients and multiplicities are

| Shape | Coefficient of d_4 | Multiplicity |
| --- | ---: | ---: |
| (0,0,0,0) | 168 | 1 |
| (1,0,0,0) | -48 | 8 |
| (1,1,0,0) | -8 | 24 |
| (1,1,1,0) | 32 | 32 |
| (1,1,1,1) | -40 | 16 |
| (2,0,0,0) | 40 | 8 |
| (2,1,0,0) | -16 | 48 |
| (2,1,1,0) | 4 | 96 |
| (2,2,0,0) | 6 | 24 |
| (3,0,0,0) | 16 | 8 |
| (3,1,0,0) | -4 | 48 |
| (4,0,0,0) | 1 | 8 |

The table includes all possible shapes of total absolute exponent at most4 in four variables, and direct coefficient multiplication in (T8) verifies its entries.
When the only relation v dot a=0 with sum_j|v_j|<=8 is v=0, orthogonality therefore gives

    integral_T D^2
      =(168^2+8*48^2+24*8^2+32*32^2+16*40^2
         +8*40^2+48*16^2+96*4^2+24*6^2
         +8*16^2+48*4^2+8)/256^2
      =17109/8192>1.                                  (T9)

This condition is realized by the positive integer tuple (1,9,81,729).
In any nonzero relation of total absolute coefficient at most8, the largest power 9^k with nonzero coefficient has absolute contribution at least9^k, while all lower powers contribute at most7*9^(k-1)<9^k; when k=0 there is no lower contribution.
Thus no such relation vanishes.
Consequently even this genuine circle tuple defeats the bound integral_T D^2<1.
Controlling more collisions cannot repair this direct second-moment method for all four-tuples.

The same symbolic program checks (T8), the full displayed coefficient table and the exact rational value in (T9).
The actual command was `python mathematics/computations/programs/Yin_J_G0134/symbolic-signs.py`, using CPython3.13.15 with the standard library and exact integer arithmetic.
Its replaceable [output](../computations/outputs/Yin_J_G0134/symbolic-signs.json) records the tables and rational summaries; no numerical integral, frequency grid, random seed or imported data is used.
The unrestricted four-pair logarithmic inequality requires a different estimate.

## Direct inputs, reuse and proof limits

The analytic argument consists of the finite polynomial multiplication (T2)--(T4), complete coefficient table, circle orthogonality, resonance bound and concavity of logarithm written here.
The Mahler/root integral convention is the established [scalar normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization), with integer content retained.
The arithmetic consequence invokes only the exact [C141 zero-removal assembly](Yin_C_G0141_v1.md#reuse-zero-removal), at its [selected decision](Yin_C_G0141_v1.md#decision-isolated-whole-review-20261023-m04), with K_support=S_length=6, q=2, eta=eta_3 and original C.
Its inherited C92 and C139 inputs, including the fixed BS13 source constant and original angular/norm scope, remain unchanged; none is re-proved or strengthened here.

The D16 and D13 discussions, the C844/C845/C849 interfaces and their recorded bounded source search were reused before developing this argument.
A bounded follow-up search on 2026-11-05 used the queries Mahler measure sum three sine functions signs trinomials and Mahler measure sine polynomial random signs quadrinomials.
Inspected results did not supply this finite sign-product estimate, and no theorem from that search is a proof dependency.
This is not an exhaustive search or a novelty claim.
The [J134 symbolic program](../computations/programs/Yin_J_G0134/symbolic-signs.py) assists checking the explicit coefficient tables, but the complete defining coefficient rules and all-frequency resonance argument are in this fixed text.
No numerical experiment is a premise.
The four-pair comparison is an exact failure of one sufficient moment bound, not a refutation or resolution of four-pair good-sign existence.
The unrestricted auxiliary-supply and Lehmer questions remain unresolved.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T17:44 |
| status | proved |
| reason | Adopt the complete uniform sign margin for at most three reflected pairs, its supplied binary original-window consequence and the exact four-pair second-moment limitation after independent R1078. Four-pair sign selection and automatic original-input auxiliary supply remain open; no unrestricted Lehmer completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All S1--S3 frequency, sign, parity, same-field integrality and positive-integer phase quantifiers, with uniform eta and original-window constants. |
| argument | [Complete argument](#argument) | Full Fourier table and resonance proof, with the preceding normalization/small cases and subsequent arithmetic and four-pair comparison sections explicitly covered by R1078. |
| dependency | [Zero-removal assembly](Yin_C_G0141_v1.md#reuse-zero-removal) | Accepted Section 1 at K=S=6, q=2 and eta=eta_3, with original degree and possible zero value. |
| dependency | [Bounded-term norm input](Yin_C_G0139_v1.md#statement) | The same fixed g(6,6,C,eta_3), retaining its accepted source-constant and source-proof limits. |
| dependency | [Short annihilator exclusion](Yin_C_G0092_v1.md#automatic-fixed-rank-power-independence) | Actual support/span threshold in the zero branch, with its inherited angular and source boundaries. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1078_v1.md#whole-c0862-finding) | Entire theorem and comparison, actual input disclosure, direct dependency interfaces and unchanged inherited review scope. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
