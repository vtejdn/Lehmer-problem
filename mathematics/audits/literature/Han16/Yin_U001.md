---
author: Yin
---
# Han16-U001: finite-field quadratic Hankel periodicity and its synchronization boundary

<a id="han16-u001"></a>
## Source, statement and reading scope

Use the [author manuscript edition](readme.md#author-manuscript), printed/PDF pp.1--3, definition (1.1), Theorem 1.1 and its adjacent interpretation.
The primary statements were directly read online and in the retained original on 2026-11-05.
No inspection of the complete Section 3 proof, Algorithm 3.3 or its implementation is claimed.

For a prime p and F(z) in F_p[[z]], Theorem 1.1 assumes a polynomial equation A(z)+B(z)F(z)+C(z)F(z)^2=0 with one of four displayed coefficient conditions.
The relevant condition (i) is B(0)=1, C(0)=0 and C not identically zero.
Under the source hypotheses the Hankel continued fraction and the sequence of leading Hankel determinant values H_n(F) are ultimately periodic.
The source's leading convention is H_n(F)=det(F_(i+j)) for 0<=i,j<n, with H_0=1.
The other three alternatives of the source theorem are not needed in the conversion below.

<a id="shifted-application-and-limit"></a>
## Exact shifted application and limit

For a series a(z), the project's shifted determinant is Delta_h(a)=H_h((a-a(0))/z).
At an odd prime the original G satisfies U G^2=V and G(0)=1.
Putting F=(G-1)/z, dividing the polynomial equation by z and then by 2 gives

    (U-V)/(2z)+U F+(zU/2)F^2=0.

All coefficients are polynomials, B(0)=1, C(0)=0 and C is nonzero, so Theorem 1.1(i) applies to the shifted determinant sequence.
For a characteristic-two Artin--Schreier germ H^2+H=a/q with q(0)=1 and a(0)=H(0)=0, putting F=H/z gives

    -a/z+q F+zq F^2=0,

which meets the same source condition.
These are direct notation conversions, not new periodicity theorems.

The inspected source conclusion is ultimate periodicity.
By itself it neither identifies a nonzero residue class containing index zero nor proves that the nonzero residue classes for several primes intersect.
The [C858 v3 lattice argument](../../../claims/Yin_C_G0858_v3.md#general-quadratic-lattice) supplies that additional exact index statement under its own split-place hypotheses, by preserving the original polynomial lattice and proving V_0=0.
The source is classical attribution and comparison for the nearby periodicity mechanism, not a proof premise of that lattice argument.
No originality or priority claim for general finite-field Hankel periodicity is made.

The scoped search used finite-field quadratic Hankel determinants, periodicity, continued fractions and polynomial Pell terminology after the direct divisor calculation suggested the established analogy.
It ended after the primary theorem and its exact shift conversion were sufficient to identify the overlap and remaining distinction; no literature-wide absence claim or recursive audit is intended.
