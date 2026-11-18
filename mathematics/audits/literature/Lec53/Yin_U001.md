---
author: Yin
---

# Zero indices of exponential polynomials over a fixed number field

<a id="lec53-u001"></a>
<a id="zero-set"></a>
## Lech's characteristic-zero theorem and exponential-polynomial lemma

Lech's theorem on printed page 417 concerns a sequence over a characteristic-zero field satisfying a homogeneous linear recurrence with constant coefficients from its order onward.
Its zero positions are eventually periodic.
Equivalently the set of nonnegative zero indices is a finite set together with finitely many arithmetic progressions.
The lemma in section 1, spanning printed pages 417 and 418, supplies the form directly applicable to exponential polynomials. [1953 edition](readme.md#edition) · [Theorem and lemma](../../../literature/pdf/Lec53.pdf#page=1)

Let \(K\) be a fixed number field, let \(\gamma_j\in K^\times\), and let \(P_j\in K[X]\) for a finite list of indices \(j\).
Put \(F(n)=\sum_j P_j(n)\gamma_j^n\).
If \(F\) has infinitely many integral zeros, the lemma gives a modulus \(r\ge1\) and complete residue classes modulo \(r\) on which \(F\) vanishes, with at most finitely many remaining zeros.
The lemma permits \(n\in\mathbb Z\), so restriction to \(n\ge0\) gives whole one-sided progressions plus a finite exceptional set.
Polynomial prefactors and repeated characteristic roots are permitted.
Indeed, with \(E\) the forward shift, \((E-\gamma_j)^{\deg P_j+1}\) annihilates \(P_j(n)\gamma_j^n\) for every nonzero \(P_j\).
The product of these operators supplies a constant-coefficient recurrence for \(F\). [Section 1, lemma continued](../../../literature/pdf/Lec53.pdf#page=2)

In the number-field argument of section 2, Lech chooses a finite place where all the bases are units and a common power close enough to one for analytic interpolation on each residue class.
Infinitely many integer zeros on such a class have a local accumulation point, forcing its interpolating function to vanish identically.
Lech credits the algebraic-number case to Mahler and extends the theorem to arbitrary characteristic-zero fields. [Number-field proof sketch, printed p. 418](../../../literature/pdf/Lec53.pdf#page=2)

<a id="torsion-classes"></a>
## Deciding which classes can contain infinitely many zeros

For fixed nonzero bases, let \(s\) be a common multiple of the orders of all root-of-unity ratios \(\gamma_i/\gamma_j\), taking \(s=1\) if there are no nontrivial such ratios.
On \(n=a+st\), combine terms with the same \(\beta=\gamma_j^s\) into the polynomial coefficient \(\sum_{\gamma_j^s=\beta}\gamma_j^a P_j(a+st)\).
The resulting distinct bases have pairwise quotients of infinite order.
If all combined coefficients vanish identically, this entire class consists of zeros.
Otherwise the class contains only finitely many zeros.

For the last assertion the lemma would otherwise give a further whole progression of zeros.
On that progression the remaining exponential bases are still distinct and the nonzero polynomial coefficients remain nonzero after the affine substitution.
Sequences \(B_i(t)\lambda_i^t\) with distinct nonzero \(\lambda_i\) and nonzero polynomial coefficients \(B_i\) are linearly independent in the required sense.
To isolate the \(i\)-th term, apply \(\prod_{j\ne i}(E-\lambda_j)^{1+\deg B_j}\).
It kills every other term and multiplies the leading coefficient of the \(i\)-th polynomial by the nonzero scalar \(\prod_{j\ne i}(\lambda_i-\lambda_j)^{1+\deg B_j}\).
Thus the putative progression cannot vanish identically.
This supplies the polynomial-prefactor version of Lech's nondegenerate consequence on printed page 417. [Source theorem](../../../literature/pdf/Lec53.pdf#page=1)

The inspection checked the theorem, the lemma and the number-field interpolation argument on printed pages 417 and 418.
The proof of the general transcendental-field extension was outside this inspection.
These statements classify the zero set qualitatively and supply no numerical upper bound on its exceptional indices for the present application.
