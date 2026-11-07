---
author: Yin
---

# Independent review of the factor bounds for a fixed measure-one quadratic template

An independently assigned agent for Yin completed this review of C879 v1 at 2026-11-07T17:26 UTC.
The reviewer had no part in developing the proof and received no development dialogue, explanatory notes or earlier finding on C879.
The fixed proof, its arithmetic input and that input's pre-existing assessment and review were available.

<a id="fixed-template-whole"></a>
## Finding on the two factor bounds

For every fixed pair \(a,b\in\mathbb Z[i][z]\) satisfying the stated nonzero and measure-one hypotheses on \(a\), the entire argument proves a linear lower bound on factor degree and a positive logarithmic Mahler gap for sufficiently large \(N\).
Both estimates apply to each positive-measure irreducible factor in the respective coefficient fields.

The leading coefficient of \(a\) has modulus at least one, and the defining product for \(M(a)\) shows it is a unit and that no root is outside the unit circle.
After removing zero roots and normalizing, the constant coefficient has modulus at least one, forcing all remaining roots of \(a\) onto the circle.
In \(P_N=a_0(z)(z^{2N}+1)-z^{N-s}b(z)\), choosing \(N>s\) sufficiently large makes the shifted middle term affect neither leading nor constant coefficient.
The uniform coefficient bound therefore applies in both directions, giving a closed annulus independent of \(N\).
For roots away from the common zeros, the reverse triangle inequality gives \(e^{Nv}\le1+|b/a|\) even when the two powers have nearly opposite arguments.
On that annulus \(|r-1|\) bounds \(|\log r|\) from below up to a positive constant, and the angular chord bounds the least angular separation up to another positive constant.
Each linear factor of \(a_0\) therefore supplies the lower bound needed for the logarithmic pole estimate, including repetitions.
Common nonzero roots have \(v=0\), and a constant \(a_0\) gives a bounded quotient directly.
Splitting at \(v=1/N\) caps the logarithmic singularity at \(\log N\) even on a pole ray.

On a bounding ray without a polynomial zero, a suitable rotation has a real part with at most \(L\) nonzero monomials.
Descartes' rule bounds its distinct positive zeros by \(L-1\).
The continuous argument on each resulting interval stays in a half-plane of angular width \(\pi\), including endpoint limits, so the total net change on a ray is bounded by \(L\pi\).
The two circular arcs give the leading term of angular change and a vanishing inner contribution in the indicated limits.
The argument principle counts multiplicity, and outward perturbations count any roots on the boundaries with the same upper bound.
This verifies the sector estimate directly.
The union of pole-direction arcs then contains \(O(Ne^{-u}+1)\) roots for \(0<u\le\log N\).
Integrating the layer counts against \(ju^{j-1}\) gives \(O(N+(\log N)^j)=O(N)\) for \(j=2,3\).
The cutoff and the \(O(N)\) total root count yield unnormalized moments of orders \(N^{-1}\) and \(N^{-2}\), respectively, including all roots of the coefficient norm after doubling.

For an irreducible rational factor of the monic integral norm polynomial with constant term one, its monic minimal polynomial is integral and its constant term is a unit in \(\mathbb Z\).
Positive logarithmic measure excludes roots of unity throughout that factor.
The adopted [C855 v2 Part A](../../claims/Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04) and its [whole review](Yin_R_G1086_v1.md#raw-p2-whole) apply with the full rational degree \(d\) and every embedding.
The selected decision and R cover \(d\sum_i u_i^2\ge1/10\) for every nontorsion algebraic unit, and the later family versions and the repository erratum disclose no withdrawal of this input.
I checked this established result's scope and normalization at the application.
The second moment upper bound immediately yields \(d\ge N/(10C_2)\).
Independently using \(d\le BN\), the square of the same arithmetic lower bound gives \((10BN)^{-2}\le(\sum_i u_i^2)^2\).
Cauchy--Schwarz applied to \(|u_i|^{1/2}\) and \(|u_i|^{3/2}\) bounds this by \(2m(f)C_3/N^2\), since the unit product makes the positive logarithmic sum half the absolute sum.
This yields the claimed fixed gap with the stated rational constant.

For a Gaussian irreducible factor \(g\) and a root \(\alpha\), its minimal polynomial over \(\mathbb Q\) contains both \(g\) and its coefficient conjugate and divides \(g\bar g\).
If the conjugate is distinct their product is the rational minimal polynomial, while in the invariant case \(g\) itself belongs to \(\mathbb Q[z]\) and is irreducible there.
Thus degrees and logarithmic measures pass to \(g\) with a loss of at most two, and the rational minimal polynomial divides \(H_N\) in both cases.
The removed powers of \(z\) and scalar units have logarithmic measure zero.
For rational templates \(Q_N\) divides its coefficient norm, and \(N=2p\) gives the stated prime specialization.
The constants depend on the fixed pair, and this inspection uses C855 v2 at its adopted interface without a fresh review of its source proofs or a conclusion for varying templates.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole template theorem](#fixed-template-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole template theorem](#fixed-template-whole) | [C879 v1 statement](../../claims/Yin_C_G0879_v1.md#statement) | All large indices, fixed Gaussian templates, both coefficient fields, each positive-measure factor and the prime specialization. |
| [Whole template theorem](#fixed-template-whole) | [C879 v1 radial bound](../../claims/Yin_C_G0879_v1.md#root-moments) | Endpoint normalization, annulus, common or absent pole roots, logarithmic displacement and cutoff. |
| [Whole template theorem](#fixed-template-whole) | [C879 v1 sector count](../../claims/Yin_C_G0879_v1.md#angular-count) | Descartes and the sector argument principle, multiplicity and boundary rays, integrated second and third moments of the whole norm polynomial. |
| [Whole template theorem](#fixed-template-whole) | [C879 v1 factor bounds](../../claims/Yin_C_G0879_v1.md#factor-bounds) | Actual-degree unit inequality from C855 v2 Part A, second and third moments, rational and Gaussian irreducible factors, and both quantitative bounds. |
