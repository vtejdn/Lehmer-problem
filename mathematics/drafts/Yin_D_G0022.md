---
author: Yin
---

# Integer four-off-circle sources and the single-terminal-cut prefix cell

This is ordinary bounded Preparation for the integer construction problem, not an independent review.
The [adopted C881 v8 interface](../claims/Yin_C_G0881_v8.md#statement) requires a nontorsion trace in the shrinking left endpoint interval and exactly one conjugate pair of nonreal exterior roots.
Two existing integer cores meet that exterior-root shape, but neither supplies the current cell: the certified degree-18 core already has full measure greater than \(6/5\), and both it and the degree-10 central-minus-one core have an explicit fixed gap from the required endpoint at large conductor.
The subsequent comparison tests a parameterized central perturbation and Gaussian integral Hermitian constructions for an actual change of noncyclotomic core with controlled complete measure.
The unresolved supply question is not restricted to the prefix cell when returning to the original G0001 contract.
The exact new arithmetic and the finite discrimination of that proposal are retained below.
This new use of the available D22 address inherits no earlier Draft content or assessment.

<a id="target-interface"></a>
## Fixed target and actual source scope

Use the original odd grid
\[
p=2n+1\ge5,\qquad b_j=2\cos(2\pi j/p),\qquad
Q=tB_n+C,\qquad P(z)=z^{n+1}Q(z+z^{-1}),
\]
with \(x=0\), \(a_0=2\), \(r_1,\ldots,r_{n-1}>0\), \(r_n<0\), and the strict endpoint \(Q(-2)/B_n(-2)<0\).
All canonical coefficients \(a_i\) are integers.
The complete necessary consequences are those of [C881 v8](../claims/Yin_C_G0881_v8.md#endpoint-nontorsion) and its [nonreal-pair argument](../claims/Yin_C_G0881_v8.md#nonreal-exterior-pair).
In particular, some trace lies in
\[
I_p=(-2,-2\cos(\pi/p)),
\tag{1}
\]
every trace in this interval is nontorsion, there is no real trace above \(b_1\), and exactly two conjugate nonreal roots are exterior.
The [prefix identity](../claims/Yin_C_G0881_v3.md#prefix-coordinates) requires
\[
P(z)=1+z+4z^2+O(z^3)
\tag{2}
\]
already at length two.
At length 140 the complete upper bound is \(M(P)\le568^{1/35}<6/5\).
No existence assertion is inferred from these necessary conditions.

The bounded local inspection used the retained [Mos26 table scope](../audits/literature/Mos26/readme.md), the original degree-18 row and [J144 exact control](../computations/programs/Yin_J_G0144/trace_control.py), [L457 v2](../ledger/Yin_L_G0457_v2.md#cyclotomic-central-minus-one-scope) and the [J138 reproduction scope](../computations/programs/Yin_J_G0138/readme.md).
The table's “smallest known” row is an example record, not a theorem giving a universal lower bound for two exterior roots.
The degree-44 completeness input used in [J149](../computations/programs/Yin_J_G0149/readme.md#core-coverage) remains at that degree bound and is not extended to the present large conductors.

Additional already retained comparisons were read at their displayed construction scopes: [J149's degree-16 integer atom](../computations/programs/Yin_J_G0149/readme.md#nonunit-atom), the [C488/L203 pendant-chain family](../claims/Yin_C_G0488_v1.md#bounded-measure-chain-root-control), and [L464 v4's moving rational cut](../ledger/Yin_L_G0464_v4.md#moving-rational-family).
Their limited applicability is recorded below without rerunning their programs.
The initial local source comparison performed no new sampling, MIP, root approximation, full-library mathematical census or external source acquisition.
Its new arithmetic was the small exact polynomial check reproduced in this Draft; the subsequent J138 and Gaussian investigations have their own stated scopes below.
The [J159 rational large-conductor witnesses](../computations/programs/Yin_J_G0159/readme.md#question) were read only as target context; their nonintegral coefficients are not an integer source.

<a id="degree-eighteen-core"></a>
## The certified degree-18 core

The original degree-18, two-exterior-root table row has leading-to-central coefficients
\[
(1,1,1,0,0,-1,0,-1,0,-1).
\]
Equivalently its complete reciprocal polynomial is \(F_{18}(z)=z^9T_{18}(z+z^{-1})\), where
\[
T_{18}(t)=
t^9+t^8-8t^7-8t^6+20t^5+19t^4-16t^3-13t^2+2t+1.
\tag{3}
\]
These are the actual inputs of [J144's rational control](../computations/programs/Yin_J_G0144/trace_control.py), not rounded reconstructed coefficients.

That existing control accounts for seven real trace roots in the disjoint intervals
\[
(-1.46,-1.45),\ (-0.78,-0.77),\ (-0.25,-0.24),\
(0.32,0.33),\ (1.05,1.06),\ (1.65,1.66),\ (1.99,2).
\]
It places the remaining upper-half-plane trace in the disk centered at
\[
(-177624+8576i)/100000
\]
of radius \(1/100000\), with its conjugate accounting for the final trace.
The exact lift and rational Rouché/ellipse inequalities in the control give
\[
(109606/100000)^2<M(F_{18})<(10961/10000)^2,
\]
hence
\[
1.2013475236<M(F_{18})<1.20143521.
\tag{4}
\]
The root-shape and full-measure certificate are existing J144 evidence.
This Preparation read that complete short control but did not rerun its Rouché verification.
Equation (4), rather than the table's decimal label, is the strict comparison used here.

Thus \(F_{18}\) is a concrete integer source with the required exterior-root shape, but its full measure is too large for the length-140 target.
Cyclotomic multiplication, a sign substitution, or a monomial substitution preserves its complete Mahler measure and cannot fix that failure.
For the bare polynomial, its first three coefficients are \(1,1,1\), contradicting (2); \(F_{18}(-z)\) already has coefficient \(-1\) at \(z\).
These bare-prefix observations do not pretend that cyclotomic multiplication preserves a coefficient prefix.

A second obstruction is independent of that measure comparison.
Direct exact evaluation gives
\[
T_{18}(-2)=-7,\qquad T_{18}(2)=1,
\qquad
\sup_{[-2,2]}|T'_{18}|
 \le\sum_{k=1}^{9}k|[t^k]T_{18}|2^{k-1}=10902.
\tag{5}
\]
The endpoint argument below shows that both \(F_{18}(z)\) and \(F_{18}(-z)\), even after arbitrary cyclotomic multiplication, cannot supply (1) for any odd \(p\ge329\).
This covers both current conductors 1009 and 2003.

<a id="degree-ten-core"></a>
## A central-minus-one integer core with the correct root shape

For odd squarefree \(N\) with at least two prime factors, [L457 v2](../ledger/Yin_L_G0457_v2.md#central-minus-one-trace-reduction) studies the actual integer family
\[
G_N(z)=\Phi_N(z)-z^{\varphi(N)/2}.
\tag{6}
\]
It proves that the only real roots are the double roots at \(1\) and \(-1\).
The raw family therefore fails the strict endpoint \(P(-1)>0\).
Removing its complete cyclotomic part preserves the whole measure but produces a different actual polynomial, whose original grid conditions still need checking.

At \(N=35\), the [existing exhaustive exact extraction](../ledger/Yin_L_G0457_v2.md#central-minus-one-exhaustive-cyclotomic-test) is
\[
G_{35}
=\Phi_1^2\Phi_2^2\Phi_3\Phi_4\Phi_6\Phi_8\,F_{10},
\qquad
F_{10}(z)=z^{10}-z^9+z^5-z+1.
\tag{7}
\]
L457/J138 already retain the complete factor identity, cyclotomic exhaustion and irreducibility of \(F_{10}\).
The existing numerical estimates of its measure are not interval certificates and are not used for a strict \(6/5\) comparison here.

The new exact root-shape check is particularly short.
Write
\[
F_{10}(z)=z^5T_{10}(z+z^{-1}),\qquad
T_{10}(t)=t^5-t^4-5t^3+4t^2+5t-1.
\tag{8}
\]
Its exact values are
\[
\begin{array}{c|rrrrr}
t&-2&-1&0&1&2\\ \hline
T_{10}(t)&-3&1&-1&3&1
\end{array},
\qquad \operatorname{disc}(T_{10})=-18583.
\tag{9}
\]
The sign changes give three distinct real roots in \((-2,-1),(-1,0),(0,1)\).
The nonzero discriminant makes all five roots simple.
For a real polynomial with simple roots the sign of its discriminant is \((-1)^s\), where \(s\) is the number of nonreal conjugate pairs.
There can be at most one such pair after the three real roots already found, and the negative sign forces exactly one.
Thus the three displayed roots are all the real trace roots.

Each trace in \((-2,2)\) lifts to two unit-circle roots.
A nonreal trace lifts to two reciprocal roots, neither real nor on the unit circle, exactly one exterior.
Conjugation pairs the exterior lifts of the nonreal trace pair.
Consequently \(F_{10}\) has precisely two nonreal conjugate exterior roots, two reciprocal interior roots and six unit-circle roots.
Its unit-circle roots are nontorsion, because the exact irreducible noncyclotomic polynomial (7) has no cyclotomic divisor.
This supplies a genuine integer example of the necessary four-off-circle geometry, distinct from a single Salem seed.

The original target bridges still fail.
The bare \(F_{10}\) has coefficient \(-1\) at \(z\); \(F_{10}(-z)\) has coefficient \(1\) at \(z\), but coefficient \(0\) at \(z^2\), contradicting (2).
More decisively for any proposed padding at the current large conductors,
\[
T_{10}(-2)=-3,\qquad T_{10}(2)=1,\qquad
\sup_{[-2,2]}|T'_{10}|
\le\sum_{k=1}^{5}k|[t^k]T_{10}|2^{k-1}=193.
\tag{10}
\]
Both signs have no trace in the required interval for every odd \(p\ge45\), as proved next.

<a id="fixed-core-endpoint-obstruction"></a>
## Why a fixed complex-pair core cannot supply the shrinking endpoint by padding

Let \(F(z)=z^dT(z+z^{-1})\) be a fixed reciprocal polynomial with
\[
\eta=\min\{|T(-2)|,|T(2)|\}>0,\qquad
D_T=\sum_{k\ge1}k|[t^k]T|2^{k-1}>0.
\]
The elementary mean-value estimate gives no zero of \(T\) in either endpoint strip of width \(w\) whenever \(D_Tw<\eta\).
For the target interval,
\[
w_p=2(1-\cos(\pi/p))<(\pi/p)^2<(22/(7p))^2.
\tag{11}
\]
Hence
\[
D_T\,484<49p^2\eta
\tag{12}
\]
is an explicit sufficient condition excluding traces of both \(F(z)\) and \(F(-z)\) from \(I_p\).
Reflection \(z\mapsto-z\) changes every trace \(t\) to \(-t\), so the two endpoint strips cover both signs.

For (3), condition (12) holds at \(p=329\), since
\[
484\cdot10902=5276568<5303809=49\cdot329^2.
\]
For (8), it holds at \(p=45\), since
\[
484\cdot193=93412<99225=49\cdot45^2.
\]
It remains true as \(p\) increases.
These are sufficient thresholds, not claims about the first conductor at which each exclusion becomes true.

If an actual target were \(H(z)F(\varepsilon z^k)\), with \(H\) cyclotomic and \(F\) one of these two-exterior cores, then the full exterior-root count, with multiplicity, would be \(2k\).
The C881 v8 count forces \(k=1\).
The endpoint lift cannot be supplied by \(H\), by the [nontorsion endpoint theorem](../claims/Yin_C_G0881_v8.md#endpoint-nontorsion).
It must therefore come from \(F(\varepsilon z)\), which (12) excludes.
No cancellation is involved in an actual polynomial product.
This explains the endpoint failure for these fixed complex-pair cores even without invoking the separate [single-Salem-seed exclusion](../claims/Yin_C_G0881_v8.md#salem-seed-exclusion).

More generally, any finite collection of fixed reciprocal cores with no roots at \(1\) or \(-1\) has fixed neighborhoods of the two endpoints containing none of its real traces.
It therefore cannot supply such an endpoint as \(p\) tends to infinity by cyclotomic multiplication alone.
A successful integer source must change the noncyclotomic core; merely presenting the same core in a larger degree does not address this condition.

<a id="bounded-comparison-limits"></a>
## Other already-read comparisons and limits

The [J149 degree-16 atom](../computations/programs/Yin_J_G0149/readme.md#nonunit-atom),
\[
1+\sum_{j=3}^{13}z^j+z^{16},
\]
already has one nonreal exterior pair and \(P(-1)=1\).
Its actual odd-grid chamber at \(p=15\) has five negative residues and shift one, and its complete measure lies in \((1.272,1.274)\).
It is therefore a useful example that endpoint positivity and the root shape can coexist integrally, but it is not the one-negative-node, zero-shift, small-measure target.
Its zero coefficient at \(z\) also fails (2).
No transfer from that chamber to the current one is established.

The [C488 pendant-chain source](../claims/Yin_C_G0488_v1.md#pendant-chain-full-determinant),
\[
p_k(z)=\frac{z^{k+2}(z^3+6z^2+21z+12)
 -(1+6z+21z^2+12z^3)}{z-1},
\]
changes the positive-measure core and supplies unbounded degrees.
The existing [all-\(k\) argument](../claims/Yin_C_G0488_v1.md#bounded-measure-chain-root-control) gives exactly one nonreal exterior pair, but with common modulus greater than two, hence complete \(M(p_k)>4\).
That decisive bound excludes the length-140 target.
The [Hir06 local source note](../audits/literature/Hir06/readme.md) supports its existing Salem--Boyd attribution at the retained scope; no new theorem is imported from the external source in this Preparation.

The [L464 v4 integer moving-cut family](../ledger/Yin_L_G0464_v4.md#moving-rational-family) also changes the core and eventually has one nonreal exterior pair.
It uses \(B=U_{d-1}(t/2)\), a different grid, with cut \(c=1/m>0\), signed residue total \(K\sim4m^{d-2}\), and [full measure \(M(P)\sim K\)](../ledger/Yin_L_G0464_v4.md#variation-and-whole-measure).
It does not preserve the odd-grid one-terminal-negative cell, \(K=a_0=2\), or the shrinking full-measure bound.
This identifies a concrete denominator-clearing cost, not an integer solution of the present problem.

None of these comparisons proves a universal positive gap for all polynomials with one nonreal exterior pair.
In particular, the record \(1.201396\ldots\) is not promoted to such a theorem.
The inspected sources provide no integer input for the required length-140 cell.

<a id="exact-check-reproduction"></a>
## New exact arithmetic and reproduction

The root-shape deduction (8)--(10) and the explicit endpoint thresholds (5), (10)--(12) are new ordinary author calculations in this Preparation.
They are not attributed to the prior root-count screens or called an independent review.
The existing factorization at \(N=35\) was additionally checked with exact rational factorization, which returned one degree-ten factor with multiplicity one.
No numerical Mahler roots were computed.

The following excerpt reproduces the executed exact calculations, using Python 3.14 and the already installed python-flint package available under the J156 ignored package directory.
Coefficients below are in ascending order.
It contains all new computational inputs; the mean-value, discriminant-sign and reciprocal-lift arguments are given above.

~~~python
from flint import fmpz_poly

t10 = fmpz_poly([-1, 5, 4, -5, -1, 1])
f10 = fmpz_poly([1, -1, 0, 0, 0, 1, 0, 0, 0, -1, 1])
t18 = fmpz_poly([1, 2, -13, -16, 19, 20, -8, -8, 1, 1])

def derivative_bound(poly):
    return sum(
        k * abs(int(poly[k])) * 2 ** (k - 1)
        for k in range(1, int(poly.degree()) + 1)
    )

assert int(t10.discriminant()) == -18583
assert [int(t10(t)) for t in [-2, -1, 0, 1, 2]] == [-3, 1, -1, 3, 1]
assert [(int(f.degree()), int(e)) for f, e in f10.factor()[1]] == [(10, 1)]
assert (int(t18(-2)), int(t18(2))) == (-7, 1)
assert derivative_bound(t10) == 193
assert derivative_bound(t18) == 10902
assert 484 * 193 < 49 * 45 ** 2
assert 484 * 10902 < 49 * 329 ** 2
~~~

The executed evaluations returned precisely the displayed discriminant, five signs, factor-degree/multiplicity pair, endpoint values and derivative sums.
The final two integer comparisons are explicitly expanded in the proof.
The excerpt consolidates those same inputs into assertions; it does not claim a separate second run.
The irreducibility check uses FLINT's factorization implementation and is an ordinary same-system check, not an independently implemented factorization algorithm.

<a id="next-core-changing-question"></a>
## A core-changing discrimination and its finite outcome

Continue, if this branch is allocated further work, with the core-changing family (6), rather than padding \(F_{10}\).
Let
\[
N_s=\prod_{j=1}^{s}q_j,\quad s\ge2,\qquad
q_1=3,\ q_2=5,\ q_3=7,\ldots,
\qquad
F_s=\frac{\Phi_{N_s}-z^{\varphi(N_s)/2}}
            {\text{its complete cyclotomic factor with multiplicities}}.
\tag{13}
\]
The whole noncyclotomic residual is retained in (13), even when reducible.
Removing only proven cyclotomic factors preserves its full measure exactly.
The fixed-prime-count sparse-completion obstruction in [L457 v2](../ledger/Yin_L_G0457_v2.md#bounded-prime-count-completion) rules out a positive-to-zero sequence when the number of prime factors remains bounded, so a proposed asymptotic use must let \(s\) grow.
Equation (13) changes the integer polynomial and potentially its entire positive-measure core as \(s\) changes; it is not a substitution or padding of a fixed core.

The first concrete parameter selected from the retained work is \(N_4=1155\).
Its complete cyclotomic block and degree-446 residual are [fixed in L457 v2](../ledger/Yin_L_G0457_v2.md#central-minus-one-exhaustive-cyclotomic-test).
The exact whole residual to test is
\[
F_4(z)=
\frac{\Phi_{1155}(z)-z^{240}}
{\Phi_1^2\Phi_2^2\Phi_3\Phi_4\Phi_5\Phi_6\Phi_8\Phi_{10}\Phi_{12}\Phi_{24}}.
\tag{14}
\]
The historical generated J138 output was absent from its recorded location at the initial comparison, so it was not used as a native coefficient input.
The [retained exact-generation program](../computations/programs/Yin_J_G0138/center_one.py) and the fixed identity (14) suffice to regenerate the vector without repeating the numerical boundary-grid experiment.
Construct numerator and denominator over \(\mathbb Z[z]\), verify exact division and reconstruction, and form the degree-223 integer trace polynomial.
At its own degree the candidate odd-grid conductor is \(p=445\).

The next finite question is whether either sign of that entire residual has precisely one nonreal conjugate trace pair, all other traces in \((-2,2)\), at least one trace in \(I_{445}\), and no real trace above \(2\cos(2\pi/445)\).
Exact real-root counts, multiplicities and comparisons against the algebraic grid endpoints can decide these necessary root conditions without Mahler root approximation, random sampling or MIP.
A count incompatible with one nonreal pair rejects this particular member immediately.
Passing those conditions would still require the original shift, \(a_0=2\), complete strict residue mask, endpoint and length-140 prefix; it would not itself establish an input.
The existing uncertified measure estimate for \(N=1155\) supplies no positive evidence for passing the small-measure bound.

The main researcher subsequently executed the exact root-count discriminator in [J138](../computations/programs/Yin_J_G0138/readme.md#degree446-exact-root-shape), preserving its new native program and complete generated coefficients there.
It finds 119 real trace roots, all in \((-2,2)\), and 104 nonreal trace roots, hence 104 exterior roots of the entire quotient.
This fails the necessary two-exterior-root condition, so no finer angular endpoint test was needed for this member.
The result and its actual review relationship belong to J138; this ordinary source Preparation is not an independent review of that computation.
The [independently reviewed factorization and complete measure](../computations/programs/Yin_J_G0138/readme.md#degree446-factor-and-measure) further show that this residual is irreducible and has \(2.10642510401468<M<2.10642510401469\).
There is therefore no proper rational factor of this particular residual to extract as a different small-measure candidate.
The failure does not exclude every later \(N_s\), while the successful degree-ten root-shape example does not establish that any later member works.
Increasing \(s\) again has no demonstrated mechanism for preserving the required exterior-root count.

<a id="gaussian-hermitian-comparison"></a>
## Gaussian Hermitian realization and complete measure

This continuation is ordinary author Preparation, not an independent review or a proved Claim assessment.
It compares a Gaussian integral Hermitian realization with the unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract), without imposing the earlier prefix cell on that original objective.
The new calculations below give a complete exterior-root count and a restriction on one explicit single-kick cyclic family.
They do not supply a sequence of positive total logarithmic Mahler measures tending to zero.
The first missing construction input is an actual changing integer core whose complete measure decreases; the existence of small loxodromic elements is not an input to this Preparation.

The [Gaussian norm equivalence in L458 v3](../ledger/Yin_L_G0458_v3.md#gaussian-norm-counterexample-equivalence) already shows why Gaussian coefficients and self-inversiveness alone can retain the original difficulty.
The exact family in [C877 v1](../claims/Yin_C_G0877_v1.md#statement) has a different, fixed-template obstruction and does not cover all integral Hermitian isometries.
The extra information considered here is Hermitian negative index one, which controls the number of expanding eigenvalues.
Its realification has negative index two, so the [fixed-count theorem C885 v8](../claims/Yin_C_G0885_v8.md#statement), whose ambient form has one real hyperbolic plane, does not apply directly.
No extension of that theorem to arbitrary Hermitian words is asserted.

<a id="gaussian-hermitian-source-scope"></a>
## Inspected primary matrix interface and limits

The consulted work is Elisha Falbel, Gabor Francsics, Peter D. Lax and John R. Parker, *Generators of a Picard modular group in two complex dimensions*, Proceedings of the American Mathematical Society 139 (2011), 2439--2447, [DOI 10.1090/S0002-9939-2010-10653-6](https://doi.org/10.1090/S0002-9939-2010-10653-6).
The actual inspected edition is the [ten-page author PDF](https://users.math.msu.edu/users/franci86/FaFrLaPa-gen-d1-arXiv.pdf), whose title page is dated September 30, 2009; publication identity was checked against the [institutional record](https://durham-repository.worktribe.com/output/1508162).
The text reading covers PDF/printed pp. 2--6: form (2), the Section 2 Heisenberg matrices, Theorem 1 and Lemma 1.
No local original acquisition, confirmed page-image inspection, whole-source proof audit or independent review is claimed here.
The later source Preparation is retained separately in [FFLP11-U001](../audits/literature/FFLP11/Yin_U001.md#fflp11-u001), with the acquired arXiv v1, its selected-passage correspondence, visual inspection and the actual failed author-host download recorded at that responsible source home.
That later acquisition does not retrospectively change the initial strategy delegate's reading depth.

Theorem 1 gives four generators for \(SU(2,1;\mathbb Z[i])\), with a constructive Euclidean decomposition.
Lemma 1 gives cusp-stabilizer parameters \(\delta=1\), \(\beta\in\{1,i,-1,-i\}\), \(r\in\mathbb Z\), \(\gamma\in\mathbb Z[i]\), and \(|\gamma|^2\in2\mathbb Z\).
Page 4, after (5), warns that general Langlands factors need not be integral even when the original matrix is integral.
These passages give neither a higher-dimensional integral normal form with bounded word length nor small spectral radii.
The block extension below is a direct author calculation, not a higher-dimensional generation theorem attributed to this source.

<a id="gaussian-hermitian-root-count"></a>
## Signature proof of the complete norm-polynomial cost

Let \(H\) be a nonsingular Hermitian matrix of signature \((d-1,1)\), and let \(A\in M_d(\mathbb Z[i])\) satisfy \(A^*HA=H\).
The determinant identity gives \(|\det A|=1\), so its Gaussian integral determinant is a unit and \(A^{-1}\) is Gaussian integral.
Write coefficient conjugation with a bar, and set
\[
g_A(z)=\det(zI-A),\qquad P_A(z)=g_A(z)\overline{g_A}(z).
\tag{G1}
\]
The polynomial \(g_A\) is monic over \(\mathbb Z[i]\).
The coefficients of \(P_A\) are Gaussian integers fixed by conjugation, hence integers; its leading and constant coefficients are one.
It is also the full characteristic polynomial of the integral realification of \(A\).

Let \(E_+\) be the direct sum of all generalized eigenspaces for eigenvalues of modulus greater than one.
For \(x,y\in E_+\), both \(A^{-k}x\) and \(A^{-k}y\) tend to zero, including the polynomial factors coming from Jordan blocks.
Form invariance gives
\[
x^*Hy=(A^{-k}x)^*H(A^{-k}y)\longrightarrow0.
\]
Thus \(E_+\) is totally isotropic.
Projection onto the one-dimensional negative summand of an orthogonal positive/negative decomposition is injective on a totally isotropic subspace, so \(\dim_{\mathbb C}E_+\le1\).
This dimension counts algebraic multiplicity, not only distinct eigenvalues.
The same argument for \(A^{-1}\) bounds the contracting generalized eigenspace by one.
Moreover \(A^{-1}=H^{-1}A^*H\), so eigenvalues, with multiplicities, are paired by \(\lambda\mapsto1/\overline\lambda\).

Consequently, if an exterior eigenvalue \(\alpha\) exists, it is simple, its unique interior partner is \(1/\overline\alpha\), and all remaining eigenvalues have modulus one.
The complete measures, with every factor and multiplicity retained, are
\[
M(g_A)=|\alpha|,\qquad
M(P_A)=|\alpha|^2,\qquad
m(P_A)=2\log|\alpha|.
\tag{G2}
\]
If there is no exterior eigenvalue, both measures are one.
When \(\alpha\) is real, the exterior root occurs twice in \(P_A\); distinct nonreal conjugate exterior roots require a nonreal \(\alpha\).
No division by dimension is involved.
The realification preserves a real form of signature \((2d-2,2)\), which explains the scope difference from C885 v8.

A scalar Gaussian rotation does not improve this cost.
For a real integral isometry \(A_0\) with characteristic polynomial \(p\), the matrix \(iA_0\) has characteristic polynomial \(i^d p(z/i)\), and the norm polynomial has complete measure \(M(p)^2\).
It rotates an existing core without decreasing its measure.
Conversely, the presence of only one nonreal conjugate exterior pair in an integer polynomial does not by itself provide a Gaussian factorization or an integral Hermitian realization of signature \((d-1,1)\).

<a id="gaussian-single-kick-determinant"></a>
## An integral single-kick family and its full determinant

Fix \(m\ge1\) and standard positive Hermitian Gram matrix \(I_m\).
For \(v\in\mathbb Z[i]^m\), \(V=v^*v\in2\mathbb Z\), and \(s\in\mathbb Z\), define
\[
C_m=\begin{pmatrix}0&0&-1\\0&I_m&0\\-1&0&0\end{pmatrix},\qquad
N(v,s)=\begin{pmatrix}
1&0&0\\v&I_m&0\\V/2+is&v^*&1
\end{pmatrix},\qquad
J=\begin{pmatrix}0&0&-1\\0&-I_m&0\\-1&0&0\end{pmatrix}.
\tag{G3}
\]
Block multiplication gives \(N(v,s)^*C_mN(v,s)=C_m\) and \(J^*C_mJ=C_m\).
The even-norm condition is needed for the displayed Gaussian integrality of \(V/2+is\).
Let \(R\) be unitary for \(I_m\), and put \(\widehat R=\operatorname{diag}(1,R,1)\) and \(A=\widehat RN(v,s)J\).
For an integral example require additionally \(R\in M_m(\mathbb Z[i])\).
The determinant identities and estimates below only require unitarity of \(R\); finite order is not used for them.
The form \(C_m\) has signature \((m+1,1)\), so (G2) applies to integral examples.

With \(q=V/2+is\), the actual matrix is
\[
A=\begin{pmatrix}
0&0&-1\\0&-R&-Rv\\-1&-v^*&-q
\end{pmatrix}.
\]
For \(D(z)=\det(zI+R)\), eliminating the middle block of \(zI-A\) gives
\[
\begin{aligned}
g_A(z)
&=D(z)\det\begin{pmatrix}
z&1\\1&z+q-v^*(zI+R)^{-1}Rv
\end{pmatrix}\\
&=D(z)\left[z^2-1+isz+
\frac z2 v^*(zI-R)(zI+R)^{-1}v\right].
\end{aligned}
\tag{G4}
\]
The equality first holds off the spectrum of \(-R\), and clearing denominators gives the same polynomial identically.
It is the full characteristic polynomial; no factor of \(D\) has been removed or silently counted as neutral.

<a id="gaussian-single-kick-low-measure"></a>
## Low complete measure bounds the single-kick parameters

Assume \(A\) is an integral example from (G3) and \(1<M(P_A)\le2\).
By (G2), its exterior root is \(\alpha=re^{i\theta}\) with \(1<r\le\sqrt2\).
Since the eigenvalues of \(R\) have modulus one, set \(x=(\alpha I+R)^{-1}v\) and divide (G4) by \(\alpha D(\alpha)\) to obtain
\[
\alpha-\alpha^{-1}+is+
\frac12v^*(\alpha I-R)x=0.
\tag{G5}
\]
Using \(v=(\alpha I+R)x\) and \(R^*R=I\),
\[
v^*(\alpha I-R)x
=(r^2-1)\|x\|^2+x^*(\alpha R^*-\overline\alpha R)x.
\]
The last scalar is purely imaginary.
Taking real parts in (G5) and using \(r>1\) therefore gives
\[
\|x\|^2=-\frac{2\cos\theta}{r}\le\frac2r,
\qquad
V=\|v\|^2\le(r+1)^2\|x\|^2
\le\frac{2(r+1)^2}{r}.
\tag{G6}
\]
In particular the exterior phase satisfies \(\cos\theta\le0\); no nonreal phase is assumed in deriving the bounds.
Taking imaginary parts and applying Cauchy gives
\[
\begin{aligned}
|s|
&\le r+r^{-1}+\frac12\|v\|(r+1)\|x\|\\
&\le r+r^{-1}+\frac{(r+1)^2}{r}
=2(r+r^{-1})+2.
\end{aligned}
\tag{G7}
\]
On \(1<r\le\sqrt2\), the right side of (G6) is at most \(4+3\sqrt2<10\), while the last expression in (G7) is at most \(2+3\sqrt2<7\).
The original arithmetic conditions thus imply
\[
V\le8,\qquad |s|\le6.
\tag{G8}
\]
The argument permits \(v=0\) and does not divide by \(V\).
It does not divide by \(r^2-1\) in the neutral case; that case was excluded by the initial positive-measure hypothesis.
These are necessary restrictions for this one-kick representation, not bounds for arbitrary displayed parameters in conjugate or longer words.

<a id="gaussian-cycle-support"></a>
## Standard cycles return the low-measure branch to bounded support

Now let \(R=\varepsilon R_m\), where \(\varepsilon\in\{1,-1\}\) and \(R_m\) is the coordinate permutation matrix of an \(m\)-cycle.
Then
\[
D(z)=z^m-(-\varepsilon)^m,\qquad
c_k=v^*R^kv,
\]
and the finite geometric identity for \((zI+R)^{-1}\) turns (G4) into
\[
g_A(z)=
\bigl(z^m-(-\varepsilon)^m\bigr)
\bigl(z^2+(V/2+is)z-1\bigr)
-z\sum_{k=1}^m(-1)^{k-1}c_kz^{m-k}.
\tag{G9}
\]
This identity again retains the full polynomial, including every cyclotomic factor and multiplicity.

For standard Gaussian coordinates, a nonzero coordinate of \(v\) contributes at least one to \(V\).
Thus (G8) bounds its coordinate support by eight.
For every ordered pair of supported coordinates there is exactly one displacement \(k\in\{1,\ldots,m\}\) at which it contributes to \(c_k\).
The extra sign \(\varepsilon^k\) does not change that support statement.
Consequently at most \(8^2=64\) of the \(c_k\) are nonzero, regardless of \(m\) or the positions of the supported coordinates.
The binomial times trinomial in (G9) has at most six terms, so \(g_A\) has at most 70 nonzero Gaussian coefficients and \(P_A=g_A\bar g_A\) at most \(70^2=4900\) nonzero integer coefficients.
Coincident exponents and cancellations can only reduce those counts.

The accepted [DS17 fixed-support statement](../audits/literature/DS17/Yin_U001.md#ds17-u001) therefore supplies an \(\eta_{4900}>0\) such that every positive measure in this branch has \(m(P_A)\ge\eta_{4900}\).
The other branch has \(m(P_A)>\log2\), so the proposed deduction gives the uniform lower bound \(\min\{\eta_{4900},\log2\}\) for positive complete measures in this exact standard-cycle family.
No numerical value or effective dependence of \(\eta_{4900}\) is asserted.
The external DS17 inspection limits remain those of its responsible source unit; this is a new author application, not a new independent review of DS17 or this deduction.

The coordinate-support step uses the standard positive Gram matrix \(I_m\) and the cycle action.
A bounded norm on an arbitrary positive Hermitian lattice does not supply the same bound on support in a chosen integral basis.
Neither this step nor (G9) is asserted for an arbitrary unitary positive factor or an arbitrary number of alternating cusp operations.
Thus this useful obstruction does not by itself classify all Gaussian Hermitian integral isometries.

<a id="gaussian-hermitian-unresolved-supply"></a>
## Exact one-coordinate discriminator and the remaining construction gap

For \(R=-R_m\), \(v=(1+i)e_1\) and \(s=-b\), (G4) gives exactly
\[
g_m(z)=(z^m-1)\bigl(z^2+(1-ib)z-1\bigr)+2z,
\qquad P_m=g_m\bar g_m.
\tag{G10}
\]
The actual fixed inputs, matrix convention and finite computations belong to [J160](../computations/programs/Yin_J_G0160/readme.md#polynomial-input) and its [program](../computations/programs/Yin_J_G0160/one_kick.py).
The precise all-parameter one-coordinate exclusion is fixed separately in [C887](../claims/Yin_C_G0887_v1.md#statement), with its own actual assessment and source/review scope.
That proof and its exact finite certificate are not duplicated or independently reviewed in this comparison.
No general Hermitian-word conclusion is inferred from the one-coordinate computation.

The inspected source gives an exact arithmetic matrix entrance, and (G2) ensures that a successful loxodromic construction would pay only the complete cost \(2\log|\alpha|\).
The natural standard-cycle single-kick attempt nevertheless has the uniform support obstruction just derived.
This leaves no developed decreasing-radius mechanism in the present bounded comparison.
A next construction would need a specified integral word, Hermitian lattice or non-scalar phase relation that changes the nonneutral core and explains a decrease in its unique exterior radius.
Increasing word length, introducing rational denominators, changing a basis, or assuming the existence of short loxodromics does not provide that missing input.
A new certified finite \(1<M(P)<6/5\) outside the excluded family would still be useful bounded discovery; the original zero-gap direction additionally requires a sequence with \(|\alpha|\downarrow1\).
Neither objective can be obtained by dividing (G2) by dimension or by cyclotomic padding of an unchanged core.
