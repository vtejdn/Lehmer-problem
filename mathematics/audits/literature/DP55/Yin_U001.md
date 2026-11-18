---
author: Yin
---

# Coefficient intervals and the reciprocal of a Pisot pole

<a id="dp55-u001"></a>
<a id="coefficient-intervals"></a>
## The rational case before the terminal degree

Dufresnoy and Pisot normalize the irreducible polynomial \(P\) of a Pisot number \(\theta\) to have \(P(0)>0\) and leading coefficient \(\epsilon=\pm1\).
They use \(Q(z)=\epsilon z^{\deg P}P(1/z)\), so \(Q(0)=1\).
For the nonlinear nonunits considered here the reduced quotient \(F=P/Q\) has integer Taylor coefficients at zero, unit boundary modulus, and a unique disk pole at \(\alpha=1/\theta\).
This lies in the authors' rational case B, and its degree \(s\) is the degree of \(P\).
Their introductory exception for a reciprocal quadratic has constant one. [Normalization, printed p. 69](../../../literature/pdf/DP55.pdf#page=2)

Write \(F=\sum_{j\ge0}u_j z^j\), with \(u_0>1\).
Their interpolation polynomials \(D_n,D_n^*\) have leading coefficients \(-1,+1\), respectively, with reciprocally normalized denominators \(E_n,E_n^*\) of constant term one.
The two quotients agree with \(F\) in Taylor degrees less than \(n\), and their coefficients in degree \(n\) give \(w_n,w_n^*\).
For \(s\ge3\) the specialization of Theorem 1 in case B gives \(u_1>w_1=u_0^2-1\) and \(w_n<u_n<w_n^*\) for \(2\le n<s\).
Here \(D_1/E_1=(u_0-z)/(1-u_0z)\) gives \(w_1\).
Theorem 2 gives \(\tau_n<1/\alpha<\tau_n^*\) for \(2\le n<s\), where \(\tau_n,\tau_n^*\) are the positive exterior roots of the interpolation polynomials.
At \(n=s\) a boundary equality depends on \(F(1)\); the strict inequalities above use only \(n<s\). [Theorems 1 and 2, printed pp. 81–82](../../../literature/pdf/DP55.pdf#page=14)

The normalization, definition of case B and these preterminal conclusions were inspected directly in the [journal edition](readme.md#edition).
This is statement-level verification of the indicated part of the two theorems.
Boyd cites this method in his [fixed-coefficient minimum](../Boy78/Yin_U001.md#least-fixed-norm); the specific cubic bound in the project also has a direct proof.
