---
author: Yin
---

# FK52-U001: The ordinary bounded determinant product proof

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained 11-page scan of the original published Annals article, printed pp. 520-530 / PDF pp. 1-11.

Passages: Definition p. 521; Theorem 1/Lemmas 2-3 pp. 522-524; Lemma 5 and the following positive-sandwich extension pp. 528-529.

Inspection: 2026-09-12 analytic-dependency reader: selected proofs read and reconstructed; pp. 524,528,529 visually inspected. The coordinating second check read p. 529 and the disclosed reconstructed steps, not all primary pages.


<a id="fk52-u001"></a>
## Exact retained source scope

This source proof was retained from [L_F2](../../../ledger/Yin_L_F0002_v1.md#ms24-analytic-dependencies) at 2026-10-21T01:19.
This maintenance performed no original-source opening, source-byte change or new proof review.
The selected proof concerns the ordinary bounded Fuglede-Kadison determinant, including zero values, with the finite-tracial adaptation below.
The paper's character, uniqueness and factor-dimension results and its unnecessary Lemma 6 are excluded.
The actual original second-check account is retained separately in the R_F0188 family; it is not a new whole-primary-source audit.

## Bounded multiplicativity and the finite-tracial adaptation

Let \((\mathcal N,\sigma)\) be a finite von Neumann algebra with faithful normal tracial state and let \(\Delta_\sigma\) use the ordinary log integral from [U001](../MS24/Yin_U001.md#determinant-convention).
FK52 formulates its result in a finite factor.
The selected proof uses spectral/holomorphic functional calculus, trace cyclicity and unitary polar decomposition; these ingredients hold in the present finite tracial algebra.
The usual completion of a polar partial isometry to a unitary uses finiteness.
No uniqueness of the scalar trace or classification by scalar projection dimension enters this selected argument.

For invertible factors, the central calculation is the traced derivative

\[
\frac{d}{dt}\sigma(\log X(t))
 =\sigma(X(t)^{-1}X'(t)),
\qquad X(t)>0,
\]

obtained by differentiating the resolvent formula and using cyclicity inside the trace.
For \(X(t)=e^{tA^*}e^B e^{tA}\), \(B=B^*\), integration gives

\[
\sigma\bigl(\log(e^{A^*}e^B e^A)\bigr)
 =\sigma(B)+2\operatorname{Re}\sigma(A).
\]

Polar decomposition then gives multiplicativity on invertible elements.
The derivative formula without the trace is not asserted.

The analytic extension in FK52 preserves multiplicativity even when a determinant is zero.
The review checked its positive sandwich argument: for bounded \(H,K\ge0\), use

\[
R_\varepsilon=H+\varepsilon^2(K+\varepsilon I)^{-1},
\qquad
A_\varepsilon=R_\varepsilon(K+\varepsilon I)R_\varepsilon.
\]

Both factors are invertible and

\[
A_\varepsilon
 =HKH+\varepsilon H^2+2\varepsilon^2 H
       +\varepsilon^4(K+\varepsilon I)^{-1}\ge HKH,
\]

with norm convergence to \(HKH\).
Also \(R_\varepsilon\ge H\) and \(\|R_\varepsilon-H\|\le\varepsilon\).
The determinant converges for positive norm approximations from above, by Lemma 5.
Passing to the limit gives

\[
\Delta_\sigma(HKH)=\Delta_\sigma(H)^2\Delta_\sigma(K).
\]

This is an equality of finite nonnegative numbers; no division by a zero determinant occurs.
Unitary polar decomposition and \(\Delta(T^*T)=\Delta(T)^2\), the latter a direct spectral identity, give the bounded product formula.
These are checks of the cited classical proof, not new project results.

Consequently, for \(S\in M_m(M)\) and invertible \(c_1,c_2\in M_m(\mathbb C)\),

\[
\Delta_{\operatorname{tr}_m\otimes\tau}
 \bigl((c_1\otimes1)S(c_2\otimes1)\bigr)
 =|\det c_1|^{1/m}|\det c_2|^{1/m}\Delta(S).
\]

This is exactly the scale-removal operation in MS24.
The required positive factors are invertible when the covariance has positive capacity, is strictly positive, or satisfies \(\eta(I)>0\) in the directly treated zero-capacity branch.
Indeed, \(c>0\) gives \(\eta(c)\ge\lambda_{\min}(c)\eta(I)\).
The case \(\eta(I)\) singular is separated before normalizing.
Affiliated inverses of \(S\) are never inserted into this identity.

The previously retained HS07 statement remains correct at its stated scope.
Its author-version Lemma 2.4, p. 6, has a minor displayed typo: the bound ending in \(-2\Delta(B)\) must read \(-2\log\Delta(B)\).
The preceding equality already has \(-2\tau(\log B)\); positivity of \(\Delta(B)\) makes the corrected expression finite.
This typo does not affect the direct bounded dependency retained here, and this observation does not claim a full HS07 audit.
