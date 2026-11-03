---
author: Yin
---

<a id="qz19-u001"></a>
# QZ19-U001: Bernstein's sup-norm derivative inequality for trigonometric polynomials

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Herve Queffelec and Rachid Zarouf, *On Bernstein's inequality for polynomials*, public arXiv1903.10801v1, margin dated26March2019 and title page dated27March2019; [retained PDF](../../../literature/pdf/QZ19--arxiv-v1.pdf). Journal metadata: Analysis and Mathematical Physics9(2019),1181--1207, DOI10.1007/s13324-019-00294-x. The preprint is the inspected mathematical text; no full journal/preprint comparison is claimed.

Passages: Theorem1.1, printed/PDFp.3; neighboring Theorem1.2 and selected M.Riesz interpolation proof, printed/PDFpp.4--5, including(1.5)--(1.11).

Inspection: On2026-10-10 the assigned resultant_research AI for Yin directly read these primary online passages and the retained local PDF text, checked the statement, complex coefficient domain, degree convention and applicability to the stated spherical restrictions, and read/followed the selected interpolation mechanism. It did not independently audit every interpolation identity, the original1916 paper, or the full QZ19 paper. Root separately read the same primary scope and handled acquisition; that assistance is not a derivation of the consuming approximation theorem.


## Exact accepted input

For an integer n>=1 and arbitrary complex coefficients a_j, let

    T(x)=sum_(j=-n)^n a_j exp(ijx),   x real.

Then

    sup_(x real)|T'(x)| <= n sup_(x real)|T(x)|.       (U1)

The source's degree is trigonometric degree at most n, allowing both positive and negative frequencies.
The constant n is optimal, as witnessed by exp(inx).
A real-valued T is allowed but not required.
No algebraic coefficient, root-location, sign, integrality or nonvanishing hypothesis occurs.

The selected proof supplies the nodes x_r=(2r-1)pi/(2n), 1<=r<=2n, and coefficients

    c_r=(-1)^(r+1)/(4n sin^2(x_r/2)),
    T'(0)=sum_r c_r T(x_r),   sum_r |c_r|=n.

Translating T proves(U1).
This is a record of the actually inspected proof mechanism, not a claim that the original interpolation theorem was independently reproved.
The established inequality is accepted at this precise statement and hypothesis scope under the ordinary external-input rule.

## Local adaptation and inspection boundary

[L_G284 retained D151 proof](../../../ledger/Yin_L_G0284_v1.md#uniform-primitive-height-working) applies(U1) with n=s to T(theta)=N(u cos(theta)+v sin(theta)), where N is a real homogeneous polynomial of degree s and u,v are perpendicular real unit vectors.
Direct expansion gives frequencies -s,-s+2,...,s; the full real circle stays on the sphere on which |N|<=M.
Hence |T'|<=sM.
No enlargement to algebraic degree2s or restriction to real trace roots is inserted.

Only this sharper derivative constant is consumed.
D151 separately proves the weaker constant sqrt[s(s+1)(s+2)/3] by finite Fourier expansion, Parseval and Cauchy--Schwarz, and obtains its own polynomial-height approximation from that independent bound.
QZ19 does not supply the integral rounding, primitive normalization, forced highest coordinate, full resultant, auxiliary-root expense or near-one conclusions in D151.

The [original publisher page](https://link.springer.com/article/10.1007/s13324-019-00294-x), Change history dated8May2019, was directly read.
It identifies a correction to the beginning of Section5 concerning the Mahler p=0 subharmonicity proof and a missing reference.
The [correction page](https://link.springer.com/article/10.1007/s13324-019-00306-w) supplies the correction's metadata, Analysis and Mathematical Physics9(2019),1209--1210, published8May2019.
Its full correction body is subscription-only and was not read.
Thus the inspected primary change-history description is retained without a claim to have compared the full corrected text.
Section5 and its Mahler derivative inequalities are not accepted inputs here.
This source unit is confined to the directly inspected Theorem1.1 and the stated selected proof depth.
