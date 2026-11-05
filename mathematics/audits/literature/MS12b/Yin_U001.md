---
author: Yin
---

<a id="ms12b-u001"></a>
# MS12b-U001: Pisot representation and the missing coefficient bound

For the [retained edition](readme.md), pages 2--5 and 13--18 were read, with pages 16--17 visually checked.
This is a statement/applicability inspection and selected algebra readback; Boyd's original proof and the complete interlacing classification were not audited.

A Pisot polynomial means a power of z times a Pisot minimal polynomial.
Write A*=z^(deg A)A(1/z).
For a Salem minimal polynomial R of degree d, Theorem 7.1 reports Boyd's Theorem 4.1: for each epsilon=+/-1 there are infinitely many monic Pisot polynomials A satisfying

    S_epsilon R=zA+epsilon A*,
    S_+=z^2+1, S_-=z-1.

The subsequent coverage theorem permits interlacing inputs that themselves have reciprocal real pairs off the unit circle; it is not cyclotomic-only coverage.
Its displayed equation is Q/((z-1)P)=2/(z+1).

Direct degree comparison gives deg A=d+1 for epsilon=+1 and d for epsilon=-1.
The infinite family therefore has unbounded coefficient height, since bounded-degree, bounded-height integer polynomials form a finite set.
This does not exclude a cheap representative, but the inspected theorem supplies no uniform coefficient-energy bound or bounded binary-support conclusion.
The hypotheses of the [binary auxiliary theorem](../../../claims/Yin_C_G0864_v2.md#statement) are therefore still missing; Salem coverage also leaves the general reciprocal-unit domain unresolved.
