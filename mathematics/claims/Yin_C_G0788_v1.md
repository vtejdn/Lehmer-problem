---
author: Yin
---

# A strict original quartic return-radius bound of 1699 over 1000

Human author Yin.
Root developed this exact finite arithmetic consequence of the adopted seven-state envelope and the already independently checked complete p256.
No new return graph, longer return computation, altered law or empirical extrapolation is used.
Every unobserved return scale is bounded by the full analytic theorem.
This fixed candidate is initially open for independent whole mathematical and arithmetic review.

## Statement

For the ACTUAL quartic P(t)=t^4-t^3-t^2-t+1 and complete original independent digit law with probabilities1/4,1/2,1/4, let R be its true exponential return radius and h_2(beta)=log R as in adopted C776.
Then

    R>1699/1000,
    h_2(beta)>log(1699/1000),
    1699/1000<R<=beta<1723/1000.

The earlier C776 bound R>1687/1000 remains valid and is strengthened at this same fixed input.
No equality R=beta, strict R<beta, critical-mean classification, positive linear midpoint moment, varying-input uniform bound or unrestricted G0001 conclusion is supplied.
The proof consumes only the existing exact p256 and the whole all-n envelope of adopted C786 v2.

## Complete argument

### RB1. Explicit rational majorants for the complete envelope

Use C786 v2's exact notation

    s=|Im zeta|=sqrt((1+sqrt13)/8), kappa=1/(2s),
    B=1/(beta-1), S=beta B,
    d1=B+S, d2=beta S+B/beta,
    a=d1/sqrt13+1/2, b=d2/sqrt13+1/2,
    h_n=n/2+kappa,
    G(n)=28ab+[28(a+b)/sqrt13]sqrt(pi h_n)
                                  +[28pi s/13]h_n.

All these are the same original quartic parameters, not independently adjustable variables.
The accepted exact root interval861/500<beta<1723/1000 gives

    B<500/361, S<861/361,
    d1<1361/361<19/5,
    d2<(1723/1000)(861/361)+(500/361)(500/861)<5.

The last inequality is an exact rational comparison.
Also18/5<sqrt13<361/100 gives

    3/4<s<19/25, kappa<2/3,
    a<14/9, b<17/9,
    ab<238/81, a+b<31/9.

For the lower s inequality it suffices that sqrt13>7/2; the upper follows from461/800<361/625.
Each square-root comparison is therefore certified by positive rational squares.
Use the elementary strict bound pi<22/7, which follows directly from

    22/7-pi=integral_0^1 x^4(1-x)^4/(1+x^2) dx>0.

Polynomial division gives integrand x^6-4x^5+5x^4-4x^2+4-4/(1+x^2), verifying the displayed evaluation.
No numerical approximation of pi is needed.

For n in{256,512,1024}, put h^+=n/2+2/3 and choose the following exact positive rational u_n with u_n^2>(22/7)h^+.
Then

    G(n)<G^+(n)
      :=28(238/81)+[28(31/9)(5/18)]u_n
                                  +[28(22/7)(19/25)/13]h^+.

All directions are strict because every coefficient and argument is positive.
The complete rational table is

| n | h^+ | u_n | u_n^2-(22/7)h^+ | G^+(n) | Integer upper bound |
| ---: | --- | --- | --- | --- | ---: |
|256|386/3|2011/100|6541/210000|67547923/52650|1283|
|512|770/3|14201/500|5203/750000|113914381/52650|2164|
|1024|1538/3|40141/1000|1297501/21000000|399626849/105300|3796|

Every square margin is positive, and each G^+ fraction is strictly below its final integer.
Thus these are rigorously paid bounds on the COMPLETE overlap at those scales even though no p512,p1024 or p2048 is computed here.

### RB2. Pay the entire infinite dyadic tail

Put a_n=R^n p_n and H_n=-log a_n.
The adopted C786 v2 conclusion, based on the exact C555 identity, gives

    H_n=sum_(j>=0)2^(-j-1)log D_(2^j n),
    D_m<=G(m), H_m<=log(2G(m)).

Split this exact infinite sum after its first two terms, at n=256:

    H_256=(1/2)log D_256+(1/4)log D_512+(1/4)H_1024.

RB1 and the all-n H bound therefore imply

    H_256<(1/2)log1283+(1/4)log2164
                                      +(1/4)log7592,
    R^256 p256>C_*^(-1/4),
    C_*=1283^2 *2164*7592=27043741036832.             (RB1)

The last term controls ALL later dyadic scales through the proved all-n envelope.
No later return value, finite truncation equality or identity R=beta enters this step.

### RB3. Exact existing return input and integer certificate

Adopted C776 gives the COMPLETE original value

    p256=N/2^504,
    N=264543412341747108848944040326875358997077741567393090275411759418849446982212078897310231.

Its height48 completeness and original integer weights were independently inspected in R996; this proof reuses precisely that accepted exact value and does not rerun or enlarge its graph.
An exact integer comparison gives

    C_* p256^4 (1699/1000)^1024 <19/20<1.             (RB2)

