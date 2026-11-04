---
author: Yin
---

# A restricted radial-support Mahler p=2 floor

## Statement

Use the FM13 arithmetic subspace S and Mahler-norm normalization linked below.
For a nonzero f=f_alpha in S with a minimal representative of degree d, let k count its nonzero radial logarithms with every original complex embedding counted.
Then ||f||_(m,2)>=2m sqrt(d/k).
For d>=exp(e), the accepted numerical Dobrowolski bound gives ||f||_(m,2)>=(1/1200)sqrt(d/k)(log log d/log d)^3.
For each fixed C>0 the class k<=C d(log log d/log d)^6 therefore has a positive p=2 floor, including the stated finite-degree and Salem boundaries.

## Source and original checking boundary

The place-space model, arithmetic subspace S, minimal representative and p-norm conventions are [FM13 U001](../audits/literature/FM13/Yin_U001.md#restricted-arithmetic-set) and its [degree/Mahler operator definitions](../audits/literature/FM13/Yin_U001.md#field-and-degree-projections).
The source's p=1, p=2 and p=infinity assertions and actual source-proof limits remain [there](../audits/literature/FM13/Yin_U001.md#p-two-and-classical-gap-boundary).
The project deductions below use the already accepted [C147v5 numerical bound](Yin_C_G0147_v5.md#argument) and [Dim19 house input](../audits/literature/Smy08/Yin_U001.md#smy08-house); no general p=2 theorem or uniform p=2-to-p=1 return is claimed.
No Current assessment is selected for this newly organized fixed account.
Placement preserves the existing argument and actual earlier checking scopes; it supplies no new mathematical adoption, review relationship, source reading or Task/E authority.

## Retained argument

For a nonzero f=f_alpha in S with a minimal representative of degree d, put a_i=log|alpha_i| for all d original complex embeddings, counting a nonreal pair twice.
All finite-place values vanish.
Then exactly

    sum_i a_i=0,
    m=sum_i max(a_i,0),
    ||f||_(m,1)=sum_i |a_i|=2m,
    ||f||_(m,2)^2=d sum_i a_i^2,
    ||f||_(m,infinity)=d max_i |a_i|.

Let c=log2/4 be the accepted house constant.
The house theorem supplies max_i |a_i|>=c/d, which gives only

    ||f||_(m,2)>=c/sqrt(d)

by the single largest term.
This is degree dependent and tends to zero.
The source's elementary norm comparisons do not upgrade it to a uniform p=2 lower bound.

If k is the number of NONZERO a_i, counted with the same embedding multiplicity, elementary Cauchy--Schwarz gives

    2m=sum_i |a_i|<=sqrt(k sum_i a_i^2),
    ||f||_(m,2)>=2m sqrt(d/k).                         (A)

For d>=exp(e), the already accepted [full numerical Dobrowolski input](Yin_C_G0147_v5.md#argument) gives

    m>=(1/2400)(log log d/log d)^3,
    ||f||_(m,2)>=(1/1200)sqrt(d/k)(log log d/log d)^3.  (B)

Thus a class with k<=C d(log log d/log d)^6 has the large-degree uniform p=2 floor 1/(1200 sqrt(C)).
The finitely many remaining degrees have a positive floor from the already accepted house bound.
This is a restricted support-concentration consequence of existing inputs, not an unrestricted p=2 theorem or a classical p=1 gap.
For Salem numbers, k=2 and the source's exact formula (4.8) is

    ||f_tau||_(m,p)=2^(1/p) d^(1-1/p) log tau,
    ||f_tau||_(m,2)=sqrt(2d) log tau.

The lower bound in (B) then grows with d, even though a hypothetical Salem total measure could tend to zero at a compatible slower rate.
Accordingly the Salem family is already benign for this p=2 question without settling its p=1 minimum.
Small total m has not been shown to imply the support condition in (B); conjugates can have small nonzero radial logarithms rather than lie exactly on the circle.
