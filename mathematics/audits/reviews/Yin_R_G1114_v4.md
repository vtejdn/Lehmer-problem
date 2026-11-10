---
author: Yin
---

# Independent review of short transvection words and the constant-Lehmer conjugacy control

## Review arrangement and exact inputs

The review act is dated 2026-11-10T01:22, with Yin as the human record author.
A separately organized reviewer inspected the complete fixed [L462 v14](../../ledger/Yin_L_G0462_v14.md#scope) without developing its argument or receiving author derivation dialogue.
The inspected text explicitly identifies the right factor in the composition calculation and numbers the control's basis by its cyclic action.
Those final sentences were read directly.
No substantive proof repair was contributed.

The reviewer's prior independent findings on [C885 v1](Yin_R_G1114_v2.md#cyclic-two-transvection-gap-review) and [C885 v2](Yin_R_G1114_v3.md#positive-lattice-two-transvection-gap-review) are reused only at their unchanged determinant, lattice and uniform-gap scopes.
The new word identities, their admissibility, the complete control polynomial and the parameterized conjugacy were checked by exact algebra.
The [McM02 accepted source record](../literature/McM02/readme.md#canonical-coxeter-gap-input) was read for the exact known Lehmer polynomial and its established identification.
The [J156 canonical-core expression](../../computations/programs/Yin_J_G0156/primitive_core_sampling.md#exact-observed-minima) was read for its exact displayed coefficients and the substitution \(z\mapsto-z\).
No sampling results, runtime observations or numerical root certificates are necessary premises of this argument.
No original source proof was newly audited, and no sampler, root computation or word enumeration was run.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole argument finding](#short-word-conjugacy-control-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole argument finding](#short-word-conjugacy-control-review) | [L462 v14 scope](../../ledger/Yin_L_G0462_v14.md#scope) | Exact input family, direct-application role and explicit absence of a new asymptotic construction or experiment. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [Short-word reduction](../../ledger/Yin_L_G0462_v14.md#short-word-reduction) | Addition, inverse and covariance identities, even-norm preservation, cyclic conjugacy and transfer of the complete gap to all words of at most three factors in the stated two-cusp setting. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [Lehmer control](../../ledger/Yin_L_G0462_v14.md#lehmer-control) | Exact cyclic correlations, full characteristic polynomial, degree-eleven factorization and identification with the retained known core. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [Unbounded parameters](../../ledger/Yin_L_G0462_v14.md#unbounded-parameters) | Every positive integer N, admissible vectors, exact three norm formulas, integral conjugacy and constant complete measure. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [Longer-word boundary](../../ledger/Yin_L_G0462_v14.md#next-interface) | The precise failure of displayed parameter energy as a growth criterion and the remaining four-factor, representation and original-Task limitations. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [C885 v2 statement](../../claims/Yin_C_G0885_v2.md#statement) | The exact positive-lattice, fixed-hyperbolic-plane family, neutral zero-vector case and absolute complete-logarithmic gap transferred by conjugacy. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [C885 v2 argument](../../claims/Yin_C_G0885_v2.md#argument) | Reuse of integral transvections, finite positive isometries and the already independently reviewed gap at the new short-word invocation. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [C885 v1 determinant](../../claims/Yin_C_G0885_v1.md#argument) | Complete cyclic characteristic-polynomial identity and correlation numerator convention used for the explicit control. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [McM02 known polynomial](../literature/McM02/readme.md#canonical-coxeter-gap-input) | Exact degree-ten polynomial and accepted Lehmer identification only; no canonical-Coxeter representation of the new word is inferred. |
| [Whole argument finding](#short-word-conjugacy-control-review) | [J156 supplied core](../../computations/programs/Yin_J_G0156/primitive_core_sampling.md#exact-observed-minima) | Exact displayed canonical-core coefficients and equality of the control core with F(-z), without reuse or new certification of experimental outcomes. |

<a id="short-word-conjugacy-control-review"></a>
## Finding

No mathematical defect or unresolved input-applicability gap was found in the final inspected L462 v14 argument.
All words with at most three permitted transvections at the two fixed isotropic directions, interspersed with the stated positive isometries, inherit the absolute complete-logarithmic gap of C885 v2.
The explicit three-factor family has unbounded displayed parameter norms but exactly the same complete characteristic polynomial \((z-1)L(z)\) for every positive integer parameter.
The result is an exact conjugacy and known-value control, with the limitations stated below.

### Addition, inverses and preservation of admissibility

For positive-lattice vectors, \((e,u)=(e,v)=(e,e)=0\).
Thus \(E_v\) preserves \(s=(e,x)\) and gives
\[
(u,E_vx)=(u,x)+s(u,v).
\]
Substituting this in the next application \(E_u\) leaves positive displacement \(s(u+v)\) and the coefficient of \(e\)
\[
-(u+v,x)-\tfrac12\bigl((u,u)+2(u,v)+(v,v)\bigr)s.
\]
This is exactly the original formula for \(E_{u+v}\), in the specified right-factor-first order.
The same calculation with \(f\) proves \(F_uF_v=F_{u+v}\).
Taking the second vector to be the negative of the first gives both inverse identities and \(E_0=F_0=I\).

The pairing \((u,v)\) is integral, so the norm of \(u+v\) is even whenever both input norms are even.
Negating a vector preserves its norm and integrality.
Therefore combining adjacent factors or removing inverse or zero factors stays within the admissible integral family.
These calculations need no sign condition on the cross pairing and no bound on the lattice determinant or vector coordinates.

### Moving positive isometries and reducing every short word

An integral positive isometry fixes \(e,f\) and acts on the positive lattice by an invertible integer matrix.
Substitution in the transvection formula gives \(E_uR=RE_{R^{-1}u}\) and \(F_uR=RF_{R^{-1}u}\), because it preserves both the pairing and the two isotropic vectors.
The new vectors are integral and have exactly their original norms.
Repeated use of these identities moves every intervening positive isometry to the left without adding transvection factors.
Their product is again an integral positive isometry of the same \(H\), fixing the same hyperbolic plane, so it satisfies the input assumptions of C885 v2.
No commutativity between different positive isometries is required.

For \(W=RE_vF_wE_u\), direct multiplication by the indicated inverse gives
\[
E_uWE_{-u}=E_uRE_vF_w
=RE_{R^{-1}u}E_vF_w
=RE_{R^{-1}u+v}F_w.
\]
This checks every order and sign in equation (1).
The conjugating matrix and its inverse are integral lattice isometries, and the new first vector has even norm by the preceding addition rule.
Conjugacy preserves the entire characteristic polynomial, since \(zI-SWS^{-1}=S(zI-W)S^{-1}\).
It preserves all roots and multiplicities rather than only an exterior-root statistic.
Exchanging the two isotropic directions gives the corresponding reduction of an alternating \(FEF\) word.

For a mixed two-factor word in the opposite order, the integral map that swaps \(e,f\) and fixes the positive summand preserves the lattice form, commutes with the left positive isometry, and exchanges \(E\) with \(F\).
It therefore conjugates that word to the order used in C885 v2.
All nonalternating words of length at most three have adjacent equal-direction factors that combine, so these cases cover every allowed word.
Words with one transvection are the theorem's zero-vector cases after this ordering; a word with no transvections is just a finite-order positive isometry extended by the identity and has measure one.

Each resulting two-factor input lies in exactly the accepted C885 v2 family, and the original word has exactly its characteristic polynomial.
The same absolute gap constant consequently works for all words in this short-word class, even if the number and sizes of the intervening positive isometries vary.
This conclusion is a transfer of that established gap, not a new parameter-dependent estimate.
After these reductions, an alternating four-factor word is the first length not decided by the supplied argument; no claim of irreducibility under every group relation is needed.

### The full characteristic polynomial of the known-value control

The control fixes \(H=I_9\) and the indexing \(Rb_j=b_{j+1}\) modulo nine.
Thus \(a=b_0+b_1\) has norm two and is admissible in both isotropic directions.
For the same cyclic indexing in every length \(g\ge3\), its support overlaps its rotate in one coordinate at lags \(1\) and \(g-1\), in two coordinates at lag \(g\), and in none at the other lags between one and \(g\).
The two unit-overlap lags are distinct also when \(g=3\).
In the retained correlation convention this gives exactly
\[
U_{a,a}=z^{g-1}+z+2,
\qquad V=\frac{U_{a,a}}{z^g-1}.
\]
Both half-norms are one, the cross pairing is two, and every one of the four correlation resolvents is this same \(V\).

Substitution in the already reviewed full determinant identity gives the first line of equation (2).
Expanding its determinant, the quadratic terms in \(V\) cancel, the constant term is \(z^2-z-1\), and the linear coefficient is \(z^2-1\).
Consequently
\[
P_B=(z^g-1)(z^2-z-1)+(z^2-1)(z^{g-1}+z+2)
=z^{g+2}-z^g-z^{g-1}+z^3+z^2-1.
\]
The calculation is a polynomial identity obtained from the full characteristic determinant, so no unexamined factor or normalization is suppressed.
Coincident powers at small \(g\) simply combine; for example the displayed expression becomes \(z^5-1\) when \(g=3\), consistently with the same formula.

At \(g=9\), multiplying the displayed degree-ten \(L\) by \(z-1\) gives exactly \(z^{11}-z^9-z^8+z^3+z^2-1\).
All coefficients, including the monic leading term and constant term minus one, agree with the complete characteristic polynomial above.
The retained McM02 equation specifies exactly this \(L\) as the known Lehmer polynomial.
The retained J156 expression is
\[
F(z)=z^{10}-z^9+z^7-z^6+z^5-z^4+z^3-z+1,
\]
and substituting \(-z\) gives exactly \(L(z)\) term by term.
This verifies the J interface without reading a numerical certificate as a new proof or claiming a new experimental observation.

The factor \(z-1\) has measure one, and changing the sign of the variable preserves every root modulus and the absolute leading coefficient.
Thus the whole output has precisely the known value \(M(L)=M(F)\).
Its positivity is also consistent with the elementary check \(L(1)=-1\) and eventual positivity for large real \(z\), which gives a real root greater than one.
The established name and source identification are reused at their accepted scope, without importing McM02's canonical-Coxeter theorem as a classification of this matrix word or recomputing the known number.

### The arbitrary-parameter family and its invariant measure

For every positive integer \(N\), \(Na\) and \(-Na\) are integer vectors of even norm \(2N^2\).
The composition and covariance identities give exactly
\[
E_{Na}BE_{-Na}
=RE_{NR^{-1}a+a}F_aE_{-Na}.
\]
With the fixed nine-cycle, \(R^{-1}a=b_8+b_0\), so \((a,R^{-1}a)=1\).
Expanding the norm of the new first vector gives
\[
\|NR^{-1}a+a\|^2=2N^2+2N+2.
\]
Together with the other two norms, the displayed list is therefore correct, integral and even for every permitted \(N\).
Their sum is \(4N^2+2N+4\), which tends to infinity.

Nevertheless the family was defined by conjugacy with the invertible integral matrix \(E_{Na}\), so its complete characteristic polynomial is always \((z-1)L\).
The polynomial, degree, factorization and complete Mahler measure are all unchanged.
In equation (1), the final vector for this family is \(u=-Na\), while its first vector is \(v=NR^{-1}a+a\).
The reduced first vector is
\[
R^{-1}u+v=-NR^{-1}a+NR^{-1}a+a=a,
\]
and its second vector is still \(a\).
This explicitly checks the cancellation rather than inferring it from the size of the parameters.

The family proves that unbounded displayed norm energy does not force complete Mahler measure to grow for three-factor words.
It does not contradict the large-norm implication in C885 v2, because the two vectors after reduction are the fixed norm-two vectors \(a,a\), rather than the unreduced three-vector parameters.
It also supplies an exact example of arbitrarily many parameter choices representing one polynomial and one positive measure, without an assertion about the actual behavior or probabilities of any optimizer.

### Scope and remaining interfaces

The argument uses two fixed isotropic directions in the specified hyperbolic plane and intervening isometries of the positive summand that fix both directions.
It supplies no reduction for transvections based at arbitrary other isotropic vectors and no representation theorem for all integral indefinite isometries or Salem polynomials.
The earlier Coxeter and fixed-support boundaries retain their actual scope, and failure to recognize a canonical representation supplies no evidence of escape from a known theorem.

The three-factor gap rules out a shrinking-positive-measure construction within the stated short-word class even as the positive lattice changes.
The constant-Lehmer control is neither a new small measure nor a family tending to one.
No four-factor gap or longer-word spectral bound follows from the checks above.
The unrestricted [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.
This review records the complete direct argument and its input interfaces, without adopting a new Claim assessment, changing research priorities or extending the scope of earlier source and computational reviews.
