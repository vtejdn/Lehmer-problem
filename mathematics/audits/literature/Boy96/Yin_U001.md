---
author: Yin
---

<a id="boy96-u001"></a>
# Boyd's defining polynomials for regular Pisot numbers

<a id="regular-cofactor"></a>
## The cofactor in the defining polynomial

In Section 2, pp. 845–846 of the [published paper](readme.md#edition), \(C\) is the monic minimal polynomial of a Pisot accumulation point and \(A\) is an associated integer polynomial with \(A(0)\ne0\) and \(|A|\le |C|\) on the unit circle.
For the two signs the regular defining polynomials have the form \(F_n=z^nC\pm A\).
Boyd describes their eventual factorization as a Pisot minimal polynomial times a product of cyclotomic polynomials.
He identifies the first four distinct accumulation points as \(\phi_1=\psi_1,\phi_2,\psi_2,\phi_3\), followed by the exceptional quartic root exceeding \(1.90\).
On p. 846 he gives Talmoudi's finiteness of the irregular exceptions on every fixed compact subinterval below two.

The factor assertion also follows directly in the application to an actual Pisot root.
For \(n+\deg C>\deg A\) and \(0<s<1\), Rouché's theorem on the unit circle gives \(z^nC\pm sA\) exactly one exterior zero, counting multiplicity.
The monic polynomial at \(s=1\) can have at most one exterior zero by continuity.
If it has the prescribed Pisot number as a zero, its monic minimal polynomial accounts for that zero.
Every remaining monic irreducible factor then has its roots in the closed unit disk and nonzero constant term.
Kronecker's theorem makes each such factor cyclotomic.

The beta-expansion characteristic polynomial on p. 841 comes from a different construction, and the paper gives examples where its complementary factor has roots off the unit circle.
The proof above uses only a fixed associated pair and its circle inequality.
The second displayed choice for \(\psi_r\) on p. 845 is \((z^r+1)/(z+1)\), which fails to be a polynomial for even \(r\).
The [fixed-pair extraction](../Laz78/Yin_U001.md#compact-pisot-families) avoids this formula.
This inspection covers the statements and their cofactor implication in Sections 1–2, without rechecking the beta-expansion computations or Amara's original classification.
