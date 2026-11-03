---
author: Yin
---
# A two-set logarithmic correction to the all-shear component screen

Date: 2026-10-18T11:45.
Root authored this direct analytic reduction under the until-stop G0001 authority.
No new parameter grid or original-norm assertion is needed.

<a id="two-set-correction"></a>
## Exact question and reuse

The accepted [C157v2](../../../claims/Yin_C_G0157_v2.md#statement) gives U_s=(E+sG)^2+2G^2 and the full all-positive-q logarithmic envelope.
[J100](../Yin_J_G0100/readme.md#certified-results) already excludes every real shear on the quartic control, while the Lehmer component-only lower bound leaves a possible deficit below0.038554.
That earlier screening bound dropped the nonnegative E-dependent correction entirely.
The present finite question asks whether two fixed phase sets force that omitted correction to exceed0.077107, which would close the Lehmer all-real-s family without optimizing or scanning s or q.
This changes the analytic certificate; it does not rerun the earlier unchanged component integrals or infer a uniform-input conclusion.

## Direct analytic reduction

Use normalized circle Haar measure mu and the exact real centered functions E,G of C157v2.
The nonzero Laurent polynomial G has finitely many circle zeros, so T=E/G is defined almost everywhere.
For every real s,

    J_(U,s)=J_G+log2+integral log(1+(T+s)^2/2) dmu.

This follows from U_s=2G^2[1+(T+s)^2/2] away from the finite zero set.
All logarithms are integrable: U_s and G are nonzero Laurent-polynomial absolute-value squares or sums of such squares, with at most finite-order zeros.
Their difference gives the integrability of the nonnegative correction, including removable or logarithmic singularities of T.

Suppose measurable disjoint phase sets A,B satisfy T>=a on A and T<=b on B, where a>b, and mu(A),mu(B)>=eta>0.
If s>=-(a+b)/2, then T+s>=(a-b)/2 on A.
Otherwise T+s<-(a-b)/2 on B.
Consequently, simultaneously for all real s,

    integral log(1+(T+s)^2/2) dmu
       >=eta log(1+(a-b)^2/8)=Delta.

Combining with C157v2 gives for every real s and every positive real q,

    I_(s,q)>=log2+[J_G+J_V+log2+Delta]/2.

Only the phase-set enclosures and previously retained J100/J99 balls are needed for a rigorous fixed-input exclusion.
No integrality condition is imposed on s or q in this circle bound; the separate arithmetic theorem still requires s integral and q an integer at least1.

## Finite certificate and review boundary

The complete finite program, exact declared scope, interval unions and enclosing result belong to [this J101 group](readme.md).
Only the original Lehmer degree-ten input is new in that certificate; the quartic exclusion and prior component integrals retain their existing J100/J99 scopes.
The preliminary point observations choose the phase thresholds but are not certified measures.
Whole rational phase intervals supply the actual measure certificate.
The finite result excludes this one complete all-shear/all-weight family, not every quadratic auxiliary, all inputs or the unrestricted Task.
Actual independent checking, when completed, is recorded separately and does not arise from this author argument.
