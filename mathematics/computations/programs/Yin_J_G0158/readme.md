---
author: Yin
---

# Natural trace-lattice obstruction and unimodular model for the degree-18 known Salem core

<a id="question"></a>
## Question and scope

This is a single-object representation test for [S4](../../../strategies/Yin_S_G0004.md#route) within the [unchanged Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract).
The exact input is the degree-18 second known core \(p\), taken from the reviewed [J144 input](../Yin_J_G0144/trace56_cell.json), field H_ascending.
It asks whether the natural trace Gram lattice of its integer companion matrix admits an integral unimodular hyperbolic plane \(U\), without taking a matrix power, adjoining a hyperbolic plane or changing the polynomial.
It then tests whether that same lattice isometry can be a word in positive-summand integral isometries and the two fixed-cusp integral transvection groups, with no word-length bound.
This is a representation test for one known value, not a new small value or a sampling campaign.
The [separate source-diagram continuation](coxeter_model.md#question) constructs a different integral form and an explicit two-transvection realization of this same polynomial.

The Gram matrix is \(G_{ij}=\operatorname{Tr}(\alpha^{i-j})\), for \(0\le i,j<18\).
Newton identities and reciprocity construct it entirely over the integers.
The program checks the actual companion invariance and exact inertia.
The [ERT19 source interface](../../../audits/literature/ERT19/Yin_U001.md#companion-trace-gram) identifies this integral bilinear Gram as twice the source's quadratic coefficient matrix; it supplies no integral hyperbolic-plane splitting theorem.
For an initial bounded witness search, inspect vectors in \(\{0,\pm1\}^{18}\) of support at most four, with first nonzero coordinate positive, stopping at the first isotropic vector \(e\) with \(\gcd(Ge)=1\).
Failure on that finite set supplies no general lattice obstruction.
An actual witness permits exact Bezout construction of \(f\), an integral basis and the full split Gram matrix.

## Files

| File | Role |
| --- | --- |
| [trace_lattice.py](trace_lattice.py) | Exact trace Gram, bounded isotropic search and unimodular splitting certificate. |
| [Original degree-18 input](../Yin_J_G0144/trace56_cell.json) | The fixed polynomial and previously checked source core. |
| [Result](../../outputs/Yin_J_G0158/trace_lattice.json) | Generated complete matrices and exact checks, when available. |
| [Discriminant argument](discriminant_action.md#necessary-condition) and [program](discriminant_action.py) | Necessary discriminant-action condition for all permitted words and the exact test on this fixed lattice. |
| [Discriminant result](../../outputs/Yin_J_G0158/discriminant_action.json) | Complete adjugate, modular matrix power, defect matrix and nonzero witness. |
| [Independent trace checker](checks/independent_trace_lattice_review.py) and [result](../../outputs/Yin_J_G0158/independent_trace_lattice_review.json) | Separate quotient-algebra reconstruction, all matrices, determinants and positive principal minors. |
| [Independent discriminant checker](checks/independent_discriminant_review.py) and [result](../../outputs/Yin_J_G0158/independent_discriminant_review.json) | Separate polynomial-quotient powering, full modular certificate and integral change of basis. |
| [Unimodular model](coxeter_model.md) and [program](coxeter_model.py) | Exact source-diagram quotient, E8 plus E8 plus U splitting and complete two-transvection identity on a different integral lattice. |
| [Model certificate](../../outputs/Yin_J_G0158/coxeter_model.json) | Complete matrices, primitive radical, quotient maps, integral bases, order and all characteristic coefficients. |
| [Independent model checker](checks/independent_coxeter_model_review.py) and [result](../../outputs/Yin_J_G0158/independent_coxeter_model_review.json) | Independent reconstruction of every certificate field and full characteristic polynomials by exact determinant evaluations. |

## Reproduction

From the repository root, generate the two natural-lattice author certificates and then verify them in this order:

~~~text
python -B mathematics/computations/programs/Yin_J_G0158/trace_lattice.py
python -B mathematics/computations/programs/Yin_J_G0158/discriminant_action.py
python -B mathematics/computations/programs/Yin_J_G0158/checks/independent_trace_lattice_review.py
python -B mathematics/computations/programs/Yin_J_G0158/checks/independent_discriminant_review.py
~~~

Only the Python standard library is required.
All mathematical calculations use integers or exact rational fractions, with no numerical eigensolver, root approximation or tolerance.
The generated result is replaceable by reproduction and is written only after the complete claimed calculation succeeds.
The finite search has support cap four and a twenty-second search allowance; an expired allowance yields an explicit incomplete search rather than an exclusion.
Exact certificate checks after a found witness are distinct from the finite witness search.
The original J144 polynomial is the fixed input; the discriminant program requires the first generated certificate, and the independent checkers require the corresponding actual author certificates.
The independent programs write their own result files without importing or executing the author programs.

The different-lattice model has its own independent command pair and reads no earlier generated certificate:

~~~text
python -B mathematics/computations/programs/Yin_J_G0158/coxeter_model.py
python -B mathematics/computations/programs/Yin_J_G0158/checks/independent_coxeter_model_review.py
~~~

The first command reads only the fixed J144 polynomial, and the second reads that input and the actual model certificate.
Both use the Python standard library; the author model also reuses the retained author matrix helpers.

## Results and limits

The exact test completed and found a divisor-one isotropic vector after checking 18 support-one vectors and 33 support-two vectors.
No support-three or support-four search was needed.
In the original power basis, its actual two null vectors are
\[
e=1-\alpha^{17},\qquad
f=-24+\alpha-\alpha^2-\alpha^9+24\alpha^{17}.
\]
The complete result verifies \((e,e)=(f,f)=0\) and \((e,f)=1\), and retains every entry of the resulting basis matrix \(T\), its integral inverse and the transformed companion matrix \(A\).
It checks
\[
\det T=-1,\qquad
T^{\mathsf T}GT=H_+\oplus
\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
CT=TA,
\]
where \(H_+\) is integral positive definite of rank sixteen.
Exact symmetric elimination gives inertia \((17,1,0)\) for \(G\) and \((16,0,0)\) for \(H_+\).
The original Gram determinant is \(-2915479459020775961521\).
The program also directly verifies \(C^{\mathsf T}GC=G\) and preservation of the split Gram matrix by \(A\).

Here is the integral construction behind the finite certificate.
An isotropic \(e\) with \(\gcd(Ge)=1\) has an integral Bezout partner \(f_0\) with \((e,f_0)=1\).
The Gram matrix has even diagonal, so \((f_0,f_0)\) is even and \(f=f_0-\tfrac12(f_0,f_0)e\) is an integral null partner.
Integer Bezout column operations extend \(e,f\) to a unimodular basis; projecting its remaining vectors off this pair gives the displayed orthogonal splitting.
The program checks the whole resulting matrices, rather than inferring unimodularity or positive definiteness from the witness search.

The [independent splitting finding](../../../audits/reviews/Yin_R_G1114_v5.md#trace-lattice-splitting-review) checks the complete certificate and original characteristic-polynomial preservation by integer conjugacy.
It supplies an actual positive-lattice-plus-U input for the known second core, with no power or added dimensions.
The independent verification also proves positive definiteness from all sixteen leading principal minors, separately from the author's inertia algorithm.

The subsequent [discriminant obstruction](discriminant_action.md#conclusion-and-limits), covered by the [independent discriminant finding](../../../audits/reviews/Yin_R_G1114_v5.md#discriminant-action-review), excludes a representation by the stated generators at every finite word length on this same natural trace lattice.
It applies to every integral positive-rank-sixteen-plus-U splitting of that lattice, not only the displayed basis.
Both independent result files report verified.
Other invariant lattices or pairings and other realizations remain outside this exclusion.
The natural trace-lattice test supplies no canonical Coxeter representation, new Mahler value or general splitting or generation theorem.

<a id="unimodular-model-result"></a>
The [completed source-diagram model](coxeter_model.md#two-transvection-model), covered by its [complete independent finding](../../../audits/reviews/Yin_R_G1114_v6.md#coxeter-two-transvection-model-review), realizes the same polynomial on \(E_8\oplus E_8\oplus U\).
It gives \(A=RT_{e,\theta}T_{f,\theta}\), with positive-isometry order sixty and \((\theta,\theta)=2\).
The original nineteen-dimensional graph has a primitive one-dimensional radical with eigenvalue minus one; its exact integral quotient preserves the original eighteen-dimensional polynomial and complete measure.
The quotient Gram has determinant minus one, so it is distinct from the fixed natural trace lattice excluded above.
This supplies an explicit representation of the known second small value inside the already controlled C885 v2 family, without a new value, a longer-word escape or an effective exclusion below \(6/5\).
