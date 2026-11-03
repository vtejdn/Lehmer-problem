---
author: Yin
---

# Nonnegative integral midpoint levels for the actual quartic

Contributor original_signed_asymptotic developed the complete NL1--NL5 author argument for Yin.
Root supplied the analytic assignment and read the whole draft before requesting this fixed candidate.
This candidate concerns the actual quartic P=t^4-t^3-t^2-t+1 and the complete original independent digit law (1,2,1)/4 only.
It begins from C300's exact signed two-integer identity, C204's actual two-real-strip core and C779's finite signed diagnostic.
No infinite-time lower bound or critical-mean branch is assumed.

## Statement

Fix P=t^4-t^3-t^2-t+1, its positive exterior root beta, a neutral conjugate zeta, and the actual original zero-to-zero core D in O=Z[beta].
The chronological state is X_(j+1)=beta X_j+eta_j, X_0=0, for independent original digits with probabilities1/4,1/2,1/4 at-1,0,1.
For n>=1 let E_(2n) and Pr_(2n) mean the complete law conditioned on X_(2n)=0, including every earlier zero visit and every original word representation.
Write rho(x)=|x(zeta)|, M_n=E_(2n)rho(X_n)^2, and x_+,x_- for the beta,beta^(-1) embeddings.
For the integer power-basis coordinates x=sum_(j=0)^3 a_j beta^j set s_l=sum_(j=0)^(3-l)a_j a_(j+l), A=s_0+s_2+3s_3 and K=-(s_1+s_2+s_3).
Then K is a nonnegative integer at EVERY x in D, and

    |rho(x)^2-sqrt13 K(x)|<(3+sqrt13)/2.

The quadratic form K is invariant under sign, multiplication by beta, and iota(beta)=beta^(-1), as an algebraic identity; no invariance of D under arbitrary beta powers is asserted.
The core set K=0 is finite, and its squared neutral radii belong to {0,1,2,3}, without asserting that all four values occur.

Put c_n(x)=4^n Pr(sum_(j<n)eta_j beta^j=x), Jx=beta^(-1)iota(x), W_(2n)=c_(2n)(0), and w_n(x)=c_n(x)c_n(Jx).
The genuine C300 integer numerator obeys

    mathcal_B_n=-sum_x w_n(x)K(x),
    -mathcal_B_n/W_(2n)=E_(2n)K(X_n)
                       =sum_(k>=1)Pr_(2n){K(X_n)>=k},
    |M_n-sqrt13 E_(2n)K(X_n)|<(3+sqrt13)/2.

In particular there are no positive endpoint summands in this numerator.
For EVERY n>=3 one furthermore has

    E_(2n)K(X_n)>=1/512,
    mathcal_B_n/W_(2n)<=-1/512,
    Pr_(2n){K(X_n)>=1}>=1/1024.

All of these bounds are for the COMPLETE original law.
Their constant scale does not imply positive limsup E_(2n)K(X_n)/n.
That latter unproved premise is equivalent to the original signed diffusive premise and, if proved, implies infinite critical mean by C285.
No actual critical-mean classification, R=beta or R<beta, varying-input uniform bound, or unrestricted G0001 conclusion is asserted.

## Complete argument

### Question and reuse

