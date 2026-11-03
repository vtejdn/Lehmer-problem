---
author: Yin
---

# Strict original quartic return radius above 1711 over 1000

Human author Yin.
Root developed this exact arithmetic consequence of the newly adopted complete p512 and the already adopted full seven-state overlap envelope.
C788 retains the complete rational parameter majorants and the earlier p256 application; this proof extends only the finite arithmetic input and pays the entire later dyadic tail again.
No return graph beyond the adopted time512 calculation or asymptotic fit is used.
This fixed candidate is initially open for independent whole review.

## Statement

For the ACTUAL quartic P(t)=t^4-t^3-t^2-t+1, its exterior root beta and complete original iid digit probabilities1/4,1/2,1/4, the true exponential return radius R and h_2(beta)=logR satisfy

    R>1711/1000,
    h_2(beta)>log(1711/1000),
    1711/1000<R<=beta<1723/1000.

This strengthens the adopted lower endpoint1699/1000 at the SAME fixed input and law.
No equality R=beta, strict R<beta, critical-mean branch, positive linear midpoint moment, varying-input uniform estimate or unrestricted G0001 result is asserted.

## Complete argument

### NR1. Extend the exact rational envelope table

Use the SAME exact G(n) of adopted C786 v2 and the proved positive parameter majorants of C788 RB1.
In particular, for h^+=n/2+2/3 and any positive rational u with u^2>(22/7)h^+,

    G(n)<G^+(n)
      =28(238/81)+[28(31/9)(5/18)]u
                                  +[28(22/7)(19/25)/13]h^+.

This follows from the already proved actual beta bracket, bounds a<14/9,b<17/9,s<19/25,kappa<2/3 and exact pi integral in C788.
Those inequalities concern fixed input parameters and apply at EVERY positive n, not only the old table indices.
The entries at512 and1024 are the same as C788; the new2048 entry is an application of the all-n analytic envelope, not a newly observed return.

| n | h^+ | u | u^2-(22/7)h^+ | G^+(n) | Strict integer upper bound |
| ---: | --- | --- | --- | --- | ---: |
|512|770/3|14201/500|5203/750000|113914381/52650|2164|
|1024|1538/3|40141/1000|1297501/21000000|399626849/105300|3796|
|2048|3074/3|56749/1000|1429021/21000000|723842753/105300|6875|

Every square margin is positive.
The integer-minus-G^+ margins are respectively20219/52650,91951/105300 and94747/105300, all positive.
Hence G(512)<2164,G(1024)<3796 andG(2048)<6875 strictly.
All entries use exact integer or rational arithmetic with no floating-point decision.

### NR2. Complete infinite tail at the new base time

Put H_n=-log(R^n p_n).
C786 v2's exact full dyadic identity gives

    H_512=(1/2)log D_512+(1/4)log D_1024+(1/4)H_2048,
    D_n<=G(n), H_n<=log(2G(n)).

Therefore

    H_512<(1/2)log2164+(1/4)log3796
                                      +(1/4)log13750,
    R^512 p512>C_*^(-1/4),
    C_*=2164^2*3796*13750=244423756720000.             (NR1)

The term involving H_2048 controls every unobserved later dyadic scale through the all-n theorem.
No p1024,p2048 or p4096 is computed or used as an observed value.
The exact finite input needed in the next step is only p512.

### NR3. Accepted complete p512 and a strict integer certificate

Adopted C793, independently reproduced in whole R1012, gives the COMPLETE original probability

    p512=N/2^1019,
    N=5298548391970129745344684892772394289057669827956111368871272718708030755799876567240009996275901111428878134985202079634126536883620984644784010837788567749143910392852997044503323399.

It includes every original returned word through512, with the declared height95, original weights and complete statewise checks; no scope extension is made by this scalar reuse.
Exact arbitrary-precision integer arithmetic gives

    C_* p512^4 (1711/1000)^2048 <97/100<1,             (NR2)

or equivalently

    100 C_* N^4 1711^2048
                    <97 *2^4076 *1000^2048.

The exponent4076 is4*1019.
The complete decisive arithmetic certificate is reproducible as

```python
N = 5298548391970129745344684892772394289057669827956111368871272718708030755799876567240009996275901111428878134985202079634126536883620984644784010837788567749143910392852997044503323399
C = 2164**2 * 3796 * 13750
assert C == 244423756720000
assert 100*C*N**4*1711**2048 < 97*2**4076*1000**2048
```

Positive fourth roots in NR2 give

    (1711/1000)^512 p512<C_*^(-1/4).

