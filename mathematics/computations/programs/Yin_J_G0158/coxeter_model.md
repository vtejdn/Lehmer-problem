# A source-diagram realization of the same degree-18 polynomial

<a id="question"></a>
## Fixed question and source interface

This continuation of the [J158 representation test](readme.md#question) changes the integral lattice and form while retaining the exact degree-18 polynomial H_ascending in the [original J144 input](../Yin_J_G0144/trace56_cell.json).
It constructs the diagram model specified by McM02 Figure 7 and Corollary 7.11, printed pages 181--182 of the [retained published original](../../../literature/pdf/McM02.pdf).
The [source unit](../../../audits/literature/McM02/Yin_U002.md#figure-seven-recipe) retains the complete diagram transcription and source-inspection limits; the source's group-classification statements are not premises of the finite matrix checks below.
No polynomial power, added nonneutral root, numerical root calculation or parameter search is involved.

Label the horizontal chain in Figure 7 as \(h_1,\ldots,h_{17}\), with a left leaf attached to \(h_3\) and a right leaf attached to \(h_{15}\).
The nineteen-by-nineteen canonical Gram matrix \(B\) has diagonal two, minus one on those eighteen edges and zero elsewhere.
Let \(S_i=I-e_i(e_i^{\mathsf T}B)\) be its column-action reflection, and let \(\sigma\) reverse the chain and exchange the leaves.
The selected left \(Y_{2,3,7}\) has color classes
\[
\{h_1,h_3,h_5,h_7,h_9\},\qquad
\{h_2,h_4,h_6,h_8,\ell\}.
\]
The source isometry is \(g=\sigma c\), where \(c\) is the first color product followed by the second.

<a id="integral-quotient"></a>
## Exact quotient and integral splitting

In coordinates \(h_1,\ldots,h_{17},\ell,r\), put
\[
e_L=2h_1+4h_2+6h_3+5h_4+4h_5+3h_6+2h_7+h_8+3\ell,
\qquad e_R=\sigma e_L.
\]
The program checks \(\operatorname{rad}(B)=\mathbb Q(e_L-e_R)\), inertia \((17,1,1)\), and \(g(e_L-e_R)=-(e_L-e_R)\).
The coefficient of \(h_8\) in this primitive radical vector is one.
Consequently removing \(h_8\), with its image replaced by the negative of the other radical coefficients, gives an explicit integral basis of the free quotient \(\mathbb Z^{19}/\mathbb Z(e_L-e_R)\).
The projection, inclusion, complete quotient matrix and Gram matrix are all retained and checked.

Use the eight left roots \((h_1,\ldots,h_7,\ell)\) and their mirrored right roots as the positive basis.
In the quotient put \(e=e_L=e_R\) and \(f=-h_9-e\).
The program checks the entire unimodular change of basis and the exact splitting
\[
L=E_8\oplus E_8\oplus U,\qquad (e,e)=(f,f)=0,\quad(e,f)=1.
\]
Each displayed positive Gram block has leading principal minors \(2,3,4,5,6,7,8,1\).
The quotient Gram is even, has determinant minus one and signature \((17,1)\).
These are direct finite matrix checks, without an inferred maximal-order or class-number calculation.

<a id="two-transvection-model"></a>
## Exact two-transvection form

Let
\[
\theta=(2,4,6,5,4,3,2,3;0,0,0,0,0,0,0,0)\in E_8\oplus E_8.
\]
It has squared norm two, and the image of \(h_8\) is \(e-\theta\).
Let \(P\) be the product of positive-root reflections in the order
\[
h_1,h_3,h_5,h_7,h_2,h_4,h_6,\ell,
\]
and let \(R=\sigma P\) on the positive summand, extended to fix \(e,f\).
The program verifies that \(R\) is an integral positive isometry of exact order sixty.

Write \(J=s_{e+f}\), so \(J(e)=-f\), \(J(f)=-e\), and \(J\) fixes the positive summand.
The reflection in \(h_9\) is \(J\), and it commutes with the other factors in its color and with the positive factors of the opposite color.
Thus the displayed source word becomes \(g=R J s_{e-\theta}\).
Direct substitution, using \((\theta,\theta)=2\), gives
\[
J s_{e-\theta}=T_{e,\theta}T_{f,\theta}.
\]
The program also checks the complete matrix equality
\[
A=R T_{e,\theta}T_{f,\theta}
\]
in the integral split basis.
All eighteen-dimensional characteristic coefficients equal the original H_ascending coefficients.
The nineteen-dimensional source polynomial is exactly \((x+1)H(x)\); the removed radical eigenvalue is minus one and has no Mahler cost.

<a id="results-and-limits"></a>
## Execution and interpretation

The exact program completed successfully and retained [coxeter_model.json](../../outputs/Yin_J_G0158/coxeter_model.json), reporting verified after all claimed finite checks passed.
The [separate independent finding](../../../audits/reviews/Yin_R_G1114_v6.md#coxeter-two-transvection-model-review) checks the whole argument, program, original input, source interface and all forty-two certificate fields.
Its [independent checker](checks/independent_coxeter_model_review.py) verifies all complete characteristic polynomials by exact determinant evaluations at sufficiently many distinct integers, separately from the author's Newton implementation.
The [actual independent result](../../outputs/Yin_J_G0158/independent_coxeter_model_review.json) reports verified.
The original [natural trace-lattice obstruction](discriminant_action.md#conclusion-and-limits) concerns a different Gram lattice and remains unchanged.
This independently checked known second small value belongs to the two-transvection family of [C885 v2](../../../claims/Yin_C_G0885_v2.md#decision-positive-lattice-two-transvection-gap).
It calibrates coverage of that family and produces neither a new value nor an escape from its positive-gap theorem.
The theorem's gap is not asserted to be an effective exclusion below \(6/5\).

From the repository root, run:

~~~text
python -B mathematics/computations/programs/Yin_J_G0158/coxeter_model.py
python -B mathematics/computations/programs/Yin_J_G0158/checks/independent_coxeter_model_review.py
~~~

Only the Python standard library and the retained author matrix helpers in trace_lattice.py are required.
The fixed J144 polynomial is the only input file; earlier generated trace or discriminant certificates are not read.
The output is written only after all asserted integer identities, complete characteristic coefficients and definiteness checks succeed.
The independent checker requires that generated certificate, writes its separate result, and neither imports nor executes author code.