Equivalently, with no logarithm or rounding decision,

    20 C_* N^4 1699^1024
                    <19 *2^2016 *1000^1024.

This comparison and the preceding finite rational table can be reproduced with integer arithmetic.
For the final comparison alone:

```python
N = 264543412341747108848944040326875358997077741567393090275411759418849446982212078897310231
C = 1283**2 * 2164 * 7592
assert C == 27043741036832
assert 20*C*N**4*1699**1024 < 19*2**2016*1000**1024
```

The arithmetic is a finite exact certificate; no floating-point sign or sampled asymptotic fit is a premise.
Taking positive fourth roots in RB2 gives

    (1699/1000)^256 p256<C_*^(-1/4).

Combine this with RB1 and cancel p256>0 to obtain R>1699/1000.
The logarithmic assertion follows because log is strictly increasing on positive reals.
The accepted upper bound R<=beta and root bound beta<1723/1000 give the displayed final interval.
This strengthens only the lower bound for the same true original quartic radius.
It estimates neither the derivative g'(R) of C785 nor the critical mean, and it supplies no unrestricted Mahler bound.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision radius-1699-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T11:10 |
| status | open |
| reason | Fix the exact finite arithmetic consequence R>1699/1000 using the adopted seven-state full overlap envelope and the previously checked complete p256. Three rational envelope bounds, an analytically paid infinite dyadic tail and an exact integer margin establish the candidate. Independent whole review is outstanding; no new return graph, radius equality, mean branch or unrestricted Task result is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Strict actual original radius bound](#statement) | Same fixed quartic and complete original law, true R and entropy, exact1699/1000 lower endpoint with accepted upper endpoint, and all exclusions. |
| argument | [Complete rational and infinite-tail proof](#complete-argument) | RB1--RB3 exact parameter bounds and pi integral, all rational table entries, complete dyadic split, exact existing p256, integer certificate and strict comparison. |
| dependency | [Adopted seven-state complete envelope](Yin_C_G0786_v2.md#decision-whole-reviewed-2026-10-26) | Exact same-quartic G(n), original D_n, full true-radius dyadic identity and all-n normalized lower bound; no finite-to-infinite extrapolation or lower-moment premise. |
| dependency | [Adopted exact original return and root scope](Yin_C_G0776_v1.md#decision-whole-reviewed-2026-10-26) | Complete original p256=N/2^504 and accepted exact861/500<beta<1723/1000, true R<=beta and h2=logR; no new native execution or mean conclusion. |
| support | [Whole original midpoint/native review](../audits/reviews/Yin_R_G0996_v1.md#complete-midpoint-native-and-radius) | Existing independent evidence for p256 and its full original height48/time256 scope, reused as accepted input without a new graph run. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T11:17 |
| status | proved |
| reason | Root read the complete fixed RB1--RB3 and whole independent mathematical/arithmetic R1007 and adopts strict R>1699/1000 for the same actual quartic original law without substantive repair. The exact rational envelope table, analytically paid infinite tail and independently recomputed integer margin retain the existing complete p256 scope. No graph enlargement, radius equality/strict upper comparison, critical-mean branch or unrestricted Task result is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Strict actual original radius bound](#statement) | Same fixed quartic and complete original law, true R and entropy, exact1699/1000 lower endpoint with accepted upper endpoint, and all exclusions. |
| argument | [Complete rational and infinite-tail proof](#complete-argument) | RB1--RB3 exact parameter bounds and pi integral, all rational table entries, complete dyadic split, exact existing p256, integer certificate and strict comparison. |
| dependency | [Adopted seven-state complete envelope](Yin_C_G0786_v2.md#decision-whole-reviewed-2026-10-26) | Exact same-quartic G(n), original D_n, full true-radius dyadic identity and all-n normalized lower bound; no finite-to-infinite extrapolation or lower-moment premise. |
| dependency | [Adopted exact original return and root scope](Yin_C_G0776_v1.md#decision-whole-reviewed-2026-10-26) | Complete original p256=N/2^504 and accepted exact861/500<beta<1723/1000, true R<=beta and h2=logR; no new native execution or mean conclusion. |
| support | [Whole original midpoint/native review](../audits/reviews/Yin_R_G0996_v1.md#complete-midpoint-native-and-radius) | Existing independent evidence for p256 and its full original height48/time256 scope, reused as accepted input without a new graph run. |
| dependency | [Accepted original upper-radius interface](Yin_C_G0526_v1.md#statement) | Only the same fixed original-law R<=beta interface already selected by C776 and expressly inspected in R1007; no critical-mean classification. |
| review | [Independent whole strict-radius finding](../audits/reviews/Yin_R_G1007_v1.md#radius-1699-whole-finding) | Entire statement and RB1--RB3, all rational majorants and exact table, complete infinite dyadic tail, exact p256 matching and independent integer certificate, strict true-radius comparison and retained limits. |