Comparing with NR1 and cancelling the strictly positive p512 proves R>1711/1000.
The entropy inequality follows by strict monotonicity of log.
The existing same-law R<=beta and actual beta<1723/1000 give the full stated interval.
This proof makes no inference about the derivative g'(R), the critical mean or unrestricted Mahler measure.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision radius-1711-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T12:29 |
| status | open |
| reason | Fix the exact stronger original-quartic lower-radius candidate1711/1000 using the newly adopted completep512, existing rational parameter bounds, full analytic dyadic tail and strict integer certificate. Independent whole mathematical/arithmetic review remains outstanding. No later return calculation, equality/strict upper-radius comparison, mean branch or unrestricted Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Strict actual original radius above1711/1000](#statement) | Same fixed quartic/full original law, true radius and entropy, strict rational endpoint with accepted upper interval and all exclusions. |
| argument | [Complete NR1--NR3](#complete-argument) | Exact all-n rational majorants and three table entries, complete infinite dyadic split, acceptedp512 scalar and independent-checkable integer certificate, strict comparison and scope boundaries. |
| dependency | [Adopted complete seven-state envelope](Yin_C_G0786_v2.md#decision-whole-reviewed-2026-10-26) | Same actual G(n), all-n original D_n, exact true-radius dyadic identity and full analytic normalized-return bound. |
| dependency | [Adopted rational parameter majorants](Yin_C_G0788_v1.md#decision-whole-reviewed-2026-10-26) | RB1's fixed beta/s/radical/pi bounds and G^+ formula, repeated512/1024 table entries, same-law entropy/upper-interval conventions; its earlier1699 lower endpoint is comparison only. |
| dependency | [Adopted complete original p512](Yin_C_G0793_v1.md#decision-whole-reviewed-2026-10-26) | Only exactp512=N/2^1019 at the full original time512/height95 scope; no midpoint lower-growth inference. |
| support | [Independent complete native evidence](../audits/reviews/Yin_R_G1012_v1.md#whole-finite-finding) | Existing full independent reproduction and statewise payload validation for the adoptedp512 input, reused without another graph run. |
| dependency | [Accepted true upper-radius interface](Yin_C_G0526_v1.md#statement) | Same original quartic R<=beta, without a critical-mean branch or equality assertion. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T12:40 |
| status | proved |
| reason | Root read the complete fixed NR1--NR3 and whole independent R1014 and adopts strictR>1711/1000 at the same actual original quartic law without substantive repair. The existing exactp512, three rational analytic bounds, entire paid dyadic tail and independently recomputed integer margin retain all native and infinite-time scopes. No radius equality/strict upper comparison, critical-mean branch, linear midpoint lower bound or unrestricted Task conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Strict actual original radius above1711/1000](#statement) | Same fixed quartic/full original law, true radius and entropy, strict rational endpoint with accepted upper interval and all exclusions. |
| argument | [Complete NR1--NR3](#complete-argument) | Exact all-n rational majorants and three table entries, complete infinite dyadic split, acceptedp512 scalar and independent-checkable integer certificate, strict comparison and scope boundaries. |
| dependency | [Adopted complete seven-state envelope](Yin_C_G0786_v2.md#decision-whole-reviewed-2026-10-26) | Same actual G(n), all-n original D_n, exact true-radius dyadic identity and full analytic normalized-return bound. |
| dependency | [Adopted rational parameter majorants](Yin_C_G0788_v1.md#decision-whole-reviewed-2026-10-26) | RB1's fixed beta/s/radical/pi bounds and G^+ formula, repeated512/1024 table entries, same-law entropy/upper-interval conventions; its earlier1699 lower endpoint is comparison only. |
| dependency | [Adopted complete original p512](Yin_C_G0793_v1.md#decision-whole-reviewed-2026-10-26) | Only exactp512=N/2^1019 at the full original time512/height95 scope; no midpoint lower-growth inference. |
| support | [Independent complete native evidence](../audits/reviews/Yin_R_G1012_v1.md#whole-finite-finding) | Existing full independent reproduction and statewise payload validation for the adoptedp512 input, reused without another graph run. |
| dependency | [Accepted true upper-radius interface](Yin_C_G0526_v1.md#statement) | Same original quartic R<=beta, without a critical-mean branch or equality assertion. |
| review | [Independent whole radius-1711 finding](../audits/reviews/Yin_R_G1014_v1.md#radius-1711-whole-finding) | Entire statement and NR1--NR3, all three exact rational bounds and new2048 arithmetic, complete infinite dyadic tail, exact adoptedp512 scalar and independent integer certificate, strict true-radius conclusion and every limit. |

