---
author: Yin
---
# RW01-U001: weak-Poincare terminology and the fixed-defect boundary

Date: 2026-10-18T15:38.
Human record author Yin.
This is a bounded primary-source definition and applicability reading for G0001, not an external proof audit or a source of an arithmetic mixing constant.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Bielefeld SFB343 preprint 00-073 by Michael Roeckner and Feng-Yu Wang, title page dated September 19, 2000; the exact 38-page [preprint PDF](../../../literature/pdf/RW01--preprint-2000.pdf) is retained under RW01. No equivalence with the 2001 published edition is asserted.

Passages: Printed/PDF pages 1--3: title/author/date, Section1 setup and homogeneous functional in equation(1.2), and the weak Poincare inequality equation(1.6) on page3.

Inspection: All three pages were visually read from the original PDF. Ordinary text extraction was garbled and was not treated as mathematical evidence. Only the stated definition/formulation is accepted; later convergence, isoperimetric and perturbation theorems and their proofs were not inspected.


<a id="rw01-u001"></a>
<a id="rw01-weak-poincare-definition"></a>
## Exact formulation and local specialization

The source starts with a probability space (E,F,mu), a Markov C0-semigroup on L2(mu), invariant mu and generator L with domain D(L).
It writes E(f,f)=-mu(f Lf).
Equation(1.6) uses a nonnegative decreasing function alpha on(0,infinity) and a functional Phi:L2(mu)->[0,infinity] that is homogeneous of degree two, and requires

    mu(f^2)<=alpha(r)E(f,f)+r Phi(f),
    mu(f)=0, f in D(L), EVERY r>0.

The functional satisfies Phi(cf)=c^2 Phi(f) for every real c and every f in L2(mu).
These are the source's definition conventions, not a newly proved project mixing theorem.

For a finite reversible Markov kernel K and invariant law pi, L=K-I generates its Poissonized continuous-time chain and E(f,f)=<f,(I-K)f>.
The choice Phi(f)=osc(f)^2 is nonnegative, homogeneous and unchanged by adding constants.
Thus the corresponding centered formula can be written with Var_pi(f).
This finite notation conversion is elementary; it supplies no bound on alpha.

The new G0001 inquiry asks only for ONE fixed defect r<1/4 and a common finite coefficient B across its actual finite carry graphs.
That single-defect assertion is weaker than a full profile valid for every r>0.
It is not claimed to imply source semigroup convergence, irreducibility or a global spectral gap.
Its clipped-midpoint consequence and component/padding arguments are separately proved in the responsible project material; they are not attributed to RW01.

## Scope of reuse

The inspected primary passage adequately identifies the classical weak-Poincare form and its quantifiers.
No numerical constant, all-input existence theorem, original-proof acceptance or automatic quartic coverage is imported.
