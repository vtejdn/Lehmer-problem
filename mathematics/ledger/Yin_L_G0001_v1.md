---
author: Yin
---
# Lehmer route assessment: arithmetic entropy, affine relations and determinants

<a id="lehmer-route-assessment"></a>
Date: 2026-10-06.
Acting agent: root for Yin, with three parallel AI assessments.
Record kind: method evaluation and known-result reproduction for [Task G0001](../tasks/Yin_T_G0001_v1.md#contract).
This fixes the evidence behind revisions of [S G0001](../strategies/Yin_S_G0001.md), [S G0002](../strategies/Yin_S_G0002.md) and [S G0003](../strategies/Yin_S_G0003.md).
It claims neither a new Lehmer bound nor a counterexample.
The human ordering remains algebraic entropy first, affine growth second, determinant methods third.
The complete current zero-gap reverse proof is owned by [C G0207](../claims/Yin_C_G0207_v1.md#argument), and the exact affine short-free-pair proof by [C G0208](../claims/Yin_C_G0208_v1.md#argument).
The original body below preserves the dated route/source assessment and the original L1 Section 1 reverse implication inspected by [R384](../audits/reviews/Yin_R_G0384_v1.md#zero-gap-direct-sum-independent-finding); its historical review does not become a review of those later Claim wrappers.

## 1. Finite capture locates the difficulty; it does not weaken it

Use natural-log entropy, the Addition Theorem, continuity under directed unions and the finite-rank/attainment inputs at the scopes retained in [DGB16-U002](../audits/literature/DGB16/Yin_U002.md#dgb16-u002) and [DGB16-U004](../audits/literature/DGB16/Yin_U004.md#dgb16-u004).
A positive uniform gap forces finite capture by the audited stabilization argument; the retained realization argument then gives finite-set attainment.

Conversely, if the gap is zero, choose finite positive entropy flows with entropies e_j in (0,2^(-j)).
Their direct sum has entropy sum(e_j), by finite addition and continuity.
Every finite subset is supported on finitely many summands, so its local entropy is strictly below this sum.
A finitely generated Z[t]-submodule likewise has finite summand support.
Thus universal finite capture and universal finite-set attainment fail.
This argument needs no exact-spectrum theorem.
In particular, proving universal capture is an equivalent route to Lehmer, not an easier consequence of generic compactness.
A nonattaining flow would refute the gap through the valid gap-implies-attainment implication; it would not refute that implication itself.

A useful diagnostic already occurs in a split semisimple category.
Let R=Q[t], S_j=R/(t-j) for j>=2, and consider direct sums of these pairwise nonisomorphic simple modules.
Define
\[
\ell\left(\bigoplus_{j\ge2}S_j^{(\kappa_j)}\right)
 =\sum_{j\ge2}2^{-j}\kappa_j,
\]
with any infinite multiplicity contributing infinity.
In this category exact sequences split; the function is additive and is the supremum of its values on finitely generated submodules.
For M=direct-sum(S_j), ell(M)=1/2, whereas every finitely generated submodule has finite support and strictly smaller length.
The ring R is Noetherian.
This is a countermodel to the proposed inference from Noetherianity plus generic length properties to capture, already in a split category.
It is **not** an algebraic-entropy counterexample, nor is a length function on all R-modules being asserted: actual algebraic entropy assigns h(S_j)=ln(j).
The missing information is the arithmetic constraint on genuine entropy weights.

## 2. Where the uniform arithmetic problem remains

For a primitive irreducible integer polynomial p with positive leading coefficient a, m(p)>=ln(a).
If p is monic with |p(0)|>=2, the product of root moduli gives m(p)>=ln|p(0)|.
Reducible polynomials reduce to their irreducible factors by additivity of m; zero roots contribute nothing.
Thus a family with positive m tending to zero must eventually use monic algebraic units of unbounded degree.
Fixed degree cannot supply such a family: bounded Mahler measure bounds all integer coefficients in fixed degree, leaving finitely many polynomials.

The author's survey Smy08, Section 5.1, printed pp.327--328 / PDF pp.6--7, equation (15), states Smyth's theorem for nonreciprocal algebraic integers: M(alpha)>=theta_0=1.3247..., the positive real root of t^3-t-1.
Its hypotheses and multiplicative normalization were checked directly; the original 1971 proof was not audited.
Accepting this standard theorem at statement level narrows the unresolved core to **irreducible reciprocal noncyclotomic monic unit polynomials, with unbounded degree**.
This is not a reduction to Salem numbers alone: reciprocal polynomials may have more than one pair of roots off the unit circle.

Accordingly the primary route needs a new arithmetic entropy mechanism on cyclic rational flows or integral lattices carrying these units.
Torsion shifts and extension/splitting arguments are useful controls but do not remove the hard core.
General module structure, or a uniqueness theorem whose prime weights are already Mahler measures, does not itself constrain those weights away from zero.

<a id="affine-free-pair-obstruction"></a>
## 3. Universal short free pairs are excluded in the exact affine family

Bre07, Theorem 1.7 on p.4 and Section 7, Theorem 7.2 and proof on pp.14--15, gives unbounded positive-independence diameter in metabelian polycyclic subgroups of GL_2(Qbar).
The overbar matters.
The following direct positive-word check records its applicability to the Task's S_x={z maps to xz-1, z maps to xz+1}; the source's more general signed-exponent argument is not required.

For any integer N>=1, put r=N!.
Let y in (-1,0) be the real root of y^3+y+1=0, and choose x with x^r=y.
Then x is a nonzero algebraic unit, |x|<1 and x is not a root of unity; hence m(x)>0 by Kronecker.
The affine change g(z)=z/2+1/(2(1-x)) conjugates S_x to A(z)=xz, B(z)=xz+1.

Take any two nonempty positive words U,V in A,B of lengths q,p<=N.
Their slopes are x^q,x^p, neither equal to one.
If their fixed points coincide they commute and are not free.
Otherwise a simultaneous affine conjugacy puts them in the form U(z)=x^q z, V(z)=x^p z+1.
Consequently
\[
U^{r/q}(z)=yz,\qquad V^{r/p}(z)=yz+b,\qquad
b=(1-y)/(1-x^p)\ne0.
\]
Composition is read right to left.
For C(z)=yz and D(z)=yz+b, direct multiplication yields
\[
D^2CD(z)=y^4z+b(y^3+y+1)=C^4(z).
\]
Therefore
\[
U^{4r/q}=V^{2r/p}U^{r/q}V^{r/p}.
\]
This is a nontrivial equality of distinct positive words in the proposed generators U,V.
All pairs in the positive ball of radius N fail to generate a free semigroup.
Since N was arbitrary, there is **no universal bounded-word free-pair construction even in this same-slope two-map family with positive Mahler measure**.
This excludes the initial prospective mechanism, not the uniform growth-gap target.
The source explicitly separates these questions.

It also explains a weakness of single-place ping-pong.
Every conjugate of x has logarithmic modulus bounded in absolute value by C/r, where C depends only on the three roots of t^3+t+1.
No fixed power makes a uniformly contracting/expanding conjugate.
A many-conjugate entropy argument could still succeed.
Do not infer small total entropy from these small individual logarithms: M(p(t^r))=M(p), and field-extension multiplicity matters when passing from that polynomial to a chosen irreducible factor.

## 4. Finite-scale evidence and determinant direction checks

For the affine positive-word rate,
\[
\rho_2(S)=\inf_{n\ge1}\frac{\log_2|S^n|}{n}.
\]
Thus an exact finite count is an **upper** bound.
For a refutation, an all-k algebraic family with m(lambda_k)>0 and exact counts |S_(lambda_k)^(N_k)|<=2^(N_k/k) would suffice: BV20 ensures positivity and these counts force rho_2 to zero.
Finitely many numerical examples do not suffice.
For proving a lower bound, finite balls require a uniform continuation mechanism.
Primitive roots of unity of increasing degree satisfy |S_zeta^n|=2^n for each fixed n eventually (a collision would give a nonzero polynomial of degree <n vanishing at zeta), while each rate is zero: their translations lie in a finite-rank lattice with polynomial growth.
Passing to a marked-group limit supplies no lower-bound continuity; the infimum formula gives the opposite semicontinuity direction.

For determinants, retain [Luc22-U001](../audits/literature/Luc22/Yin_U001.md#luc22-u001), [U002](../audits/literature/Luc22/Yin_U002.md#luc22-u002) and [U003](../audits/literature/Luc22/Yin_U003.md#luc22-u003).
The Fourier identity log det(p)=m(p) is a comparison, not a new gap.
Integer finite-dimensional determinants >=2 give normalized values >=2^(1/n), which tend to one.
In fact on a cyclic group C_n with odd n, det(1+t)=2^(1/n), whereas on Z its determinant is one.
These are not scalar Lehmer counterexamples.

A genuine positive bridge remains available: if a fixed group G contains Z, each corresponding group constant satisfies C(G)<=C(Z).
A bound C(G)>1 for any of the four constants therefore implies the classical scalar gap, using Lambda(Z)<=Lambda_1(Z) when needed.
This is often a stronger problem, not an automatic simplification.
In the opposite direction, small determinants over arbitrary groups require a proved return to nonzero integral Laurent polynomials p_k (or square weak Z[Z] matrices), including positivity and an estimate m(p_k)<=C log det_G(A_k) with C independent of k.
Small values in varying finite groups alone provide no such map.

Uniform control of the logarithmic singularity can justify determinant limits but does not itself yield a positive arithmetic gap: nonintegral constant operators e^epsilon have spectra uniformly away from zero and logarithmic determinants tending to zero.
This is a diagnostic for missing integrality, not a counterexample in the Task's coefficient ring.

## 5. Consequences and the next bounded work package

Keep G0001 active priority 1, G0002 proposed priority 2, G0003 proposed priority 3.
Recast universal finite capture as a final equivalent closure criterion.
Remove universal short free pairs from G0002's candidate mechanisms.
Reopen that mechanism only with a justified restricted scope and a separate return to the full Task.

The next primary package is: (i) mark known identities, equivalent unknowns and genuinely new candidate inputs in one dependency map; (ii) formulate one explicit trajectory/lattice entropy-increment inequality, stating every dependence on degree, conjugate distribution and word length; (iii) test it against the split weighted-length diagnostic, reciprocal unit companion flows, high-degree roots of unity, t^d-2 (Mahler measure ln2 despite house tending to one), 2t-1 (leading coefficient), and infinite direct sums of zero-entropy flows.
An entropy-capturing submodule need not be the whole flow or make the whole group finite rank.
The output should be a precise viable inequality or a located obstruction, not another equivalent reformulation alone.

For a time-dilation control, the cyclic shift on G^k with phi at the wrap satisfies psi^k=phi direct-sum ... direct-sum phi, so the logarithmic law and addition give h(psi)=h(phi), not h(phi)/k.
Taking long roots or longer return times must carry the corresponding multiplicities.

Method consultation: Uniform descent and finite closure; current organization, formulation dated 2026-10-02, is used only for its all-parameter closure requirement; no detecting descent or finite global degree bound is currently supplied.
Shared structure across families; current organization informs the common orbit-relation interface of the entropy and growth routes, not an assertion that either known equivalence already solves the problem.
This assessment does not change those methods' reusable scope.

## Inspection and limits

Three parallel AI agents assessed the entropy, affine and determinant mechanisms; root checked their arguments and the retained relevant PDF pages.
Bre07 pp.4,14--15 were inspected, including the positive-word construction above; Smy08 pp.327--328 were inspected for the quoted theorem's statement and applicability.
Neither entire source was audited.
Existing DGB16, BV20 and Luc22 source-review limitations remain in force.
No independent full-theorem review, new Claim acceptance, changed Task contract or autonomous research execution is asserted.
