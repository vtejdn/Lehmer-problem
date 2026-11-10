---
author: Yin
---

# Independent review of the degree-18 diagram quotient and two-transvection model

## Review arrangement and fixed inputs

This review act is dated 2026-11-10T02:18, with Yin as the human record author.
A separately organized reviewer inspected the complete fixed diagram-model argument, author program, designated polynomial input and actual generated certificate without participating in development or receiving the main thread's derivation dialogue.
No substantive repair was supplied.
This is new evidence for the integral representation question, distinct from the earlier natural trace-lattice calculation and obstruction.

The reviewer directly read the canonical-form/action text and the degree-eighteen example in the [published McM02 original](../../literature/pdf/McM02.pdf) at printed pages 161--162 and 181--182, respectively.
The reviewer visually inspected Figure 7 and the complete example on pages 181--182 and read the new source unit at its recorded scope.
The earlier independently reviewed C885 v2 theorem is reused only for the stated family and its already established gap.
The shared author matrix helpers retain their prior reviewed scope, with their new diagram-model uses inspected here.
No source classification theorem, matrix search or numerical root computation is part of this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Fixed question and source interface](../../computations/programs/Yin_J_G0158/coxeter_model.md#question) | Exact original polynomial, diagram, reflection convention, involution and chosen bicolored word. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Integral quotient and splitting](../../computations/programs/Yin_J_G0158/coxeter_model.md#integral-quotient) | Primitive radical, free integral quotient, full induced form and action, unimodular basis and complete E8 plus E8 plus U splitting. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Two-transvection form](../../computations/programs/Yin_J_G0158/coxeter_model.md#two-transvection-model) | Word rearrangement, exact root and transvection identities, positive-isometry order and all characteristic coefficients. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Interpretation and limits](../../computations/programs/Yin_J_G0158/coxeter_model.md#results-and-limits) | Full application to C885 v2, unchanged-polynomial control, compatibility with the different-lattice obstruction and stated nonconclusions. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Whole author program](../../computations/programs/Yin_J_G0158/coxeter_model.py) | Complete fixed integer/rational algorithm, newly defined operators, checks, output construction and actual helper interfaces. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Original input](../../computations/programs/Yin_J_G0144/trace56_cell.json) | Exactly the nineteen ascending H_ascending coefficients; other J144 fields are not review targets. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Actual diagram certificate](../../computations/outputs/Yin_J_G0158/coxeter_model.json) | All forty-two fields, every matrix and vector entry, complete polynomials, determinant, inertias, order and Boolean conclusions. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Shared matrix helpers](../../computations/programs/Yin_J_G0158/trace_lattice.py) | Imported determinant, identity, inertia, integral inverse, matrix/vector product, pairing and transpose at their actual diagram-model uses. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Earlier arithmetic review](Yin_R_G1114_v5.md#trace-lattice-splitting-review) | Reuse of the unchanged exact helper inspection; it supplies no prior review of the new diagram or quotient. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Source polynomial](../literature/McM02/Yin_U002.md#degree18-polynomial) | Coefficient agreement with the source's existing example and its symmetry-times-bicolored recipe, without a new classification-proof audit. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Source diagram transcription](../literature/McM02/Yin_U002.md#figure-seven-recipe) | All nineteen vertices, eighteen edges, source normalization, involution, selected Y subdiagram, colors and column-action convention. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Source integral-model limits](../literature/McM02/Yin_U002.md#integral-model-verification) | The source-reading boundary and the separate quotient/splitting/generator obligations resolved by this finite certificate; no general group-generation result is imported. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [C885 v2 family](../../claims/Yin_C_G0885_v2.md#statement) | Substitution of positive rank sixteen, the verified integral isometry R and the two norm-two vectors v=w=theta; complete-polynomial and ineffective-gap qualifications. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Existing C885 v2 review](Yin_R_G1114_v3.md#positive-lattice-two-transvection-gap-review) | Reuse of the unchanged independently reviewed family theorem, without a new audit of its external foundational inputs. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Earlier discriminant obstruction](Yin_R_G1114_v5.md#discriminant-action-review) | Its restriction to the natural trace lattice and compatibility with this different integral form. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Independent diagram checker](../../computations/programs/Yin_J_G0158/checks/independent_coxeter_model_review.py) | Separate vector-action reconstruction, rational determinants, full quotient/basis identities and complete-polynomial verification, without author-code imports or execution. |
| [Complete diagram-model finding](#coxeter-two-transvection-model-review) | [Independent verification result](../../computations/outputs/Yin_J_G0158/independent_coxeter_model_review.json) | Actual successful all-field verification, positive minors, determinant values at every prescribed integer, exact order and full matrix identities. |

<a id="coxeter-two-transvection-model-review"></a>
## Finding: complete finite model and family application

No mathematical, source-interface or implementation defect was found in the inspected argument and its actual certificate.
The finite construction realizes the exact original degree-eighteen polynomial on an even unimodular integral lattice with an explicit splitting \(E_8\oplus E_8\oplus U\).
In that basis its entire isometry is \(R T_{e,\theta}T_{f,\theta}\), with \(R\) an integral positive isometry of exact order sixty and \((\theta,\theta)=2\).
The precise derivation remains at the author's bound argument above; the following records the decisive review evidence and its limits.

### Source and whole-program conventions

The original canonical form is \(B(e_i,e_j)=-2\cos(\pi/m(i,j))\), and the source's action is \(x\mapsto x-B(e_i,x)e_i\).
Thus diagonal two and simple-edge entry minus one require exactly the author's column-action matrices, without a half-form rescaling.
Visual comparison confirms the chain of seventeen vertices and the leaves at its third and fifteenth vertices.
The chosen left subdiagram has arm edge lengths \(1,2,6\), the source's \(Y_{2,3,7}\), with the stated mutually orthogonal color classes.
The published degree-eighteen polynomial agrees in every coefficient with the original J144 input.
The source specifies the product of a diagram symmetry and a bicolored subdiagram element; the labels and explicit color order are the local transcription, whose complete polynomial is verified here rather than presumed from that description.

The reviewer inspected the whole author program, including its matrix multiplication order, column construction, reflection formula, projection and inverse-basis interfaces, modular-free integer power routine, transvection signs and Newton recurrence.
The latter uses every trace through degree \(n\), with the correct coefficient reversal and exact divisibility checks.
The imported inertia routine is also used on the singular nineteen-dimensional form; the separate congruences below verify that new interface without relying on its output.
The finite order checks \(R^{60}=I\) and \(R^{30},R^{20},R^{12}\ne I\) suffice for exact order sixty because every proper divisor of sixty divides one of those three exponents.
The author's asserted checks apply to the documented ordinary Python invocation, and the separately executed checker uses explicit exceptions rather than removable assertions.

### Primitive quotient and full integral splitting

Write \(r=e_L-e_R\), \(Q\) for the displayed quotient projection, \(I_q\) for its inclusion, and \(G_q\) for the quotient Gram matrix.
The exact check verifies \(Br=0\), \(gr=-r\) and \(r_{h_8}=1\).
It also verifies
\[
QI_q=I_{18},\qquad Qr=0,\qquad
B=Q^{\mathsf T}G_qQ,\qquad Qg=A_qQ.
\]
The nineteen columns consisting of \(I_q\) followed by \(r\) form a unimodular basis and transform \(B\) to \(G_q\oplus0\).
Together with \(\det G_q=-1\), this proves that the rational radical is exactly one-dimensional, the full integer radical is \(\mathbb Zr\), and the stated integral quotient is free.
The quotient isometry is integral and satisfies \(A_q^{\mathsf T}G_qA_q=G_q\).
No torsion class or unverified overlattice is suppressed.

The split basis \(T\) is reconstructed from the sixteen stated roots, \(e=Qe_L=Qe_R\) and \(f=-Qh_9-e\).
Both inverse identities are checked entrywise for the actual stored integer inverse, and rational elimination gives \(\det T=1\).
The whole congruence is
\[
T^{\mathsf T}G_qT=S=K\oplus K\oplus U,
\qquad A=T^{-1}A_qT.
\]
Here \(K\) is exactly the displayed E8 Cartan Gram matrix, with leading principal minors \(2,3,4,5,6,7,8,1\).
Sylvester's criterion proves its positive definiteness; the complete off-diagonal blocks vanish and the final block is precisely \(U\).
It follows that the quotient is even unimodular with inertia \((17,1,0)\), while the original form has inertia \((17,1,1)\).
These arguments independently certify both reported inertias instead of numerically diagonalizing either form.

### Exact word, all roots and the family interface

The images of the remaining roots are exactly
\[
h_8=e-\theta,\qquad h_9=-(e+f).
\]
The diagram involution fixes \(e,f\) in the quotient and exchanges the two positive blocks.
The positive-root word \(P\) fixes \(U\), and the reconstructed \(R=\sigma P\) has all claimed positive-isometry and order properties.
Within the source word, \(h_9\) is orthogonal to every factor moved past it; the leaf reflection also commutes with the \(h_8\) factor.
This justifies the rearrangement to \(RJs_{e-\theta}\) without interchanging any adjacent noncommuting reflections.

The norm-two identity \(Js_{e-\theta}=T_{e,\theta}T_{f,\theta}\) holds on the complete lattice.
For example both sides send \(e\) to \(-f\), send \(f\) to \(f+\theta-e\), and send a positive vector \(x\) to \(x-(\theta,x)(\theta+f)\).
This checks the signs, composition order and the half-norm coefficient directly.
The independent program rebuilds both transvections from that pairing formula and verifies the entire equality
\[
A=RJs_{e-\theta}=RT_{e,\theta}T_{f,\theta},
\qquad A^{\mathsf T}SA=S,\qquad \det A=1.
\]

For an additional independent check of all characteristic coefficients, rational Gaussian elimination evaluates \(\det(tI-M)\) at \(t=0,\ldots,n\) for each of \(M=A,A_q,g\), of dimensions eighteen, eighteen and nineteen.
It agrees at all these distinct integers with \(H(t),H(t),(t+1)H(t)\), respectively.
Since both polynomials in each comparison have degree at most \(n\), these \(n+1\) exact equalities prove the full polynomial identities.
This is not sampling of an unbounded hypothesis or a numerical root check.
The radical eigenvalue is exactly minus one, so its removed factor \(x+1\) has Mahler measure one.
The quotient and split isometry retain all eighteen roots and multiplicities of the original \(H\).

For C885 v2, the positive matrix is \(H_+=K\oplus K\), the positive rank is sixteen, and both parameter vectors equal the verified integral norm-two vector \(\theta\).
Every integrality, definiteness, parity and positive-isometry hypothesis therefore holds.
This places the known example in the theorem's exact two-transvection family.
The product of parameter norms is two, so the theorem's separate \(s\ge650\) implication is not being used as a finite-value exclusion.
The uniform positive gap remains the previously reviewed theorem; no effective threshold at \(6/5\) is derived here.

### Independent execution and limits

The separate checker ran successfully with CPython 3.14.7 and only standard-library exact integers and fractions.
It imports and executes no author program.
It checks all forty-two actual certificate fields, including every matrix and vector entry, with integer and Boolean types distinguished.
The inverse is certified by both complete inverse identities; the other matrices are reconstructed from vector actions or verified full changes of basis.
The separate output retains the exact principal minors and all determinant evaluation values.

With the interpreter selected as python, run from the repository root:

~~~text
python -B mathematics/computations/programs/Yin_J_G0158/checks/independent_coxeter_model_review.py
~~~

The required inputs are the fixed J144 polynomial document and the actual coxeter_model.json generated by the author's documented command.
The checker writes only its distinct independent_coxeter_model_review.json result.
Earlier generated trace and discriminant certificates are not runtime inputs.

The natural trace lattice of R1114 v5 has a different determinant, while the present quotient has determinant minus one.
Thus the earlier same-lattice discriminant obstruction and this explicit representation are compatible.
No isomorphism or conjugacy between those two integral lattices is asserted.

The original source's reflection-group classification, index-two theorem and nonmembership classification are not premises of the finite identities or the C885 application and were not independently proved here.
The source reading supplies attribution and the precise diagram/action interface, not a general generation theorem.
This certificate supplies one existing polynomial realization, no new Salem value, no unrestricted representation theorem and no unrestricted Mahler gap.
The [original G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.
