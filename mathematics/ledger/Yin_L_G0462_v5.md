---
author: Yin
---

# Probability laws from surface monodromy and rotating integral symplectic matrices

<a id="scope"></a>
## The probability question

The [unrestricted Task](../tasks/Yin_T_G0001_v1.md#contract) permits proving that, for every \(\varepsilon>0\), a law on actual integer polynomials gives positive probability to \(1<M(P)<1+\varepsilon\).
The [fixed-shell amplification](../claims/Yin_C_G0870_v2.md#amplification) already shows that conditional probability tending to one can be caused by a single positive measure.
The present exploration asks for a different source of integer polynomials and for a discriminating test of its whole measure.
The [Salem quotient obstruction](Yin_L_G0462_v4.md#cross-field-fibers) and its radical qualification remain at their previous scope.

Agent-S developed the comparisons below for Yin on 9 November 2026.
The topology assertion and its complete proof are retained separately in [C883](../claims/Yin_C_G0883_v1.md#statement), with its actual selected assessment governing use.
The proposed symplectic sampling law is an exploratory candidate and has no established near-one witness or positive-probability lower bound.

<a id="topological-law"></a>
## A surface-monodromy law and its first test

For a closed connected orientable surface \(S_g\), an orientation-preserving homeomorphism gives an integral symplectic action \(A_f\) on \(H_1(S_g;\mathbb Z)\).
The output \(P_f(t)=\det(tI-A_f)\) is monic integral reciprocal with constant one.
Choose any finite or countable collection of pseudo-Anosov mapping classes, any probability law on that collection, and output this whole characteristic polynomial.
Let
\[
 E_\varepsilon=\{f:1<M(P_f)<1+\varepsilon\}.
\]
If the chosen collection has a fixed bound \((2g-2)\log\lambda(f)\le C\), the [topological gap](../claims/Yin_C_G0883_v1.md#bounded-normalized-entropy) makes \(\mathbb P(E_\varepsilon)=0\) for every \(0<\varepsilon\le e^{\eta_C}-1\), for every such law.

The original attraction of this construction was the availability of geometric stretch factors approaching one on growing surfaces.
The homological spectral radius is at most the geometric stretch factor, while the full measure satisfies
\[
                  m(P_f)\le N_+(f)\log\lambda(f),
\]
where \(N_+(f)\) counts all expanding homological eigenvalues with multiplicity.
The inequality by itself leaves the expanding count unpaid.
C883's exact Alexander specialization and puncture-filling argument settles the entire bounded-normalized-entropy attempt, including all the remaining conjugates.

Thus any sequence of positive whole homological measures tending to zero must have \((2g-2)\log\lambda(f)\to\infty\).
The conclusion concerns the chosen pseudo-Anosov realizations.
It does not give a restriction on all integral reciprocal polynomials, or a lower bound for a separately extracted irreducible factor of a larger characteristic polynomial.
Letting a probability law mix arbitrarily large normalized-entropy bounds leaves the required positive probability unresolved.

The exact external inputs and their checked scope are in [C883](../claims/Yin_C_G0883_v1.md#external-inputs).
[FLM11](../audits/literature/FLM11/readme.md) was inspected at its finite-mapping-torus theorem.
[DGT23](../audits/literature/DGT23/readme.md) was inspected at its general graph-map Alexander specialization, including the exact characteristic-polynomial normalization.
The [DS17 fixed-support input](../audits/literature/DS17/Yin_U001.md#ds17-u001) retains its existing accepted external scope.

<a id="rotating-symplectic-law"></a>
## An ensemble with a growing number of coupled twists

For integers \(g\ge3\) and even \(2\le k\le g\), let \(S_g\) cyclically permute the standard basis of \(\mathbb Z^g\), and put \(R_g=\operatorname{diag}(S_g,S_g)\).
Choose uniformly one \(k\)-element subset \(I\) of \(\{1,\ldots,g\}\).
On that subset choose independently and uniformly two sign vectors, each having exactly \(k/2\) plus signs and \(k/2\) minus signs.
Indices are taken modulo \(g\).
Set
\[
 \begin{split}
 v_i&=e_i-e_{i+1},\qquad w_i=e_i+e_{i+1},\\
 D&=\sum_{i\in I}\epsilon_i v_i v_i^{\mathsf T},\qquad
 E=\sum_{i\in I}\eta_i w_i w_i^{\mathsf T},\\
 U(D)&=\begin{pmatrix}I&D\\0&I\end{pmatrix},\qquad
 L(E)=\begin{pmatrix}I&0\\E&I\end{pmatrix},\\
 A&=R_gU(D)L(E),\qquad P_{g,k}(t)=\det(tI-A).
 \end{split}                                                     \tag{1}
\]
The matrices \(D,E\) are integral symmetric.
Direct multiplication against the standard skew form shows that \(U(D),L(E)\) and \(R_g\) are integral symplectic matrices.
Consequently every sampled output is a monic reciprocal integer polynomial of degree \(2g\), with constant one.
An elementary outcome has probability
\[
       \binom{g}{k}^{-1}\binom{k}{k/2}^{-2}>0.
\]
Different elementary outcomes may yield the same polynomial, which increases that polynomial's mass.
A countable mixture giving positive weight to selected pairs \((g,k)\) therefore gives positive probability to every polynomial supplied by those finite laws.
This specifies the discrete probability space without assuming a small-shell outcome.

The intended exploration takes \(k\to\infty\) and \(k=o(g)\).
The number of active local twists then grows, and the matrices couple adjacent handles through both the plus and minus directions.
The candidate changes the construction input from free coefficients or prescribed scalar residue signs to symplectic integral dynamics.
No fixed-template theorem has been shown to cover this entire growing family, and no claim of escape from all existing obstructions is made.

The tentative mechanism is to dilute a growing collection of interacting local perturbations around a long integral rotation while using their signed interactions to reduce the number of expanding modes.
For the actual output, let \(N_+(A)\) count eigenvalues of modulus greater than one with multiplicity.
Then
\[
                 m(P_{g,k})\le N_+(A)\log\rho(A).
 \tag{2}
\]
A hypothetical bound \(\log\rho(A)=O(k/g)\), together with \(0<N_+(A)=o(g/k)\), would make the full positive measure tend to zero.
Neither bound has been established for (1).
Small spectral radius alone does not furnish a whole-measure estimate.

<a id="separable-control"></a>
## An exact control that rejects spectral-radius dilution alone

Keep the rotation \(R_g\), but use \(D=d\,e_1e_1^{\mathsf T}\) and \(E=e\,e_1e_1^{\mathsf T}\) with fixed integers \(d,e\).
After grouping the two coordinates of each handle, this is a cyclic block shift with identity weights except for
\[
                      W=\begin{pmatrix}1+de&d\\e&1\end{pmatrix}.
\]
Following an eigenvector through a full cycle gives the block characteristic equation \(\det(t^gI_2-W)=0\).
Thus the complete characteristic polynomial is
\[
                    P_g(t)=t^{2g}-(2+de)t^g+1.                       \tag{3}
\]
If \(|2+de|\le2\), all roots have modulus one.
If \(|2+de|>2\), exactly \(g\) roots are outside the circle and
\[
 \log\rho(A)=\frac1g\operatorname{arcosh}\frac{|2+de|}{2},
 \qquad
 m(P_g)=\operatorname{arcosh}\frac{|2+de|}{2}.
\]
The exact positive cost is independent of \(g\).
This control explains why the coupled model must change the exterior-root count or its full radial distribution.
Choosing the principal eigenvalue closer to one does not achieve that change.

<a id="discriminating-test"></a>
## The bounded first investigation

[J153](../computations/programs/Yin_J_G0153/readme.md) owns the completed finite computation for the coupled law, its exact matrices and reproducible outputs.
The tested window uses \(g=12,24,48\), even \(k=2,4,8\) and eight labelled samples at each pair, for 72 labelled inputs.
The exact seeded rule and complete characteristic polynomials are retained in its [program](../computations/programs/Yin_J_G0153/rotating_shears.py).
Each matrix was checked exactly against the symplectic form, and each full characteristic polynomial was checked for reciprocity.
FLINT root balls at 256-bit precision enclosed the product of all factors \(\max(1,|\alpha|)\), counting their multiplicities and checking the full degree.
All 24 inputs whose product did not certify strict positivity were factored exactly, and every irreducible factor was cyclotomic.
The remaining 48 inputs have strictly positive measure.
Their smallest complete measure, at \((g,k,\mathrm{sample})=(12,8,6)\), lies in
\[
                  1.75487766624669<M<1.75487766624670.
\]
The program separates that positive minimum from the other positive outputs by their certified intervals, allowing identical characteristic polynomials.
The numerical house for this input is about \(1.15096\), with six numerically expanding roots.
These latter diagnostics are distinguished from the rigorous complete-measure enclosure.
The exact cyclotomic check also resolves inputs with misleading floating-point logarithmic measures of order \(10^{-5}\).
The finite result provides no positive measure near the current small-measure seeds and establishes no trend towards one.

Compare the coupled matrices with (3) using the entire sum of positive radial logarithms.
If the expanding roots occupy a positive proportion of the degree while their radii have only the proposed \(k/g\) scale, the dilution mechanism has supplied no shrinking total cost.
If the smallest certified positive measures stabilize or increase on the selected window, return that negative evidence before enlarging the sample count.
An isolated decrease would motivate a narrower structural investigation of the responsible sign pattern and invariant subspaces.
It would supply no probability lower bound at smaller radii and no asymptotic sequence.

The immediate unresolved obligation is to find an actual signed interaction producing both low complete exterior cost and a scalable reason for its persistence.
