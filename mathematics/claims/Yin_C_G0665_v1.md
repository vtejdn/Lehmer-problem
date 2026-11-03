---
author: Yin
---

# Complete trace products satisfy the large dyadic positive-character and degree conditions

Human author Yin.
Root proposed the thirteen-prime construction and the floor/remainder adjustment; original_law checked the exact formal H domain, prime certificate, Mobius sign, product cancellation and explicit uniform threshold as a contributor.
Both are authors of the present development, not independent reviewers.
This result is developed under the active [G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).

## Exact question, inputs and scope

The question is only whether the necessary dyadic epsilon1 character and complete-factor degree conditions from [adopted C655](Yin_C_G0655_v1.md#decision-whole-reviewed-2026-10-23) can be met by formal polynomials H at every sufficiently large dyadic m.
Use the calibrated character and complete trace polynomials of [adopted C652](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23), with their [C608 trace/divisor definitions](Yin_C_G0608_v1.md#argument).
The exact bound here is all m=2^j with integer j>=70, one fixed explicitly specified squarefree odd order n, and the two complete factors W_n,W_3 at nonnegative integer multiplicities.
No native computation, prime search, degree scan, unrestricted source assertion or original polynomial search is performed.
Focused fixed-Claim reuse found the calibration and complete group definitions but no existing account of the displayed thirteen-prime ratio or the resulting all-late construction.
The common-direction and five-adic block materials are not logical inputs to this separate characteristic-two construction.

C655 T1 requires H in F_2[t], H(0)=1 and5deg H<5m-Q, where Q is a power of2 in(2m,5m).
It does NOT require the primitive support orders of H to be prime to3, or require H to be prime to1+t.
C652 N5 explicitly permits all odd complete orders other than5, with no coprimality-to3 restriction.
Thus W_3=1+t is permitted in this formal H domain.
The coprime-three representatives in C693 are an additional choice in another construction, not an extra H hypothesis here; C693 is not used as a dependency.
The present formal assertion is not an assertion that an actual C655 input with epsilon1 exists.
All original q, integer layers, canonical Y/U/R, full gate, zero-Haar, original-field and characteristic-zero residual requirements remain separate obligations.

<a id="large-dyadic-complete-h-statement"></a>
## Statement

Put phi(t)=1+t+t^2 and chi(t)=t phi(t)^2 over F_2.
Write varphi for Euler's totient, distinct from the polynomial phi.
Let ell:1+tF_2[[t]]->Z_2 be the C652 continuous multiplicative-to-additive character with ell(1+t)=1.
For positive odd d let B_d be the complete polynomial of traces of nonidentity d-th roots, with B_1=1; for odd d>1 let W_d be the complete primitive order-d trace polynomial.
Use chi_4(d)=(-1)^((d-1)/2), so the adopted calibration is

    B_d=product_(e|d,e>1)W_e,
    ell(B_d)=(1-chi_4(d)d)/4.

For every odd squarefree n>1, one has the exact ordinary integer character formula, viewed in Z_2,

    ell(W_n)=-(1/4)product_(p|n)(chi_4(p)p-1).           (LH1)

Take the fixed thirteen-prime set

    S={3,7,11,19,23,31,43,47,59,67,71,79,83},
    n=product_(p in S)p,
    A=(1/4)product_(p in S)(p+1),
    D=(1/2)product_(p in S)(p-1)=deg W_n.

Then n is odd squarefree,5 does not divide n, every p in S is3 modulo4, and

    ell(W_n)=A>0,
    A=357847875*2^34,
    A/D=71303168/27374347>5/2.                           (LH2)

For EVERY dyadic m=2^j with j>=70 define the ordinary nonnegative integers

    k_m=floor(m/(2A)), b_m=m/2-k_m A,
    H_m(t)=W_n(t)^(k_m) W_3(t)^(b_m), Q_m=4m.           (LH3)

The remainder satisfies0<=b_m<A, and this is an explicit monic finite complete-factor polynomial with constant term1.
It obeys

    ell(H_m)=m/2 exactly in Z_2,
    deg H_m=k_m D+b_m<m/5,
    2m<Q_m<5m, 5deg H_m<5m-Q_m=m.                       (LH4)

Thus C655's necessary epsilon1 congruence ell(H)=m/2 modulo2m and its complete H degree condition are simultaneously satisfied for every such m.
Moreover the corresponding FORMAL complement

    B_form,m(X)=X^(3m)H_m(chi(X))

is monic, prime to phi, has degree below4m, and is explicitly the complete product

    B_form,m=X^(3m) W_n^(k_m) W_(5n)^(k_m)
                         W_3^(b_m) W_15^(b_m).          (LH5)

Every displayed primitive order is odd and different from5.
The orders5n and15 in this last formula are allowed complete orders, not omitted fifth-order factors.
No actual normalized complement, canonical Y, finite-group membership of its full target, original maximal q, actual epsilon-layer, characteristic-zero P/T or residual realization is supplied by these formal statements.
No G0001 completion or negation of the original exclusions follows.

<a id="large-dyadic-complete-h-argument"></a>
<a id="argument"></a>
## Complete argument

### 1. Divisor inversion with its exact sign

Every B_d and W_d has constant term1, since a nonidentity odd-order root z cannot have trace0: z+z^(-1)=0 would imply z^2=1 and hence z=1 in characteristic2.
Complete primitive trace roots are stable under Frobenius, so their monic products lie in F_2[t].
Distinct inverse pairs give distinct traces by the quadratic equation z^2+tz+1=0.
This is the complete original trace-polynomial definition, not a choice of some irreducible factors within W_d.
In particular W_3=1+t, degree1 and character1.

For squarefree n, divisor inclusion-exclusion applied to ell(B_d)=sum_(e|d,e>1)ell(W_e) gives

    ell(W_n)=sum_(d|n)mu(n/d)ell(B_d).

To verify the inversion directly, the coefficient of a fixed ell(W_e) in this sum is sum_(e|d|n)mu(n/d), which is1 for e=n and0 otherwise by the expansion of(1-1)^a over the remaining prime divisors.
Also sum_(d|n)mu(n/d)=0 because n>1.
Substituting the adopted C652 calibration therefore gives

    ell(W_n)=-(1/4)sum_(d|n)mu(n/d)chi_4(d)d
            =-(1/4)product_(p|n)(chi_4(p)p-1).

The last equality is the finite expansion obtained by selecting whether each prime divides d; chi_4 is multiplicative on odd integers.
This proves LH1 without assigning a negative multiplicity to any constructed H.
The inclusion-exclusion only computes the additive character, whereas every exponent in LH3 is nonnegative.
All values ell(B_d) are ordinary integers under the calibration, so the equality lies in the embedded copy of Z in Z_2.

### 2. The exact finite prime certificate and complete trace degree

The thirteen displayed integers are distinct and all are3 modulo4: their respective values of(p-3)/4 are

    0,1,2,4,5,7,10,11,14,16,17,19,20.

All are odd and none is5 or divisible by5.
The entries3 and7 are prime directly.
If another entry were composite, it would have a prime divisor at most its square root, which is less than10 since every entry is at most83<100.
It therefore suffices to test2,3,5 and7.
Oddness excludes2 and the final digits exclude5.
For the entries11,19,23,31,43,47,59,67,71,79,83 the digit sums are respectively

    2,10,5,4,7,11,14,13,8,16,11,

none divisible by3, and their remainders modulo7 are

    4,5,2,3,1,5,3,4,1,2,6,

all nonzero.
This proves primality of every entry by an explicit hand certificate, with no prime table or native search.
Thus n is squarefree, odd and prime to5.
Each chi_4(p)=-1, and the number of factors is13, so LH1 gives

    ell(W_n)=-(1/4)(-1)^13 product_(p in S)(p+1)=A>0.

The primitive n-th roots are distinct, and inverse pairs have two elements because n is odd and greater than1.
The number of primitive n-th roots is varphi(n)=product_(p in S)(p-1), by the independent nonzero residue choices modulo these distinct primes.
The trace-pair argument above therefore gives deg W_n=varphi(n)/2=D, proving the exact degree in LH2.

### 3. Every factor in the ratio and a uniform positive degree margin

The complete hand factorizations are

| p | p-1 | p+1 |
| --- | --- | --- |
| 3 | 2 | 2^2 |
| 7 | 2*3 | 2^3 |
| 11 | 2*5 | 2^2*3 |
| 19 | 2*3^2 | 2^2*5 |
| 23 | 2*11 | 2^3*3 |
| 31 | 2*3*5 | 2^5 |
| 43 | 2*3*7 | 2^2*11 |
| 47 | 2*23 | 2^4*3 |
| 59 | 2*29 | 2^2*3*5 |
| 67 | 2*3*11 | 2^2*17 |
| 71 | 2*5*7 | 2^3*3^2 |
| 79 | 2*3*13 | 2^4*5 |
| 83 | 2*41 | 2^2*3*7 |

Multiplying the displayed prime powers gives

    product(p+1)=2^36*3^7*5^3*7*11*17,
    product(p-1)=2^13*3^7*5^3*7^2*11^2*13*23*29*41.

Their quotient is exactly

    2^23*17/(7*11*13*23*29*41)
      =142606336/27374347.

For transparent integer verification,7*11*13=1001,1001*23=23023,23023*29=667667 and667667*41=27374347, while2^23*17=142606336.
The quotient is reduced since the remaining numerator primes are2 and17 and neither divides the displayed denominator.
Its numerator exceeds five times its denominator by

    142606336-5*27374347=5734601>0.

Since A/D is HALF this quotient, A/D=71303168/27374347>5/2.
In particular the relevant positive margin is

    delta_deg=1/5-D/(2A)=5734601/713031680>1/128,          (LH6)

because128*5734601=734028928>713031680.
This delta_deg is a positive rational coefficient, not the original algebraic trace element delta in the C655 original-input domain.
Finally

    A=2^34*(3^7*5^3*7*11*17)
      =2^34*357847875<2^63,

where3^7*5^3=273375, multiplication by7,11,17 gives1913625,21049875,357847875, and357847875<2^29=536870912.
These exact comparisons provide the stated uniform threshold without an estimate based on floating point.

### 4. All sufficiently large dyadic targets are met with nonnegative multiplicities

Fix m=2^j with j>=70.
Its half m/2 is an ordinary positive integer.
Euclidean division by the positive integer A defines k_m and b_m exactly as in LH3 and gives k_m>=0 and0<=b_m<A.
The polynomial H_m is consequently a finite product of TWO allowed complete primitive trace polynomials at nonnegative integer multiplicities.
It is monic with H_m(0)=1.
Additivity of ell on products gives the exact equality

    ell(H_m)=k_m ell(W_n)+b_m ell(W_3)=k_m A+b_m=m/2.

Monicity and the exact factor degrees give deg H_m=k_mD+b_m.
Since k_m<=(m/2)/A and b_m<A,

    deg H_m < (D/(2A))m+A.

By LH6 and the upper bound for A,

    delta_deg*m > m/128 >=2^63>A.

It follows strictly that deg H_m<m/5, for EVERY dyadic m at or above2^70, proving LH4.
This bound deliberately does not assert that2^70 is the least possible threshold.
For dyadic m, Q_m=4m is a power of2 and lies strictly between2m and5m.
Then5m-Q_m=m, so the same inequality is exactly C655 T1's strict complement-degree inequality.
The exact character equality implies C655 T6 with epsilon1 modulo2m.
No actual epsilon is reassigned: this is formal compatibility with that specified necessary branch, not the construction of its original top layer.

### 5. Complete substituted factors, the admissibility of W_3, and the precise limit

For any odd d>1 prime to5, the exact complete-factor composition identity is

    W_d(chi(X))=W_d(X)W_(5d)(X).                         (LH7)

Indeed chi(z+z^(-1))=z^5+z^(-5).
The roots on the left correspond exactly to traces of roots of unity whose fifth powers have primitive order d.
The original order is either d or5d; conversely all primitive roots of both orders have primitive order d after fifth powering, since5 does not divide d.
The resulting two complete trace sets are disjoint and comprise all roots, and their total degree is varphi(d)/2+varphi(5d)/2=5varphi(d)/2, the full left degree.
Both sides are monic, which proves the identity including all complete factors and multiplicities.
This is consistent with the adopted B_(5d)=phi B_d(chi) identity and does not delete a required W_5 factor: W_5 never appears on either side when d>1.
Apply LH7 with d=n and d=3 to obtain LH5.
Because chi has degree5 and H_m is monic,

    deg B_form,m=3m+5deg H_m<4m.

At either root of phi, chi=0 and H_m(chi)=H_m(0)=1, while X is a unit; hence B_form,m is prime to phi.
Its order3 and order15 factors are permitted by C652's complete-product domain.
The mere fact that C693 can select certain representatives prime to3 does not impose that optional property on H or B_form,m here.

Only the H-character, whole-factor polynomial construction and strict degree conditions have been solved.
C655 also imposes an actual maximal q, actual integer layer data and epsilon, the same canonical Y/U/R, two full CRT conditions, corrected root and full gate, and characteristic-zero original polynomial/field/residual hypotheses.
They have neither been removed from an original-input theorem nor been supplied by this construction.
In particular ell(H_m)=m/2 is not being used as an unproved sufficiency criterion for complete membership of the entire Y target.
No actual P,T,G_can or zero-Haar residual example, no general inverse realization, and no unrestricted G0001 conclusion follows.
This exact family shows that the isolated necessary character and degree conditions cannot by themselves exclude all sufficiently large dyadic epsilon1 parameters.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision large-dyadic-formal-compatibility-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T01:30 |
| status | open |
| reason | Register the complete LH1--LH7 formal necessary-condition compatibility theorem. The squarefree divisor formula and an explicit thirteen-prime hand certificate give a positive character/degree ratio A/D=71303168/27374347>5/2. For every dyadic m>=2^70, nonnegative powers of whole W_n and W_3 give ell(H)=m/2 exactly and deg H<m/5, satisfying C655's epsilon1 necessary congruence and strict Q=4m degree condition. The substituted formal B also has a complete allowed factorization and degree below4m. All prime, sign, reduced-ratio and strict threshold calculations are retained, and the exact H domain permits W_3. Root and original_law are contributors; fresh isolated whole review remains required. No actual epsilon-layer, full target membership, canonical Y/q, original P/T, characteristic-zero residual realization or G0001 completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire formal construction](#large-dyadic-complete-h-statement) | LH1--LH5 with the fixed thirteen-prime n, every dyadic m>=2^70, all nonnegative exponents, exact positive character, strict degree and complete formal B factorization, with original-realization and necessary-only boundaries. |
| argument | [Complete hand argument](#large-dyadic-complete-h-argument) | All five sections and LH6--LH7: divisor inversion, ordinary integer sign, every prime test and factor, exact reduced ratio and uniform threshold, whole-factor construction, admissibility of W_3 and complete scope distinctions. |
| dependency | [Adopted calibrated character](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23) | Exact continuous character/additivity and ell(B_d)=(1-chi4(d)d)/4, full B/W definitions and allowed complete orders; no sufficiency for an entire target is imported. |
| dependency | [Adopted exact H and dyadic branch](Yin_C_G0655_v1.md#decision-whole-reviewed-2026-10-23) | Only T1's formal H/degree domain and T6's necessary epsilon1 character congruence at Q=4m, while every original layer/canonical/root/gate/field/residual hypothesis remains an unconstructed additional obligation. |
| dependency | [Complete primitive trace roots and divisors](Yin_C_G0608_v1.md#argument) | Complete primitive trace polynomials, disjoint inverse-pair root sets, constant terms and complete divisor partition only; no finite native certificate, A0=2 gate or all-order group sufficiency is a premise. |
| support | [Exact question and scope](#exact-question-inputs-and-scope) | The task is formal compatibility of selected necessary character/degree conditions, not an actual original-input construction; C693 is not a dependency and its optional coprime-three representative choice is not imposed on H. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T01:40 |
| status | proved |
| reason | Adopt the entire explicit large-dyadic complete-H construction after full main-agent reading and isolated whole R886. Exact divisor inversion, all thirteen prime and factor certificates, positive character/degree ratio, strict uniform threshold and nonnegative exponents establish ell(H)=m/2 and degH<m/5 for every dyadic m>=2^70. The complete substituted complement and permitted order3 factors are retained. This solves compatibility of the selected necessary conditions, not actual Y/q/layers, an original P/T or residual realization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire formal construction](#large-dyadic-complete-h-statement) | LH1--LH5 with the fixed thirteen-prime n, every dyadic m>=2^70, all nonnegative exponents, exact positive character, strict degree and complete formal B factorization, with original-realization and necessary-only boundaries. |
| argument | [Complete hand argument](#large-dyadic-complete-h-argument) | All five sections and LH6--LH7: divisor inversion, ordinary integer sign, every prime test and factor, exact reduced ratio and uniform threshold, whole-factor construction, admissibility of W_3 and complete scope distinctions. |
| dependency | [Adopted calibrated character](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23) | Exact continuous character/additivity and ell(B_d)=(1-chi4(d)d)/4, full B/W definitions and allowed complete orders; no sufficiency for an entire target is imported. |
| dependency | [Adopted exact H and dyadic branch](Yin_C_G0655_v1.md#decision-whole-reviewed-2026-10-23) | Only T1's formal H/degree domain and T6's necessary epsilon1 character congruence at Q=4m, while every original layer/canonical/root/gate/field/residual hypothesis remains an unconstructed additional obligation. |
| dependency | [Complete primitive trace roots and divisors](Yin_C_G0608_v1.md#argument) | Complete primitive trace polynomials, disjoint inverse-pair root sets, constant terms and complete divisor partition only; no finite native certificate, A0=2 gate or all-order group sufficiency is a premise. |
| support | [Exact question and scope](#exact-question-inputs-and-scope) | The task is formal compatibility of selected necessary character/degree conditions, not an actual original-input construction; C693 is not a dependency and its optional coprime-three representative choice is not imposed on H. |
| review | [Independent entire finding](../audits/reviews/Yin_R_G0886_v1.md#large-dyadic-complete-h-whole) | Whole LH1--LH7 and all five proof sections, exact source domains, every prime/character/ratio/threshold operation, complete substituted factors and necessary-only realization boundaries. |

