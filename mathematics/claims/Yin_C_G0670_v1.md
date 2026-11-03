---
author: Yin
---

# Complete finite formal H lists at normalized multiplicities24 and28

Human author Yin.
Root proposed the two bounded formal-H classifications and the explicit distinction between passing character and whole-factor status.
Original_law checked the two character reductions, derived the exact finite algorithm and trace-order bound, authored J131 and its separately written certificate checker, and retained the complete result below.
Both are contributors, not independent reviewers of this result.
The native scope was declared before execution in [J131](../computations/programs/Yin_J_G0131/readme.md#question-and-scope); it consists of exactly32 and128 constant-one polynomials, not a sampled or expanding search.
No new D41 content, unbounded order search, new source-proof inspection, original realization or unrestricted G0001 conclusion is involved.

## Exact inputs and source boundary

The exact [C655 statement](Yin_C_G0655_v1.md#statement), adopted at [its whole-reviewed decision](Yin_C_G0655_v1.md#decision-whole-reviewed-2026-10-23), supplies T1's formal H bounds, T3's actual nondyadic epsilon0, T5's finite character and T8's original degree costs.
The exact [C652 proof](Yin_C_G0652_v1.md#argument), adopted at [its whole-reviewed decision](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23), supplies the normalized ell, triangular Theta decomposition, finite precision and B_n calibration.
[C608](Yin_C_G0608_v1.md#argument) supplies the complete primitive trace definitions, recurrence and divisor partition at their previously accepted mathematical scope.
Focused reuse found its degree-at-most3 predecessor list but no existing full degree5/7 formal-H classification.
No claim about independent source-proof inspection or another project's native result is made.

## Statement

Work over F_2 with phi(t)=1+t+t^2 and chi(t)=t phi(t)^2=t+t^3+t^5.
Let ell:1+tF_2[[t]]->Z_2 be the adopted multiplicative-to-additive character with ell(1+t)=1 and kernel Theta(U), where Theta(g)=g(t)^5/g(chi(t)).
For every odd n>1, W_n is the WHOLE primitive order-n trace polynomial, with one trace z+z^(-1) per inverse pair of primitive n-th roots.
A polynomial H is called complete here when it is a finite nonnegative product of these whole W_n, INCLUDING the allowable H factor W_5=phi.
No such completeness is assumed when enumerating H.
The formal domain is simply H in F_2[t], H(0)=1 and the stated degree bound.

For m=12,Q=32, the complete C655 necessary character is

    ell(H)=10 modulo16, deg H<=5.                         (FH1)

Among ALL32 such polynomials there is exactly ONE solution:

    H=1+t^2+t^5.                                          (FH2)

It is irreducible of degree5 and primitive trace order31, and it is not the whole W_31, whose degree is15.
Thus it is not a complete H product under the definition above.

For m=14,Q=32, the necessary condition is

    ell(H)=9 modulo16, deg H<=7.                          (FH3)

Define the following irreducible factors, where the subscript specifies primitive trace order:

    f_17=1+t+t^2+t^3+t^4,
    f_31=1+t^2+t^5,
    f_33=1+t+t^3+t^4+t^5,
    f_65,a=1+t+t^6,
    f_65,b=1+t+t^3+t^4+t^6,
    f_43=1+t+t^7.

The complete list of the EIGHT solutions of FH3 is

| H | Degree | Full irreducible factorization | Complete H product? |
| --- | ---: | --- | --- |
| 1+t+t^3+t^4+t^5 | 5 | f_33 | No |
| 1+t+t^6 | 6 | f_65,a | No |
| 1+t+t^3+t^4+t^6 | 6 | f_65,b | No |
| 1+t+t^5+t^6 | 6 | W_3^2 f_17 | No |
| 1+t+t^7 | 7 | f_43 | No |
| 1+t+t^3+t^4+t^7 | 7 | W_7 f_17 | No |
| 1+t+t^5+t^7 | 7 | W_3 W_21 | YES |
| 1+t+t^3+t^4+t^5+t^6+t^7 | 7 | W_5 f_31 | No |

Here W_3=1+t, W_5=1+t+t^2, W_7=1+t^2+t^3 and W_21=1+t^5+t^6 are themselves irreducible whole trace polynomials.
The entire table, including every factor, multiplicity and complete status, is assertion FH4.
The sole complete passing polynomial in this case has the exact character

    ell(W_3W_21)=1-8=-7=9 modulo16.                       (FH5)

For m=14 the other possible endpoint Q=64 has degree bound deg H<=1 and the SAME character9 modulo16.
Its only H are1 and1+t, of characters0 and1, so this entire endpoint branch is excluded by the character. (FH6)
For m=12 the only possible power-of-two endpoint in(2m,5m) is32.

On the ENTIRE original domain of C655, any actual A_0=24 input must consequently have Q=32 and H=f_31, with

    deg B=45, r-w=3q.                                    (FH7)

Any actual A_0=28 input must have Q=32 and one of the eight H above.
The respective degree costs by d_H=deg H are

| d_H | deg B | r-w |
| ---: | ---: | --- |
| 5 | 43 | 13q |
| 6 | 48 | 8q |
| 7 | 53 | 3q |

This is FH8, retaining the SAME original maximal q, original fields, all integer layers, canonical Y/U/R, corrected root and full gate.
Both m are nondyadic, hence epsilon=0 by the actual C655 layer identity; other correction layers have not been set to zero.
The non-complete passing H remain candidates because the original domain does not require H or Y separately to be whole complete products.
The existence of passing H, including the one complete H, does not by itself give an actual same-T realization or a complete target lift.
Neither original multiplicity24 nor28 is excluded by this result, and no one of these candidates is asserted to be realized by an original P/T.

## Complete argument

### 1. The exact moduli, degrees and original parameter scope

C655 T5, for nondyadic m, has epsilon=0 and

    Pi_N(Y)=(-165m+37Q-330ell(H))/25 modulo K_N/2,
    N=4m, K_N=the least power of2 strictly greater than N.

For m=12 or14, N is48 or56 and K_N=64, so the modulus is32.
Multiplication by25 is invertible at that modulus.
For m=12,Q=32 the constant numerator is -165*12+37*32=-796, and vanishing is equivalent to

    330ell(H)=-796 modulo32,
    10ell(H)=4 modulo32,
    5ell(H)=2 modulo16,
    ell(H)=10 modulo16,

because the inverse of5 modulo16 is13.
The bound5deg H<5m-Q=28 is exactly deg H<=5.
The endpoint bounds24<Q<60 permit only the power of2 Q=32.

For m=14,Q=32 the numerator constant is -2310+1184=-1126.
The same steps give10ell(H)=26 modulo32,5ell(H)=13 modulo16 and ell(H)=9 modulo16.
The degree inequality5deg H<38 is exactly deg H<=7.
The interval28<Q<70 permits the two powers32 and64.
At Q=64 the numerator constant is58, which is again26 modulo32, hence the same character9 modulo16 is required.
Its inequality5deg H<6 gives deg H<=1.
The two polynomials1 and1+t have exact characters0 and1, proving FH6 without an additional scan.
These are reductions of the whole known C655 character, not substitutions into its dyadic-only T6.
The nondyadic epsilon0 does not make all of Sigma or the original integer layer data vanish.

### 2. Exact finite character certificates and exhaustive candidate coverage

C652 proves that ell modulo16 is determined by the unit modulo t^16.
Its triangular generators are1+t^j at the four orders j=1,2,4,8, with character j, and one Theta generator at each remaining order j from1 through15.
For a non-power-of-two j=2^v u, u odd>=3, put e=2^v(u-2).
C652 P2 gives Theta(1+t^e)=1+t^j+terms of larger order, since Theta commutes with the indicated2^v power.
Thus multiplication by the inverse of that generator removes the j-th coefficient without changing any earlier coefficient.
The same is true of1+t^j at a power-of-two order.
Eliminating successively through order15 gives an exact certificate

    H=Theta(G)(1+t)^a modulo t^16,
    G(0)=1, deg G<16, 0<=a<16.                            (FH9)

Taking the exact character and using C652 finite precision proves ell(H)=a modulo16.
Conversely every certificate of this form proves that character value, irrespective of how it was found.
The exponent a is the sum of the selected distinct powers1,2,4,8, and G is the product of the selected Theta source factors, truncated modulo t^16.
This is a proof of the finite character algorithm, not a numerical approximation to a2-adic limit.

Every constant-one polynomial of degree at most d has the unique encoding

    H=1+sum_(i=1)^d c_i t^i,
    c=sum_(i=1)^d c_i 2^(i-1), 0<=c<2^d.

J131 generates exactly c=0,...,127, retaining all128 certificates FH9; c<32 is precisely the degree-at-most5 set.
It imposes no prefilter about factorization or primitive support.
The separate coefficient-set checker does not import the generator or rerun its elimination: it verifies FH9 directly for each of the128 rows, together with the exact input scopes and case filters.
All operations are exact polynomial addition, multiplication, unit inversion and composition over F_2.

The declared controls also all pass:32 B_n character certificates for odd1<=n<=63 against C652's exact(1-chi4(n)n)/4,15 Theta(1+t^e) certificates for1<=e<=15, and the exact leading term of all15 elimination generators.
These checks are part of the finite retained evidence and do not enlarge the candidate degree range.
Both programs are author work; separately written arithmetic does not confer an independent-review relationship.

### 3. The complete finite output and checkable reconstruction witnesses

The executed J131 classification (`mathematics/computations/outputs/Yin_J_G0131/classification.json`) contains all128 rows and the full exact factor data for every passing row.
Its separate author verification (`mathematics/computations/outputs/Yin_J_G0131/verification.json`) verifies all128 candidate certificates, all9 passing factorizations/orders/complete-status assertions and every declared control.
For a binary polynomial P=sum p_i t^i, write mask(P)=sum p_i2^i.
The complete passing outputs and their source masks in FH9 are

| Case | mask(H) | a=ell(H) modulo16 | mask(G) in FH9 |
| --- | ---: | ---: | ---: |
| m12,Q32 | 37 | 10 | 13289 |
| m14,Q32 | 59 | 9 | 54315 |
| m14,Q32 | 67 | 9 | 2485 |
| m14,Q32 | 91 | 9 | 34499 |
| m14,Q32 | 99 | 9 | 38089 |
| m14,Q32 | 131 | 9 | 26209 |
| m14,Q32 | 155 | 9 | 57023 |
| m14,Q32 | 163 | 9 | 57149 |
| m14,Q32 | 251 | 9 | 22135 |

The finite conclusion uses the checked coverage of EVERY row, not only these positive witnesses.
There is exactly one accepted mask among the32 degree-at-most5 candidates and exactly eight among the128 degree-at-most7 candidates.
Converting the masks to their polynomials gives FH2 and the H column of FH4 exactly.
The complete128-row evidence is needed for the asserted absence of other solutions; the displayed witnesses alone would not prove exhaustiveness.

### 4. Irreducibility, exact trace orders and whole-factor status

The native factorization uses exact monic division over F_2, verifies product reconstruction and tests each asserted irreducible against every monic constant-one divisor through half its degree.
A reducible constant-one polynomial has a nonconstant factor of at most half its degree, so this is an exhaustive irreducibility criterion at these degrees.
The verification program checks the same mathematical conditions with separate coefficient-set arithmetic.

For an irreducible factor f of degree d<=7 with nonzero root x in F_(2^d), let z be either root of z^2+xz+1.
The two roots are distinct because x!=0.
Frobenius to the2^d power fixes x, so it fixes z or exchanges z with z^(-1).
Thus z^(2^d-1)=1 or z^(2^d+1)=1.
Its order n is odd, at least3 and at most2^d+1<=129.
A factor f divides B_n precisely when this order divides n; the smallest such odd n is its exact primitive trace order.
This proves the finite native order bound and forbids interpreting129 as an empirical support cutoff.
Every reported order is checked by exact B_n division and nondivision for every smaller tested odd index.

The complete W_n is recovered from the exact recurrence B_1=1,B_3=1+t,B_(n+2)=tB_n+B_(n-2), followed by exact division by W_d for all proper divisors d>1 of n.
For each reported order, group all factors of H of that exact order with their actual multiplicities.
That group is complete precisely when it equals a nonnegative integer power of its full W_n; equality is checked as a polynomial, not inferred from a common order label.
Different primitive orders have disjoint trace root sets, so this criterion is both necessary and sufficient for H to be a whole product.

For the noncomplete factors in the statement, the full required degrees are

    deg W_17=8, deg W_31=15, deg W_33=10,
    deg W_43=21, deg W_65=24.

Each displayed factor f_n has smaller degree than its full W_n, and no other factor of that same order supplies the missing part in its H row.
The groups at orders3,5,7 and21 in the listed rows are complete: the retained exact division yields W_3=1+t, W_5=phi, W_7=1+t^2+t^3 and W_21=1+t^5+t^6.
This proves all complete-status entries of FH2 and FH4, including the sole complete H=W_3W_21.
As a direct analytical check on that positive example, B_21=W_3W_7W_21 and C652 gives ell(B_21)=-5, ell(W_3)=1 and ell(W_7)=2.
Hence ell(W_21)=-8 and ell(W_3W_21)=-7, proving FH5 without using its native character output as an oracle.
Allowing W_5 in the formal H classification is necessary: C655's own degree-at-most3 list explicitly contains it.
The fact that the original complete V product omits W_5 does not impose that separate omission on H.

### 5. Same-original-input consequences and the unresolved realization boundary

C655 T8 retains deg B=Q-m+5deg H and r-w=q(5m-Q-5deg H), with q the SAME actual maximal Frobenius power and with the complete original Y retained in r and w.
For A_0=24 one has m=12,Q=32 and the unique passing H has degree5, giving deg B=45 and r-w=3q.
For A_0=28, FH6 removes Q=64 at this necessary character level, and the eight Q=32 candidates have degrees5,6,7.
Substituting these degrees gives exactly(43,13q),(48,8q),(53,3q) for(deg B,r-w), proving FH7--FH8.
No original q or individual integer layer exponent has been divided, altered or chosen in this deduction.

The original problem requires the SAME actual T, canonical remainder, nonsquare normalized data, all original layer weights, full CRT class, corrected root and gate, and the characteristic-zero nonzero residual and field hypotheses.
None is supplied merely by a passing formal H.
Conversely the original theorem does not assert that H or Y alone is a complete trace product, so the incomplete rows cannot be discarded for that reason.
A full complete V may have coupled factors from its different pieces; no such completion is constructed or ruled out here.
The finite result therefore neither excludes A_0=24 or28 nor proves their original realization.
It provides the exact remaining H lists at this character filter, with reproducible native evidence and honest source/contributor boundaries, pending fresh independent whole review.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision finite-h-classification-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T01:58 |
| status | open |
| reason | Register FH1--FH9, the exhaustive exact formal-H classifications for m12,Q32 degree<=5 and m14,Q32 degree<=7, with no completeness prefilter. J131 retains all128 unique Theta reconstruction certificates and separate author verification of all candidate/calibration/factor/order/group assertions. The first case has one passing partial order31 factor; the second has eight passing polynomials, exactly one of which is the whole product W3 W21 with exact character-7. The m14,Q64 branch is separately excluded by its two degree<=1 characters. Same-original-input degree gaps retain the actual q and all canonical/layer/gate/field obligations. Root and original_law are contributors; fresh isolated whole mathematical and finite-evidence review is required. Incomplete H remain allowed candidates, and neither original multiplicity is excluded or realized. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire finite classification](#statement) | FH1--FH8, all32/128 constant-one candidates, exact one/eight passing lists, full factors and primitive orders, inclusive-H completeness, Q64 hand exclusion and original degree gaps/remaining limits. |
| argument | [Complete reduction and finite proof](#complete-argument) | Five sections and FH9: exact C655 congruences, finite triangular character certificate, exhaustive encodings and all checked native rows, rigorous factor/order bound and whole-group criterion, direct W3W21 character and original same-q boundary. |
| dependency | [Adopted exact original H character and costs](Yin_C_G0655_v1.md#decision-whole-reviewed-2026-10-23) | T1 formal H/endpoint bounds, T3 nondyadic epsilon0 without discarding other layers, T5 exact modulus and T8 same-original-q costs; every other original hypothesis remains required. |
| dependency | [Adopted exact calibrated character](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23) | Triangular Theta decomposition, ell normalization/additivity, t16-to-mod16 precision and full B_n calibration; no necessary-character sufficiency is imported. |
| dependency | [Complete root and divisor definitions](Yin_C_G0608_v1.md#argument) | Complete primitive trace sets, B_n recurrence and divisor partition only; its different native finite range and earlier gate are not premises. |
| dependency | [Executed finite native evidence](../computations/programs/Yin_J_G0131/readme.md#results-and-limits) | The predeclared full32/128 classification, all128 reconstructible Theta certificates, nine complete factor/order/group checks,32 B controls,15 Theta controls and15 leading-generator controls, with separate author arithmetic but no independent review claim. |
| support | [Exact source and scope](#exact-inputs-and-source-boundary) | Fixed-input reuse, original field/q/layer/canonical limits and the distinction between partial H and whole V; no unbounded search, new source-proof inspection, original realization or Task completion. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:29 |
| status | proved |
| reason | Adopt the entire FH1--FH9 classification and actual J131 evidence through isolated whole R891 after main reading of the full claim, native scope, independent verifier and complete review. All32 and128 allowed candidates, every reconstruction witness, nine factor/order/whole rows and all bounded controls are independently reproduced. The one/eight passing lists and Q64 hand exclusion retain the exact original q and degree costs. Partial H remain allowed; this does not supply a full original realization or exclude multiplicity24 or28. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire finite classification](#statement) | FH1--FH8, all32/128 constant-one candidates, exact one/eight passing lists, full factors and primitive orders, inclusive-H completeness, Q64 hand exclusion and original degree gaps/remaining limits. |
| argument | [Complete reduction and finite proof](#complete-argument) | Five sections and FH9: exact C655 congruences, finite triangular character certificate, exhaustive encodings and all checked native rows, rigorous factor/order bound and whole-group criterion, direct W3W21 character and original same-q boundary. |
| dependency | [Adopted exact original H character and costs](Yin_C_G0655_v1.md#decision-whole-reviewed-2026-10-23) | T1 formal H/endpoint bounds, T3 nondyadic epsilon0 without discarding other layers, T5 exact modulus and T8 same-original-q costs; every other original hypothesis remains required. |
| dependency | [Adopted exact calibrated character](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23) | Triangular Theta decomposition, ell normalization/additivity, t16-to-mod16 precision and full B_n calibration; no necessary-character sufficiency is imported. |
| dependency | [Complete root and divisor definitions](Yin_C_G0608_v1.md#argument) | Complete primitive trace sets, B_n recurrence and divisor partition only; its different native finite range and earlier gate are not premises. |
| dependency | [Executed finite native evidence](../computations/programs/Yin_J_G0131/readme.md#results-and-limits) | The predeclared full32/128 classification, all128 reconstructible Theta certificates, nine complete factor/order/group checks,32 B controls,15 Theta controls and15 leading-generator controls, with separate author arithmetic but no independent review claim. |
| support | [Exact source and scope](#exact-inputs-and-source-boundary) | Fixed-input reuse, original field/q/layer/canonical limits and the distinction between partial H and whole V; no unbounded search, new source-proof inspection, original realization or Task completion. |
| review | [Independent whole finite and native finding](../audits/reviews/Yin_R_G0891_v1.md#finite-h-classification-whole-independent-finding) | Complete FH1--FH9, every native input/program/output and independently reproduced128 characters/certificates, nine factor/order/group rows,32 B controls,15 Theta and15 leading controls; exact original-input costs and all realization boundaries. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0131](../computations/programs/Yin_J_G0131/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
