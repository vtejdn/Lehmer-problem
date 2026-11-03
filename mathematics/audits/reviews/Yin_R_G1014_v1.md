---
author: Yin
---

# Independent whole review of the original quartic radius bound above 1711 over 1000

The review act is dated 2026-10-26T12:32, with Yin as the human record author.
A separately assigned reviewer outside substantive development read the entire fixed [C794 v1 Statement](../../claims/Yin_C_G0794_v1.md#statement) and [Complete argument](../../claims/Yin_C_G0794_v1.md#complete-argument) before inspecting the new exact finite input.
The initial selected target is [decision radius-1711-open](../../claims/Yin_C_G0794_v1.md#decision-radius-1711-open).
No author arithmetic dialogue, proposing-agent explanation outside the fixed proof, mutable draft, persistent memory or prior conclusion about C794 was supplied or consulted.
The reviewer's prior independent whole work on C786 v2 and C788 v1, retained in [R1006](Yin_R_G1006_v1.md#whole-seven-state-finding) and [R1007](Yin_R_G1007_v1.md#radius-1699-whole-finding), is reused openly at its unchanged scope.
After reading C794, the reviewer read the complete fixed C793 and its adopted decision, and read [R1012](Yin_R_G1012_v1.md#whole-finite-finding) as the explicitly selected accepted native evidence for the new scalar p512.

The reviewer checked the entire NR1--NR3 chain and independently recomputed all three rational table entries, every displayed margin, the constant C_*, exact scalar correspondence, exponent bookkeeping and large-integer certificate.
These arithmetic checks used Python standard-library exact fractions and arbitrary-precision integers, with no floating-point premise.
No substantive repair was supplied.
This review did not run another return graph or native recurrence and does not relabel the existing R1012 reproduction as its own calculation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole radius-1711 finding](#radius-1711-whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole radius-1711 finding](#radius-1711-whole-finding) | [C794 entire statement](../../claims/Yin_C_G0794_v1.md#statement) | Actual quartic and complete original law, true R and h_2(beta), strict1711/1000 lower endpoint, accepted upper interval and every stated exclusion. |
| [Whole radius-1711 finding](#radius-1711-whole-finding) | [C794 complete argument](../../claims/Yin_C_G0794_v1.md#complete-argument) | All NR1--NR3 rational majorants and table entries, complete infinite dyadic split, accepted exact p512, independently recomputed integer certificate and strict true-radius comparison. |
| [Whole radius-1711 finding](#radius-1711-whole-finding) | [C786 v2 adopted envelope](../../claims/Yin_C_G0786_v2.md#decision-whole-reviewed-2026-10-26) | Same original complete D_n, exact all-n G(n), true-radius dyadic identity and H_n<=log(2G(n)); reuse unchanged prior independent R1006 coverage. |
| [Whole radius-1711 finding](#radius-1711-whole-finding) | [C788 adopted rational majorants](../../claims/Yin_C_G0788_v1.md#decision-whole-reviewed-2026-10-26) | Fixed parameter bounds, exact pi integral and G^+ formula at arbitrary positive n with the stated square condition, plus the repeated512/1024 entries and same-law conventions; prior independent R1007 coverage is reused, and the older1699 lower endpoint is comparison only. |
| [Whole radius-1711 finding](#radius-1711-whole-finding) | [C793 adopted exact p512](../../claims/Yin_C_G0793_v1.md#decision-whole-reviewed-2026-10-26) | Only the exact full original p512=N512/2^1019 under the declared time512/height95 completeness and original-weight scope; no midpoint asymptotic premise is imported. |
| [Whole radius-1711 finding](#radius-1711-whole-finding) | [R1012 accepted native finding](Yin_R_G1012_v1.md#whole-finite-finding) | Existing independent full finite/native evidence, including all513 W/V entries and complete statewise vector comparisons, supporting the accepted exact scalar; reused without another graph run. |
| [Whole radius-1711 finding](#radius-1711-whole-finding) | [C526 upper-radius input](../../claims/Yin_C_G0526_v1.md#statement) | Accepted same original quartic R<=beta, without equality or critical-mean classification. |

<a id="radius-1711-whole-finding"></a>
## Whole finding

The complete fixed C794 statement and NR1--NR3 argument are supported at the stated original-law scope.
No mathematical defect, arithmetic discrepancy or required substantive correction was found.

### The parameter bounds apply at the new indices

C786 v2's full G(n) has the same fixed quartic, both original endpoint factors and true R as this target.
The bounds a<14/9, b<17/9, s<19/25, kappa<2/3, sqrt13>18/5 and pi<22/7 in C788 are inequalities for those fixed parameters.
They do not depend on the old table's finite choice of indices.
The positive-variable substitution therefore applies for every positive n and every positive rational u satisfying u^2>(22/7)(n/2+2/3).
It gives the exact majorant used here, with no new source or finite-to-infinite assumption.
The strict root/radical/pi calculations underlying these parameter bounds retain the prior independent R1007 scope.

For an independent recomputation, the formula was simplified exactly to

    G^+(n)=(6664+2170u)/81+(1672/325)h^+,
    h^+=n/2+2/3.

These coefficients equal the three unsimplified coefficients in C794.
Using exact rational arithmetic in this expression gives:

| n | h^+ | u | Exact square margin | Recomputed G^+(n) | Exact integer minus G^+(n) |
| ---: | --- | --- | --- | --- | --- |
| 512 | 770/3 | 14201/500 | 5203/750000 | 113914381/52650 | 20219/52650 |
| 1024 | 1538/3 | 40141/1000 | 1297501/21000000 | 399626849/105300 | 91951/105300 |
| 2048 | 3074/3 | 56749/1000 | 1429021/21000000 | 723842753/105300 | 94747/105300 |

The square margin is u^2-(22/7)h^+ in every row.
All six margins are strictly positive.
Thus all three stated strict upper bounds G(512)<2164, G(1024)<3796 and G(2048)<6875 follow with their exact constants.
The new 2048 row is an analytic envelope evaluation, not a measured return probability or an enlargement of C793's finite graph.

### The full dyadic tail and strict normalized lower bound

The adopted identity is the convergent nonnegative expansion

    H_n=-log(R^n p_n)
       =sum_(j>=0)2^(-j-1)log D_(2^j n).

At n=512 the terms j=0,1 give the first two displayed logarithms.
Reindexing the terms j>=2 leaves exactly (1/4)H_2048, because 2^(-(k+2)-1)=(1/4)2^(-k-1).
Hence the proposed split is exact.
The accepted every-n estimates D_m<=G(m) and H_m<=log(2G(m)) apply to each term at the same original law and true radius.
Combining them with the strict three-row bounds gives

    H_512<(1/2)log2164+(1/4)log3796+(1/4)log13750.

The factors in the product were independently multiplied:

    2164^2*3796*13750=244423756720000=C_*.

Multiplying the logarithmic inequality by four and exponentiating with the negative sign gives R^512 p512>C_*^(-1/4), with the strict direction claimed in NR1.
The H_2048 term contains all still later dyadic scales through the all-n theorem.
No finite truncation is asserted to equal the infinite sum, and no p1024, p2048 or p4096 observation is used.

### Exact scalar correspondence and native-scope boundary

The numerator N in C794 was parsed and compared with N512 in the accepted C793 statement; every digit agrees exactly.
Both fixed materials use the denominator 2^1019.
The numerator is strictly positive, so the later cancellation is legitimate.

C793's FC1 bounds every returned quotient path of length at most 512 by 6/5+(11/30)256=1426/15<96, hence integral height 95, with outward strips and both reachability directions preserving zero-to-zero words.
Its original weights are 1,2,1 over denominator 4 per digit, with no renormalization and all earlier zero visits included.
The selected R1012 finding independently reproduced all 513 return and first-return entries and checked all 254775 aligned statewise vector pairs after the original-coordinate reversal.
It specifically confirms the exact reduced p512 denominator and numerator in C793.
These facts supply an already accepted exact full-original scalar at the requested time 512 scope.
This review consumes that scalar and its actual existing evidence; it supplies no new reproduction of the native graph, recurrences or payload and extends none of their finite completeness bounds.
The C793 midpoint values and failed finite crossing tests are not premises of the new radius deduction.

### Independent integer certificate and strict radius conclusion

The reviewer independently formed the arbitrary-precision integers

    A=C_* N^4 1711^2048,
    B0=2^4076 1000^2048.

The exponents satisfy 4076=4*1019 and 2048=4*512, so A/B0 is exactly C_* p512^4 (1711/1000)^2048.
The decisive direct integer comparison 100A<97B0 passes.
A second check using integer cross-multiplication gives the exact rational enclosure

    960568297412/10^12 < A/B0
                         <960568297413/10^12 <97/100<1.

This enclosure and the direct comparison are integer-certified signs, not floating-point approximations.
The complete certificate code printed in C794 reproduces the decisive comparison using the same exact input.
Taking positive fourth roots gives (1711/1000)^512 p512<C_*^(-1/4).
Together with the full-tail lower bound above, this yields R^512 p512>(1711/1000)^512 p512.
Cancellation of p512>0 and strict monotonicity of the 512th power on positive reals prove R>1711/1000.
The logarithmic assertion follows from strict monotonicity of log and the unchanged definition h_2(beta)=logR.
The accepted same-law C526 interface R<=beta and the already certified beta<1723/1000 supply the final upper endpoint.
Since 1711/1000>1699/1000, the claimed strengthening is at precisely the same fixed input.

## Verification and remaining limits

The entire fixed target and its newly consumed exact-input evidence were inspected, and all new finite rational/integer calculations were independently recomputed.
The prior C786/C788 independent findings are reused at their unchanged analytic and parameter scopes, while R1012 supplies the separately completed native evidence for p512.
No formal verification, new graph execution, larger state cap or recursive external source-proof audit is claimed.
The only new reasoning is explicit finite rational algebra and application of the already proved convergent dyadic identity; no unresolved external theorem or source attribution was identified.

The strict lower bound does not decide R=beta or R<beta, the critical mean, g'(R), positive linear midpoint growth, varying-input uniformity or the unrestricted G0001 question.
The finding supports a separate responsible adoption decision without substantive repair.
This R changes no C assessment, Task state or execution authority.