The current analytic target is a fixed epsilon>0 with mathcal_B_n<=-epsilon n W_(2n) along an unbounded sequence.
The [actual signed identity](Yin_C_G0300_v1.md#integer-midpoint-moment-diagnostic) and [complete finite profile interpretation](Yin_C_G0779_v1.md#direct-connection-to-the-existing-lower-moment-analytic-interface) retain its exact original meaning.
The [complete original block minorization](Yin_C_G0300_v1.md#returned-block-convolution-minorization) supplies all probability comparisons used below.
The [original moment discriminator](Yin_C_G0285_v1.md#diffusive-lower-moment-null-test) is reused only for the consequence of a genuinely proved positive linear limsup.
A targeted screen of these homes, C45, C324, C440, C622 and C673 found the existing small-support, arbitrary disjoint zero-return-block and packing obstructions; no conclusion here is an improvement of their all-time diffusion status.
The new point is that the C300 coefficient is nonpositive at EVERY actual core state, before averaging.
This follows by direct substitution and integrality from the already fixed formulas; no external theorem, numerical root calculation or new source is needed.

### Exact pointwise sign

Write u_+=(1+sqrt13)/2=beta+beta^(-1), u_-=(1-sqrt13)/2=zeta+zeta^(-1), and set

    B=1/(beta-1), S=beta B,
    C=BS=beta/(beta-1)^2=1/(u_+-2)=(3+sqrt13)/2<sqrt13.

The actual core D satisfies |x_+|<B and |x_-|<S.
For x=a0+a1 beta+a2 beta^2+a3 beta^3, put

    s_l=sum_(j=0)^(3-l) a_j a_(j+l),
    A(x)=s_0+s_2+3s_3,
    Bq(x)=s_1+s_2+s_3.

C300 proves rho(x)^2=A(x)+u_- Bq(x) and x_+x_-=A(x)+u_+ Bq(x).
Hence

    rho(x)^2=x_+x_- -sqrt13 Bq(x), |x_+x_-|<C.

If the integer Bq(x) were at least1, the right side would be strictly less than C-sqrt13<0.
This contradicts rho(x)^2>=0.
Thus

    K(x):=-Bq(x) is a nonnegative INTEGER for every x in D,
    rho(x)^2=sqrt13 K(x)+x_+x_-,
    |rho(x)^2-sqrt13 K(x)|<C.                         (NL1)

No sign of x_+x_- is assumed.
Outside D, K is an indefinite quadratic form and need not be nonnegative.
Multiplication by beta and the field involution iota(beta)=beta^(-1) preserve x iota(x), so uniqueness of its expression A+u_+ Bq proves that K is invariant under these operations wherever the resulting arguments are considered.
This algebraic invariance does not assert that D is invariant under arbitrary beta powers.
Sign reversal also preserves K.
The set K=0 in D is finite because NL1 bounds its neutral radius by sqrt(C) while both real embeddings are bounded.
More specifically A(x)=rho(x)^2 is then an integer in {0,1,2,3}; no classification of which such core states occur is made.

### Actual positive level count

With the complete original midpoint weights w_n(x)=c_n(x)c_n(Jx), W=W_(2n)=sum_x w_n(x), C300's genuine signed numerator is exactly

    mathcal_B_n=-sum_x w_n(x)K(x),
    -mathcal_B_n/W=E_(2n) K(X_n)
                     =sum_(k>=1) Pr_(2n){K(X_n)>=k}.     (NL2)

Every sum is finite at each n.
There are no positive summands cancelling negative summands in mathcal_B_n for this actual quartic/core.
Thus the remaining target is genuinely linear growth of a NONNEGATIVE integral level count, not control of cancellation between endpoint signs.
In particular

    |M_n-sqrt13 E_(2n)K(X_n)|<C.                         (NL3)

The positivity and bounded error do not establish such growth.
A law with bounded level expectation is compatible with NL1--NL3.

### Complete length-six seed and paid all-time floors

Every returned word of length6 is E=(a+bt)P with a,b integers.
Its coefficients in increasing order are

    (a,b-a,-a-b,-a-b,a-b,b).

The coefficient restriction {-1,0,1} forces a,b in {-1,0,1}; when both are nonzero, either |a+b|=2 or |a-b|=2.
Consequently the five and only five legal words are0,+P,-P,+tP,-tP.
The zero word has original probability1/64, and each other word has original probability1/2048.
Their total is p_6=9/512.
At midpoint3, the two positive representatives have states

    a_*=beta-1, b_*=beta^(-2)(beta-1).

Indeed the midpoint convention is -beta^(-3) times the first three low coefficients.
For a_*, Bq=-1; invariance under beta powers gives K(b_*)=K(a_*)=1.
Their negatives have the same level.
The returned length-six law therefore assigns probability8/9 to0 and1/36 to each of +a_*,-a_*,+b_*,-b_*, giving E K=1/9.

For n>=3 choose the centered length-six digit block and keep the event that this block and its full complement each return separately.
By C300, its conditional mass q inside the entire length2n original return is at least p_6=9/512.
On this event the midpoint is Z+U, where U has the just described length-six midpoint law and Z has the symmetric complementary returned law, independently.
Both component laws are supported in D: filling the other coordinate block with zero digits gives a legal complete original return word.
Every possible sum Z+U is also in D because it is a complete returned word.
Since K is quadratic and U is centered, for each such fixed z,

    E_U K(z+U)=K(z)+E K(U)>=1/9.

Outside the subevent K is nonnegative by NL1.
It follows for EVERY n>=3 that

    E_(2n)K(X_n)>=1/512,
    mathcal_B_n/W_(2n)<=-1/512.                         (NL4)

There is also an actual level-probability floor.
For either a=a_* or a=b_* the quadratic parallelogram identity gives

    K(z+a)+K(z-a)=2K(z)+2>=2.

Both summands are nonnegative integers at these actual core states, so at least one is at least1.
Each sign pair has original conditional weight1/18 and contributes at least1/36 to the event K>=1.
The two sign pairs together give conditional probability at least1/18, and hence

    Pr_(2n){K(X_n)>=1}>=1/1024 for EVERY n>=3.          (NL5)

All block probabilities and both real neutral coordinates remain included.
Neither NL4 nor NL5 grows with n.
They therefore do not prove the positive linear limsup needed by C285 or classify the true critical mean.

### Remaining analytic gate

A sufficient and equivalent signed-moment premise is limsup E_(2n)K(X_n)/n>0.
Equivalently, the positive tail sum in NL2 must have linear size along an unbounded sequence.
A sufficient stronger form is fixed a,delta>0 with Pr_(2n){K(X_n)>=a n}>=delta along such a sequence.
The bounded-error identity NL3 transfers that premise to C285's genuine diffusive lower moment.
No such unbounded-sequence premise is supplied here.
The complete finite C819/C779 values remain finite data, and the original C324/C45/C703 comparison costs remain effective.

This fixed candidate contains author mathematics only, without independent review or adoption.
No J program or numerical experiment was needed.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision nonnegative-level-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T10:01 |
| status | open |
| reason | Fix the complete NL1--NL5 author proof: actual quartic whole-core pointwise coefficient sign, nonnegative integral level and exact complete signed/tail identity, finite zero level, algebraic invariances, complete five-word length-six seed and original-probability all-n floors. Independent whole review remains outstanding. The constant floors do not establish linear growth or classify the critical mean. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire nonnegative level statement](#statement) | Actual fixed quartic, complete original digit/bridge law, every core state, exact integer sign and level identities, full n>=3 moment/probability floors, and every unproved asymptotic boundary. |
| argument | [Entire NL1--NL5 proof](#complete-argument) | Exact BS radical calculation and integrality, quadratic invariances and finite zero level, complete original count/tail identity, full length-six word classification and weights, actual centered-block probability, conditional symmetry and parallelogram probability argument, unchanged missing linear-growth premise. |
| dependency | [Actual signed identity and original block law](Yin_C_G0300_v1.md#decision-complete-retained-proof-adoption) | Exact quartic two-integer identities and midpoint reciprocal-fiber factorization; complete original centered-block submeasure with all probabilities and symmetric complementary returned law. No diffusive lower bound is borrowed. |
| dependency | [Actual core and complete midpoint interface](Yin_C_G0204_v1.md#decision-sufficient-covariance-home) | Actual strict two-real-strip bounds and complete original chronological core/midpoint interpretation; bounded full embedding regions contain finitely many actual order elements. No finite-mean hypothesis is imposed. |
| dependency | [Actual diffusive implication](Yin_C_G0285_v1.md#decision-sufficient-projection-home) | Only the already adopted implication from a genuinely positive limsup M_n/n to infinite critical mean; its premise remains unproved here. |
| support | [Finite signed diagnostic](Yin_C_G0779_v1.md#statement) | Comparison and exact notation of the existing finite data only; no finite value is used to prove NL1--NL5 or an unbounded-sequence premise. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T10:12 |
| status | proved |
| reason | Root read the entire fixed NL1--NL5 statement/proof and whole independent R1000 and adopts the actual-core nonnegative integral level, exact original signed/tail identities and all-n constant floors without substantive repair. The independent exact seed enumeration corroborates the complete proof. No linear level growth, critical-mean branch, radius equality/strictness or unrestricted Task result is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire nonnegative level statement](#statement) | Actual fixed quartic, complete original digit/bridge law, every core state, exact integer sign and level identities, full n>=3 moment/probability floors, and every unproved asymptotic boundary. |
| argument | [Entire NL1--NL5 proof](#complete-argument) | Exact BS radical calculation and integrality, quadratic invariances and finite zero level, complete original count/tail identity, full length-six word classification and weights, actual centered-block probability, conditional symmetry and parallelogram probability argument, unchanged missing linear-growth premise. |
| dependency | [Actual signed identity and original block law](Yin_C_G0300_v1.md#decision-complete-retained-proof-adoption) | Exact quartic two-integer identities and midpoint reciprocal-fiber factorization; complete original centered-block submeasure with all probabilities and symmetric complementary returned law. No diffusive lower bound is borrowed. |
| dependency | [Actual core and complete midpoint interface](Yin_C_G0204_v1.md#decision-sufficient-covariance-home) | Actual strict two-real-strip bounds and complete original chronological core/midpoint interpretation; bounded full embedding regions contain finitely many actual order elements. No finite-mean hypothesis is imposed. |
| dependency | [Actual diffusive implication](Yin_C_G0285_v1.md#decision-sufficient-projection-home) | Only the already adopted implication from a genuinely positive limsup M_n/n to infinite critical mean; its premise remains unproved here. |
| support | [Finite signed diagnostic](Yin_C_G0779_v1.md#statement) | Comparison and exact notation of the existing finite data only; no finite value is used to prove NL1--NL5 or an unbounded-sequence premise. |
| review | [Independent whole nonnegative-level finding](../audits/reviews/Yin_R_G1000_v1.md#whole-nonnegative-level-finding) | Entire statement and NL1--NL5, exact pointwise sign and invariances, full original midpoint count/tail identities, complete length-six law and genuine centered-block mass, all-n floors and all conditional boundaries. |

