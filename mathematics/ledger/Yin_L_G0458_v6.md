---
author: Yin
---

# Moving square layers: cyclotomic repair cannot repeat the parity halving

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating and bottleneck contributors derived and checked the direct-rotation obstruction.
The bottleneck contributor supplied the cyclotomic-repair obstruction, which the coordinating contributor checked against the exact retained coprimality statement.
These are ordinary author checks, not independent review or a new Claim assessment.

<a id="rotation-iteration-scope"></a>
## The actual output of the first halving

Retain [v5's dyadic rational rotation](Yin_L_G0458_v5.md#dyadic-rational-rotation): for n=2^k, k>=2, and r=n/2+1,
\[
 B_n=(z^n-1)/(z^2-1),\qquad Q_n=z^{2n}+1-z^rB_n.
\]
It gives F_k(iz)=Q_n(z)Q_n(-z) and m(F_k)=2m(Q_n).
For k>=3 these measures are positive.
The [exact coprimality calculation](Yin_L_G0458_v5.md#dyadic-rotation-coprimality) also gives
\[
                       \gcd(Q_n(z),Q_n(-z))=1.
 \tag{H1}
\]
The present question is whether another root-of-unity rotation, with optional cyclotomic multiplication or extraction, can repeat that particular paired-factor mechanism on Q_n or one of its positive integer factors.
No new polynomial parameter is computed here.

<a id="direct-rational-rotation-obstruction"></a>
## Only the real rotations preserve rational coefficients directly

Let zeta be a root of unity, and suppose lambda Q_n(zeta z) belongs to Q[z] for a nonzero complex scalar lambda.
The constant coefficient is lambda, so lambda is a nonzero rational number.
Since B_n=1+z^2+...+z^(n-2), the coefficients of Q_n at r and r+2 are both -1.
These exponents are distinct from zero and 2n for every n>=4.
Consequently zeta^r and zeta^(r+2) are rational.
The integer r is odd, so gcd(r,r+2)=1; an integer Bezout combination of the exponents shows that zeta itself is rational.
A rational root of unity is one or minus one.
Thus
\[
 \lambda Q_n(\zeta z)\in\mathbb Q[z],\quad\lambda\ne0
                 \quad\Longrightarrow\quad\zeta\in\{1,-1\}.
 \tag{H2}
\]
This includes an arbitrary leading-coefficient normalization through lambda.
It does not assert that every individual factor of Q_n has the same coefficient-support property.

<a id="cyclotomic-repair-parity-obstruction"></a>
## Cyclotomic repair cannot restore a paired rotation on a positive factor

Let P be a monic integer divisor of Q_n with m(P)>0, and let zeta be any root of unity.
There are no nonzero products C,D of cyclotomic polynomials, allowing nonzero scalar and monomial factors, and no polynomial U in C[z], for which
\[
                   C(z)P(\zeta z)=D(z)U(z)U(-z).
 \tag{H3}
\]
The nonzero condition excludes an identically zero side.
Allowing both C and D includes cyclotomic multiplication and extraction after clearing a cyclotomic denominator.

To prove this, take a root beta of P outside the unit circle; one exists because P is monic and m(P)>0.
In particular beta and beta/zeta are nonzero and are not roots of unity.
Every nonzero root of C or D is a root of unity, so neither polynomial vanishes at beta/zeta or at -beta/zeta.
Evaluating (H3) at beta/zeta forces U(beta/zeta)U(-beta/zeta)=0.
The product U(z)U(-z) has exactly the same zero at the opposite argument, hence evaluating at -beta/zeta forces P(-beta)=0.
Thus beta and -beta are both roots of Q_n, contradicting (H1).
This proves (H3) impossible without any irreducibility requirement on P.

More generally the same proof excludes replacing U(z)U(-z) by any nonzero even polynomial with a non-torsion root.
For example, for a primitive 2^s-th root xi, s>=2, and a nonzero rational polynomial V,
\[
             N_s(z)=\prod_{a\in(\mathbb Z/2^s\mathbb Z)^\times}
                              V(\xi^a z)
 \tag{H4}
\]
is even: replacing z by -z permutes the factors by a to a+2^(s-1).
Thus no identity C(z)P(zeta z)=D(z)N_s(z) can supply a further measure-reducing rotation product in this setting.
This assertion is about the displayed rational-polynomial rotation norm, not about arbitrary polynomials with coefficients in a cyclotomic field.

<a id="rotation-iteration-remaining-gap"></a>
## What has been excluded and what remains possible

The positive degree-fourteen factor in [J143](../computations/programs/Yin_J_G0143/readme.md#rational-rotation-control) divides Q_8, so the cyclotomic-repair obstruction applies to it as well.
The first exact halving is genuine, but the whole Q_n has no direct nonreal rational rotation.
For any positive integer divisor of Q_n, cyclotomic repair cannot recreate the same paired-factor construction.
This is stronger than merely observing that Q_n itself is not even.

The argument uses the opposite-root pairing and does not exclude general odd-conductor rotation norms, arbitrary algebraic-coefficient norms, unrelated arithmetic factorizations or a changed input family.
For instance, the two conjugate rotations at order three do not have the opposite-root pairing used above.
No construction in any of those remaining domains is supplied here.
The unresolved task remains an actual integer family with positive total measures tending to zero, rather than a fixed-factor or fixed-degree improvement.

The derivations use only direct coefficient inspection, root evaluation and the exact v5 coprimality input.
No new external theorem, numerical calculation, native program or formal review is used.
The coordinating contributor read the complete saved argument and checked its coefficient, root-pairing and displayed norm scopes.
