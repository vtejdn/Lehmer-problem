---
author: Yin
---

# Independent whole review of the strict original quartic radius bound 1699 over 1000

The review act is dated 2026-10-26T11:14, with Yin as the human record author.
A separately assigned reviewer outside substantive proof development read the entire fixed [C788 v1 Statement](../../claims/Yin_C_G0788_v1.md#statement) and [Complete argument](../../claims/Yin_C_G0788_v1.md#complete-argument) before consulting the necessary exact inputs.
The initial target decision is [radius-1699-open](../../claims/Yin_C_G0788_v1.md#decision-radius-1699-open).
No proposing calculation dialogue, author explanation outside the fixed proof, mutable draft, persistent memory or prior review conclusion about C788 was supplied or consulted.
The reviewer had previously performed the independent whole inspection of C786 v2 retained in [R1006](Yin_R_G1006_v1.md#whole-seven-state-finding); that existing background is reused openly at its exact unchanged scope.
The new C786 adoption decision was checked, and the C776 input and its expressly selected [R996 finding](Yin_R_G0996_v1.md#complete-midpoint-native-and-radius) were read as accepted finite-input evidence after reading C788.

The whole reviewer independently recomputed every finite rational table entry and the final large-integer certificate with standard-library exact rational/integer arithmetic and checked the entire analytic deduction.
A separately isolated read-only helper also read the fixed whole C788 proof and independently checked its parameter majorants, pi identity, complete rational table and integer certificate.
Its bounded findings agreed with the whole review and supplied no proof repair.
Neither reviewer developed C788's proof or reran the original return graph.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole strict-radius finding](#radius-1699-whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole strict-radius finding](#radius-1699-whole-finding) | [C788 entire statement](../../claims/Yin_C_G0788_v1.md#statement) | Actual quartic and complete original digit law, true R and entropy, strict R>1699/1000, accepted upper endpoint and every exclusion. |
| [Whole strict-radius finding](#radius-1699-whole-finding) | [C788 complete argument](../../claims/Yin_C_G0788_v1.md#complete-argument) | All RB1--RB3 parameter inequalities, root/square bounds, pi integral, exact table, complete infinite dyadic split, inherited p256, independently recomputed integer certificate and strict final comparison. |
| [Whole strict-radius finding](#radius-1699-whole-finding) | [C786 v2 adopted envelope](../../claims/Yin_C_G0786_v2.md#decision-whole-reviewed-2026-10-26) | Same original complete D_n, exact G(n), true-radius dyadic identity and all-n H_n<=log(2G(n)); prior independent R1006 coverage is reused at this unchanged scope. |
| [Whole strict-radius finding](#radius-1699-whole-finding) | [C776 adopted exact input](../../claims/Yin_C_G0776_v1.md#decision-whole-reviewed-2026-10-26) | Exact complete p256=N/2^504, same original law and true R, exact exterior-root interval, h_2(beta)=log R and accepted R<=beta; no new graph or source-proof audit. |
| [Whole strict-radius finding](#radius-1699-whole-finding) | [R996 accepted native finding](Yin_R_G0996_v1.md#complete-midpoint-native-and-radius) | Existing independent evidence for C776's full height48/time256 original weighted return input; reused rather than relabelled as a new native reproduction. |
| [Whole strict-radius finding](#radius-1699-whole-finding) | [C526 upper-radius statement](../../claims/Yin_C_G0526_v1.md#statement) | Narrow same-quartic R<=beta interface already selected by C776, without importing a mean classification or equality R=beta. |

<a id="radius-1699-whole-finding"></a>
## Whole finding

No mathematical or arithmetic defect was found in the complete fixed C788 statement and proof.
The following checks support the strict true-radius conclusion without substantive repair.

### Rational majorants and exact pi bound

The original C786 parameters match exactly, including kappa=1/|1-zeta^2|=1/(2s).
For beta>1, B=1/(beta-1) and S=1+B decrease, so beta>861/500 gives B<500/361 and S<861/361.
Combining the upper beta bound with these positive upper bounds gives the displayed upper estimate for d2.
Exact independent arithmetic yields

    19/5-1361/361 = 54/1805 > 0,
    (1723/1000)(861/361)+(500/361)(500/861)
        = 1527296083/310821000
        = 5-26808917/310821000 < 5.

The root interval itself was additionally verified without numerical approximation:

    P(861/500)=-37115459/62500000000 < 0,
    P(1723/1000)=6502808441/1000000000000 > 0.

The trace formula P(t)/t^2=(t+t^-1)^2-(t+t^-1)-3 is strictly increasing on t>1 and has the actual exterior root as its unique zero there.
These signs therefore have the required root-bound direction.

The positive square comparisons are

    13-(18/5)^2=1/25,
    (361/100)^2-13=321/10000,
    (19/25)^2-461/800=27/20000.

Also sqrt13>7/2 gives s^2>9/16.
Consequently 3/4<s<19/25 and kappa<2/3 are strict.
Substituting d1<19/5, d2<5 and sqrt13>18/5 gives a<14/9 and b<17/9, hence the positive bounds ab<238/81 and a+b<31/9.
All reciprocal and product inequalities have the displayed directions.

The pi integrand division was checked by exact polynomial multiplication:

    (1+x^2)(x^6-4x^5+5x^4-4x^2+4)-4
        = x^4(1-x)^4.

The polynomial part integrates to 1/7-4/6+5/5-4/3+4=22/7, while 4 integral_0^1 (1+x^2)^-1 dx=pi.
The numerator is strictly positive throughout 0<x<1, so the integral proves pi<22/7 strictly.
This is the explicit elementary calculation in the proof, with no numerical pi estimate or new external theorem premise.

### Complete rational envelope table

For each n, h_n<h^+=n/2+2/3, and the positive square margin proves sqrt(pi h_n)<u_n.
Every coefficient used to form G^+ is positive and bounds the corresponding original coefficient from above.
Thus the substitution proves G(n)<G^+(n), rather than merely an approximate numerical comparison.
The whole reviewer recomputed the following exact values directly from the formula for G^+ using fractions.Fraction.
The separately isolated arithmetic check agreed.

| n | h^+ | Exact u_n^2-(22/7)h^+ | Recomputed G^+(n) | Exact integer-upper-bound minus G^+(n) |
| ---: | --- | --- | --- | --- |
| 256 | 386/3 | 6541/210000 | 67547923/52650 | 2027/52650 |
| 512 | 770/3 | 5203/750000 | 113914381/52650 | 20219/52650 |
| 1024 | 1538/3 | 1297501/21000000 | 399626849/105300 | 91951/105300 |

All six margins are positive.
This proves the three strict complete-envelope bounds G(256)<1283, G(512)<2164 and G(1024)<3796.
The indices label applications of the all-n analytic theorem, not newly computed return probabilities.

### Complete infinite dyadic split

C786 v2 supplies the same original D_m and true R, with H_n=-log(R^n p_n), the convergent nonnegative dyadic expansion and H_m<=log(2G(m)) for every m>=1.
Reindexing the terms j>=2 gives exactly

    H_256=(1/2)log D_256+(1/4)log D_512+(1/4)H_1024.

The factor 1/4 in front of H_1024 is correct.
The strict table bounds, D_m<=G(m), and H_1024<=log(2G(1024)) give the displayed strict upper bound for H_256.
Multiplication of that bound by four gives the exponent bookkeeping

    C_*=1283^2*2164*7592=27043741036832,
    R^256 p256>C_*^(-1/4).

The last term accounts for every remaining dyadic scale through the proved all-n envelope.
There is no truncation-equality assumption, later p512/p1024/p2048 input, graph enlargement or substitution R=beta.

### Exact accepted return input and independently recomputed certificate

The numerator N written in C788 was parsed and compared with the exact p256 numerator in the accepted fixed C776 statement; they agree exactly, and both denominators are 2^504.
C776 and R996 retain completeness for the original probabilities and every returned representation through time256, using the height48 argument and independently checked integer weights.
The present proof requires precisely that accepted scalar and no larger native scope.
C776's selected decision also explicitly supplies the already invoked C526 upper-radius input.

Writing

    A=C_* N^4 1699^1024,
    B0=2^2016 1000^1024,

independent arbitrary-precision integer arithmetic verifies 20A<19B0.
The exponent 2016 is exactly 4*504, so A/B0 equals C_* p256^4 (1699/1000)^1024.
An additional exact rational enclosure, checked by integer cross-multiplication, is

    919609135/1000000000 < A/B0
                            <919609136/1000000000 <19/20.

These are exact rational comparisons, not floating-point sign tests.
The supplied final-certificate code is sufficient to reproduce the decisive integer inequality.
The rational table above was recomputed independently from its defining formula, rather than accepted from the table text.

Taking positive fourth roots gives (1699/1000)^256 p256<C_*^(-1/4), and comparison with the independently checked infinite-tail lower bound yields R^256 p256>(1699/1000)^256 p256.
Since p256>0 and both bases are positive, cancellation and monotonicity of the 256th power prove R>1699/1000 strictly.
Strict monotonicity of log proves the entropy statement.
The unchanged accepted R<=beta and exact beta<1723/1000 give the full displayed interval.
This strengthens the earlier lower endpoint at the same fixed original input.

## Scope and remaining limits

This finding covers the whole C788 v1 statement and RB1--RB3 proof, its exact finite arithmetic and the necessary accepted-input interfaces.
It reuses the reviewer's prior independent C786 v2 inspection and the existing R996 native evidence honestly at their recorded scopes.
No new complete-return computation was run, no original graph or state cap was enlarged, and no formal verification or recursive source-proof audit is asserted.
The new deductions are fully explicit elementary rational algebra, the displayed integral evaluation and the accepted convergent dyadic identity; no unresolved source attribution or additional external theorem was identified.

The result does not determine R=beta or R<beta, the critical mean, C828's derivative at R, a positive linear midpoint moment, varying-input uniformity or the unrestricted G0001 conclusion.
The whole finding supports adoption without substantive repair by a separate responsible C788 decision.
This R itself changes no C assessment, Task status or execution authority.
