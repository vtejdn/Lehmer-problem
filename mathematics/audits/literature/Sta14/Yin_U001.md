---
author: Yin
---

<a id="sta14-u001"></a>
# Exterior root density and Mahler measure of \(X^n-aX-1\)

Fix a real \(0<a\le2\) and write \(\nu_{n,a}\) for the number of roots of \(P_{n,a}(X)=X^n-aX-1\) of modulus strictly greater than one, counted with multiplicity.
Put \(A=\arccos(-a/2)\) and let \(M(P_{n,a})\) denote the product of their absolute values.
Theorems 1 and 2 of the [inspected edition](readme.md#arxiv-v2) state that
\[
    \lim_{n\to\infty}\frac{\nu_{n,a}}n=\frac A\pi,\qquad
    \lim_{n\to\infty}\log M(P_{n,a})
       =\frac1{2\pi}\int_0^A \log(1+a^2+2a\cos t)\,dt .
\]
The paper states the second limit in multiplicative form, with absolute values explicit at the start of its proof. [Theorem 1, p. 3](../../../literature/pdf/Sta14.pdf#page=3) and [Theorem 2, p. 4](../../../literature/pdf/Sta14.pdf#page=4)

For \(a=1\) we have \(A=2\pi/3\) and \(2+2\cos t=|1+e^{it}|^2\).
Evenness and the condition \(|1+e^{it}|>1\) on \((-2\pi/3,2\pi/3)\) turn the integral into \(\int_0^{2\pi}\log^+|1+e^{it}|\,dt/(2\pi)\).
These are both scalar limits in the [joint distribution for \(X^n-X-1\)](../../../claims/Yin_C_G0345_v191.md#statement).
For a root \(z=\rho e^{it}\), Stankov's exact equation (2.1) is \(\rho^{2n}=1+a^2\rho^2+2a\rho\cos t\).
Remark 2.2 describes its approximation by a linear function of \(\cos t\) when \(\rho\) approaches one.
The joint logarithmic law in the project argument also controls the contribution of bounded tests near the singular angle \(t=\pi\). [Equation (2.1), p. 5](../../../literature/pdf/Sta14.pdf#page=5) and [Remark 2.2, p. 8](../../../literature/pdf/Sta14.pdf#page=8)

The source obtains the angular count by comparing the exterior arc with the distribution of root arguments and sums log moduli on that arc to obtain the measure.
In the finite identity following \((*)\) on p. 12, doubling the terms with upper-half-plane arguments including zero counts the positive real root \(\beta_n\) twice.
At \(a=1\) its log contribution must be counted once, so the doubled logarithmic sum exceeds the full sum by \(\log\beta_n\).
The relation \(\beta_n^n=1+\beta_n<3\) bounds that difference by \((\log3)/n\), which vanishes in the limit. [Source proof, p. 12](../../../literature/pdf/Sta14.pdf#page=12)

This inspection covered the theorem statements, the polar identity and radial remark, the selected summation step and the specialization \(a=1\).
The proofs of the auxiliary lemmas, the extension to smallest Perron numbers under the Lind–Boyd conjecture, and the finite numerical tables lie outside this inspection.
