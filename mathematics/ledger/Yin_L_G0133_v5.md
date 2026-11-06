---
author: Yin
---

# Integral decimation, rotation norms and direct rescaling costs

Date: 2026-11-05.
Prepared for Yin under the [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The witt_moment_compatibility delegate developed and checked these transformations and controls; the coordinating agent checked the deductions and their retained scope.
These are author-side development checks, not independent review or a new Claim assessment.

<a id="integral-rescaling-scope"></a>
## Responsible scope and existing stronger result

This version retains the actual arithmetic, Jensen expenses and domain failures of three direct attempts to rescale the cyclotomic quotients of [L133 v3](Yin_L_G0133_v3.md#three-block-integral).
The [high-frequency boundary separation in v4](Yin_L_G0133_v4.md#exact-fourier-escape) motivated the test, but no hypothetical positive vanishing-cost sequence is a premise.
Versions v1--v4 remain fixed.
The same cyclotomic three-block family and its rescaling mechanisms make this an extension of L133, rather than a new family.

The exact stronger [C868 statement](../claims/Yin_C_G0868_v1.md#statement) owns the analytic-majorant first-energy assertion and the whole-family alternative
\[
 \epsilon=0\quad\hbox{or}\quad
 \epsilon\ge\gamma,\qquad
 \gamma=\frac{(\sqrt5-2)^2}{50}.
\]
Its current mathematical assessment, review selections and original-input limits belong to C868.
The present ledger does not copy its proof, supply an independent review of it or reopen a vanishing-family assignment.
The retained transformations remain useful as precise boundaries on transferring arithmetic and logarithmic costs to different inputs.
Neither their failures nor C868's family statement resolves the unrestricted G0001 contract.

The existing [BM05 finite-cover comparison](../audits/literature/BM05/Yin_U001.md#finite-cover-and-exact-control) supplies the normalized-Haar covering argument used below.
[L133 v1](Yin_L_G0133_v1.md#general-delay-return-factorization) already keeps root-of-unity product and full-resultant multiplicities in a different delay-seed test.
The bounded reuse search also inspected [C51's decimation](../claims/Yin_C_G0051_v1.md#decimation-reuse-and-changed-test) and its [coarse-block failure](../claims/Yin_C_G0051_v1.md#coarse-decimation-no-compression).
Those concern actual digit-endpoint laws and matching weights, not the rational-function transformations below.
No new external theorem or literature acquisition is needed.

<a id="rescaling-original-domain"></a>
## Original domain and the common cost convention

Let \(A_0,B_0\) be monic reciprocal cyclotomic products with constant coefficient one and even degrees \(D=2a,E=2b\).
The empty product is allowed, and all root multiplicities are retained.
Set
\[
 f(z)=\frac{B_0(z)}{A_0(z)}
     =\sum_{j\ge0}c_jz^j,\qquad c_j\in\mathbb Z,\quad c_0=1,
\]
\[
 F(z,y)=z^{-a}A_0(z)(y+y^{-1})-z^{-b}B_0(z).
 \tag{1}
\]
The function f is analytic and zero-free in the open disk.
All circle and torus integrals use normalized Haar measure.

For \(T\ge2\) and \(t\ge0\), put
\[
 g_T(t)=
 \begin{cases}
  0,&t\le T,\\
  \operatorname{arcosh}(t/T),&t>T,
 \end{cases}
 \qquad
 \epsilon_T(h)=\int_{\mathbb T}g_T(|h|).
 \tag{2}
\]
Write \(\epsilon=\epsilon_2(f)\).
The complete [v3 quadratic Jensen calculation](Yin_L_G0133_v3.md#three-block-integral) gives
\[
 m_2(F)=\epsilon.
 \tag{3}
\]
In particular this is total logarithmic Mahler measure, without degree normalization.

We also use (2) for transformed rational functions that may leave the original cyclotomic domain.
It is then simply the displayed circle functional, not automatically the cost of a three-block object in (1).
Every function used below is nonzero and rational.
Its finitely many boundary zeros and poles give integrable logarithmic singularities; since \(g_T(t)\le\log^+t\) for \(T\ge2\), its cost is well-defined.
The identities and inequalities below concern the full boundary integrals.

<a id="integer-decimation-and-cost"></a>
## Integer coefficient decimation and its paid threshold-two bound

Fix an integer \(n\ge1\), write \(\zeta=e^{2\pi i/n}\), and set \(w=z^n\).
Define
\[
 {\cal D}_nf(w)
 =\frac1n\sum_{j=0}^{n-1}f(\zeta^jz)
 =\sum_{k\ge0}c_{nk}w^k.
 \tag{4}
\]
The second equality follows by averaging the Taylor series on a compact subdisk, where it converges absolutely.
It proves integrality of every output Taylor coefficient and makes the expression independent of the chosen n-th root z.

A common denominator is
\[
 \widetilde A(w)=\prod_{j=0}^{n-1}A_0(\zeta^jz).
 \tag{5}
\]
If \(\alpha_1,\ldots,\alpha_D\) are the roots of \(A_0\), its constant-one normalization gives
\[
 \widetilde A(w)=\prod_{i=1}^D(1-w/\alpha_i^n).
 \tag{6}
\]
The multiset of powered roots is Galois-stable, with roots of unity and all repetitions retained.
Its coefficients are rational algebraic integers and therefore integers.
Since D is even and \(\prod_i\alpha_i=1\), (6) is monic with constant coefficient one.
Inversion preserves the root multiset, so it is reciprocal.
Thus \(\widetilde A\) is again a cyclotomic product of degree exactly D, not \(D/n\).

Upon multiplying (4) by (5), its numerator is
\[
 \widetilde B(w)=\frac1n
 \sum_{j=0}^{n-1}B_0(\zeta^jz)
                    \prod_{k\ne j}A_0(\zeta^kz).
 \tag{7}
\]
This polynomial in z is invariant under \(z\mapsto\zeta z\), hence is a polynomial in w.
Its degree satisfies
\[
 \deg\widetilde B\le
 \left\lfloor\frac{E+(n-1)D}{n}\right\rfloor.
 \tag{8}
\]
The Taylor identity \(\widetilde B=\widetilde A\,{\cal D}_nf\), with (4) and (6), proves that its coefficients are integers despite the visible division by n in (7).
Its constant coefficient is one.
No cancellation is assumed in the degree account.

The numerator need not remain cyclotomic or zero-free, even when monicity, reciprocity and even degree happen to survive.
For example,
\[
 A_0=1,\qquad B_0=(1+z)^4,\qquad
 {\cal D}_2f(w)=1+6w+w^2.
 \tag{9}
\]
The original blocks satisfy every hypothesis in (1), while the last polynomial has the root \(-3+2\sqrt2\) strictly inside the unit disk.
Thus integer decimation alone does not preserve the original analytic and cyclotomic domain.
Its denominator in (6) still has no open-disk zero, so the output remains analytic there; zero-freeness is the property lost in (9).

There is nevertheless a complete threshold-two expense bound:
\[
 \boxed{\epsilon_2({\cal D}_nf)\le n\epsilon.}
 \tag{10}
\]
Indeed \(g_2\) is nondecreasing and, off the finite pole set,
\[
 g_2\!\left(\left|\frac1n\sum_jf(\zeta^jz)\right|\right)
 \le \max_jg_2(|f(\zeta^jz)|)
 \le \sum_jg_2(|f(\zeta^jz)|).
\]
Integrate over z; rotations preserve Haar measure and so does \(z\mapsto z^n\).
This proves (10) without a truncated Fourier series or an omitted singularity.

Even if a particular output still belongs to the original domain and has positive cost, (10) does not improve the old first-deviation scale automatically.
For example, if a captured deviation moves exactly from \(J=nJ'\) to \(J'\), combining the [v3 deviation bound](Yin_L_G0133_v3.md#first-deviation-degree-cost) for that output with (10) returns only
\[
 \epsilon>\frac1{1000nJ'}=\frac1{1000J}.
 \tag{11}
\]
This identifies the cancellation of that specific frequency gain by the available expense; it is not a claim that every multichannel decimation argument has the same limitation.

<a id="rotation-norm-and-threshold-cost"></a>
## Rotation norms preserve the cyclotomic domain but change the natural threshold

Define the multiplicative transform by
\[
 {\cal N}_nf(w)=\prod_{j=0}^{n-1}f(\zeta^jz)
              =\frac{B_n(w)}{A_n(w)},\qquad w=z^n,
 \tag{12}
\]
where
\[
 A_n(w)=\prod_jA_0(\zeta^jz),\qquad
 B_n(w)=\prod_jB_0(\zeta^jz).
\]
Formula (6) applies to both blocks.
Consequently \(A_n,B_n\) are monic reciprocal cyclotomic products with constant coefficient one and even degrees D,E, respectively.
This transform preserves the original domain, but the unreduced block degrees have not decreased.
Coincident powered roots retain their multiplicities.

Its natural expense is
\[
 \boxed{\epsilon_{2^n}({\cal N}_nf)\le n\epsilon.}
 \tag{13}
\]
To prove it, put \(u_j=g_2(|f(\zeta^jz)|)\ge0\).
For each j, \(|f(\zeta^jz)|\le2\cosh u_j\).
Repeatedly applying \(\cosh(u+v)\ge\cosh u\cosh v\) for nonnegative arguments gives
\[
 |{\cal N}_nf(z^n)|
 \le2^n\prod_j\cosh u_j
 \le2^n\cosh\!\left(\sum_j u_j\right).
\]
Apply \(g_{2^n}\) and integrate, retaining the same Haar-cover and rotation factors as in (10).

If threshold two is retained instead, put
\[
 C_n=\operatorname{arcosh}(2^{n-1}).
\]
Since
\[
 \cosh(C_n+\textstyle\sum_j u_j)
 \ge2^{n-1}\cosh(\textstyle\sum_j u_j),
\]
the same pointwise estimate yields
\[
 \boxed{\epsilon_2({\cal N}_nf)\le n\epsilon+C_n.}
 \tag{14}
\]
Here \(C_1=0\); for growing n the additive expense grows with n.
Neither (13) nor (14) returns a small threshold-two cost merely from small original \(\epsilon\).

An exact zero input proves that an additive issue is real, not only an artifact of this upper estimate.
Take
\[
 f(z)=1+z^2,\qquad \epsilon=0,\qquad
 {\cal N}_2f(w)=(1+w)^2.
 \tag{15}
\]
The transformed numerator is still an allowed monic reciprocal cyclotomic polynomial of even degree.
On the arc \(|\arg w|\le\pi/3\), of normalized measure \(1/3\),
\[
 |(1+w)^2|=4\cos^2(\arg(w)/2)\ge3.
\]
Thus
\[
 \epsilon_2({\cal N}_2f)
 \ge\frac13\operatorname{arcosh}(3/2)>0.
 \tag{16}
\]
In particular no inequality \(\epsilon_2({\cal N}_2f)\le C\epsilon_2(f)\), with finite C and valid for every original input, is possible.
This is a zero-to-positive domain-preserving control, not a positive-measure sequence tending to zero.

The opposite arithmetic extreme supplies no descent at all.
If n is coprime to the orders of all roots in \(A_0B_0\), taking n-th powers permutes each primitive-root set with its original multiplicity.
Since the polynomials are cyclotomic products, (6) gives
\[
 A_n=A_0,\qquad B_n=B_0,\qquad {\cal N}_nf=f.
 \tag{17}
\]
Thus avoiding every conductor prime leaves the entire rational function unchanged.

<a id="full-three-block-norm"></a>
## The norm of the full three-block object keeps its measure and all mixed terms

There is an exact norm operation on F itself:
\[
 {\cal R}_nF(w,y)=\prod_{j=0}^{n-1}F(\zeta^jz,y),
 \qquad w=z^n.
 \tag{18}
\]
This is a nonzero Laurent polynomial with integer coefficients in w and y.
To see integrality, its Laurent coefficients in z and y are algebraic integers in \(\mathbb Q(\zeta)\), fixed by every automorphism of that field because each such automorphism permutes the j factors.
They are therefore integers.
The product is also invariant under \(z\mapsto\zeta z\), so every occurring z exponent is divisible by n, including negative exponents.

The complete logarithms in (18) are integrable by the original v3 argument.
Finite additivity of the logarithm and the Haar-cover identity give exactly
\[
 \boxed{m_2({\cal R}_nF)=n\,m_2(F)=n\epsilon.}
 \tag{19}
\]
No boundary limit or varying-polynomial approximation is used.

However its y exponents have extreme values \(-n,n\), each with nonzero coefficient
\[
 \prod_j(\zeta^jz)^{-a}A_0(\zeta^jz).
\]
The y-width is therefore exactly \(2n\).
After multiplying by \(y^n\) one has a degree-\(2n\) polynomial in y, not the reciprocal quadratic used for threshold two in (3).
The product retains all elementary symmetric mixed terms in the rotated values of \(B/A\).
Replacing that product by a three-block expression built from \(A_n,B_n\) deletes these terms and is not justified by (19).
The zero control (15)--(16) explicitly separates those two operations: the full norm still has measure zero by (19), while the three-block object formed from the norm quotient has positive threshold-two cost.

<a id="no-growing-dilation-control"></a>
## A fixed-positive control with high-frequency escape and no growing common dilation

For every odd integer \(k\ge3\), take
\[
 A_0=1,\qquad
 B_{0,k}=(1+z^2)(1+z^{2k}),\qquad
 f_k=(1+z^2)(1+z^{2k}).
 \tag{20}
\]
These are allowed original inputs of even degree \(2k+2\).
Their four nonzero coefficients have absolute value one, so the [v3 four-term estimate](Yin_L_G0133_v3.md#first-deviation-degree-cost) gives
\[
 \frac1{256}\le\epsilon_2(f_k)\le\log4.
 \tag{21}
\]
The upper bound follows directly from \(|f_k|\le4\) and \(g_2(t)\le\log^+t\).

Locally in the disk, \(f_k\to q=1+z^2\), an exact zero-cost model.
On the circle,
\[
 \log|f_k|-\log|q|=\log|1+z^{2k}|.
 \tag{22}
\]
Its \(L^1\) norm is independent of k by Haar covering and is strictly positive.
The logarithm is not zero almost everywhere, for example on a sufficiently short arc around one.
Its nonzero Fourier frequencies are multiples of \(2k\), as follows from the logarithmic Fourier identity already justified in v3.
Thus (22) realizes exact escape beyond every fixed window with a persistent boundary difference.

The polynomial support is \(0,2,2k,2k+2\), whose gcd is always two.
Hence no growing power substitution in z represents these rational functions.
For the phase-balanced original block, the x frequencies are \(\pm(k+1),\pm(k-1)\), whose gcd is also two for odd k.
A fixed parity cover is present, but it does not account for the growing k.

Despite this genuine high-frequency difference, k-decimation gives
\[
 {\cal D}_kf_k(w)=1+w^2,\qquad
 \epsilon_2({\cal D}_kf_k)=0.
 \tag{23}
\]
Indeed k divides the support exponents zero and \(2k\), and does not divide 2 or \(2k+2\) when \(k\ge3\).
The output remains inside the original domain but has lost the positive cost.

The same-input rotation norm has the opposite behavior.
Since k is odd, squaring permutes the k-th roots of unity, and
\[
 \prod_{j=0}^{k-1}(1+\zeta_k^{2j}z^2)=1+z^{2k}=1+w^2.
\]
The second factor of \(f_k(\zeta_k^jz)\) is already \(1+w^2\) for every j.
Consequently
\[
 {\cal N}_kf_k(w)=(1+w^2)^{k+1}.
 \tag{24}
\]
On the set \(|\cos(\arg w)|\ge\sqrt3/2\), of normalized measure \(1/3\), one has \(|1+w^2|\ge\sqrt3\).
Using \(g_2(t)\ge\log(t/2)\) for \(t\ge2\) gives
\[
 \epsilon_2({\cal N}_kf_k)
 \ge\frac13\left(\frac{k+1}{2}\log3-\log2\right).
 \tag{25}
\]
This grows linearly while the original cost stays bounded as in (21).
The control is a fixed-positive-cost family, not a counterexample to the family gap or a constructed positive sequence with cost tending to zero.
It demonstrates two concrete losses of the tested transformations on inputs with high-frequency escape and no growing common dilation.
It does not preclude a different simultaneous use of residue channels or additional input information.

<a id="exact-descent-and-parity"></a>
## Exact descent has no measure expense but requires the complete support symmetry

Suppose the actual rational function satisfies
\[
 f(z)=h(z^n).
 \tag{26}
\]
Equivalently, its Taylor coefficients vanish at every index not divisible by n, or \(f(\zeta_nz)=f(z)\) identically.
The equivalence follows from its convergent Taylor series and the value \(f(0)=1\).
A finite initial window of zero coefficients does not establish (26).

First cancel any common cyclotomic factors of \(A_0,B_0\).
This leaves their quotient and \(\epsilon\) unchanged, and the corresponding common factor of F has zero logarithmic measure.
In each original block the multiplicities of both one and minus one as roots are even: the other roots pair with their inverses, the root product is one, and the total degree is even.
The common monic gcd therefore also has constant coefficient one, even degree and reciprocal symmetry, so cancelling it preserves these properties.
Write the reduced numerator and denominator as \(B_{\rm red},A_{\rm red}\), normalized to constant coefficient one.
They are monic reciprocal cyclotomic products.
The symmetry in (26) preserves their zero and pole divisors separately, because the reduced divisors are disjoint.
Comparison of constant coefficients then gives
\[
 A_{\rm red}(\zeta_nz)=A_{\rm red}(z),\qquad
 B_{\rm red}(\zeta_nz)=B_{\rm red}(z).
\]
Thus
\[
 A_{\rm red}(z)=\widehat A(z^n),\qquad
 B_{\rm red}(z)=\widehat B(z^n),
 \tag{27}
\]
where \(\widehat A,\widehat B\) have integer coefficients, are monic with constant coefficient one, and have respective degrees
\(\deg(A_{\rm red})/n,\deg(B_{\rm red})/n\).
Their roots are roots of unity, and reciprocity descends directly through (27).
No powered-root multiplicity is substituted for these actual reduced degrees.

Haar covering gives the exact cost equality
\[
 \boxed{\epsilon_2(h)=\epsilon_2(f).}
 \tag{28}
\]
To place h itself in the original three-block domain, the two descended degrees must also be even.
That condition is not automatic: \(f=1+z^2\) descends at n equal to two to \(h=1+w\), whose numerator has odd degree.
Replacing w by \(v^2\) restores even degrees and preserves the cost, but loses that factor two of the degree reduction.
This parity issue must be kept when returning to an integral phase-balanced Laurent polynomial.

For (20), the complete support gcd is two, so (26) admits no unbounded sequence of descent orders.
Neither eventual low-frequency Fourier agreement nor a long integer prefix can replace the exact global support condition.
This is the scope where direct descent succeeds without expense, and also its concrete boundary on the control above.

<a id="rescaling-retained-boundary"></a>
## Retained conclusion and author-check scope

Integer coefficient decimation preserves the arithmetic Taylor sequence and pays at most n times the original threshold-two cost, but generally loses the cyclotomic zero-free numerator and can erase positive cost even when the output domain survives.
Rotation norms preserve the original cyclotomic domain and all powered multiplicities, but their natural threshold is \(2^n\); keeping threshold two incurs the explicit additive expense in (14), and a zero input can become positive.
The norm of the entire Laurent object has exactly n times the original measure while retaining y-width \(2n\) and every mixed term.
Exact descent preserves cost but requires full support symmetry and the stated parity check.

These are precise arithmetic and analytic transformation boundaries for later use on different inputs.
The stronger C868 family statement and its assessment remain at their responsible Claim; no new open assignment for a positive vanishing-cost sequence in that family is made here.
No coverage of arbitrary original G0001 polynomials, pair-uniform finite-delay cutoff or unrestricted Mahler-gap conclusion is asserted.

The author checks covered the root-of-unity filter, numerator integrality despite division by n, all actual block degrees, the complete boundary inequalities, the threshold change, the zero-to-positive norm control, full-F integrality and y-width, the four-term no-growing-dilation control, and the exact support and parity requirements for descent.
No native mathematical program, numerical experiment, independent review or new external-source inspection supplies these deductions.
